import os, shutil, re
from block_markdown import markdown_to_html_node



def static_to_public():
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    os.mkdir("./docs")
    copy_files_recursive("./static", "./docs")
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


def generate_page(from_path, template_path, dest_path, basepath):
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
    template = template.replace('href="/', 'href="{basepath}')
    template = template.replace('src="/', 'src="{basepath}')

    with open(dest_path, "w") as file:
        file.write(template)
    
def generate_page_recursive(content_dir_path, template_path, dest_dir_path, basepath):
    print(f"Building list of files from {content_dir_path}")
    files = os.listdir(content_dir_path)
    print(f"File list built, cycling through now.")
    for f in files:
        print(f"Working on file {f}")
        filepath = os.path.join(content_dir_path, f)
        destpath = os.path.join(dest_dir_path, f)
        print(f"Source filepath is {filepath}, destination is {destpath}")
        if os.path.isfile(filepath):
            print(f"{f} is a file, so we're making a page for it.")
            destpath = destpath.replace(".md", ".html")
            print(f"Fixed {destpath} so it's .html instead of .md")
            generate_page(filepath, template_path, destpath, basepath)
        else:
            print(f"{f} is a folder, so we're making a directory for it and going another layer deeper.")
            os.mkdir(destpath)
            generate_page_recursive(filepath, template_path, destpath, basepath)
