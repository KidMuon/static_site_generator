from recursive_copy import recursive_copy
from markdown_to_htmlnode import *
import os, shutil

def main():
    recursive_copy('static', 'public')
    generate_page_recursive('content', 'template.html', 'public')


if __name__ == "__main__":
    main()
