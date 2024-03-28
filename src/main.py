from recursive_copy import recursive_copy
from markdown_to_htmlnode import *
import os

def main():
    recursive_copy('static', 'public')
    generate_page('content/index.md', 'template.html', 'public/index.html')


if __name__ == "__main__":
    main()
