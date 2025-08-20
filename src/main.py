from textnode import *
from htmlnode import *
from blocktype import BlockType
from inline_markdown import *
from block_markdown import *
from generate_html import *
import re, os, shutil, sys


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    static_to_public()
    generate_page_recursive("./content", "./template.html", "./docs", basepath)



main()
