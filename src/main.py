from textnode import *
from htmlnode import *
from blocktype import BlockType
from inline_markdown import *
from block_markdown import *
import re, os, shutil


def main():
    static_to_public()
    generate_page("./content/index.md", "./template.html", "./public/index.html")


def static_to_public():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    copy_files_recursive("./static", "./public")
    return

def copy_files_recursive(source, destination):
    # Checks if destination directory exists; if not, creates it.
    if not os.path.exists(destination):
        os.mkdir(destination)

    # Gets the list of files from the source directory
    files = os.listdir(source)

    for file in files:
        source_path = os.path.join(source, file)
        dest_path = os.path.join(destination, file)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_files_recursive(source_path, dest_path)
    return

def extract_title(markdown):
    lines = markdown.split("\n")
    title = None
    for line in lines:
        if re.match(r'^#{1} ', line):
            title = line
            break
    if not title:
        raise Exception("No valid title header found")
    title = title.strip("#")
    title = title.strip()
    return title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    title = extract_title(markdown)
    node = markdown_to_html_node(markdown)
    node_html = node.to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", node_html)

    with open(dest_path, "w") as file:
        file.write(template)
    

main()
