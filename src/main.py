from recursive_copy import recursive_copy
from markdown_to_htmlnode import *
import os

def main():
    recursive_copy('static', 'public')
    generate_page('content/index.md', 'template.html', 'public/index.html')
    #document = """# Heading text \n\n* Quick list `code` and \n* Quick list2"""
    #html = markdown_to_htmlnode(document).to_html()
    #print(html)


if __name__ == "__main__":
    main()
