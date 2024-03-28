from textnode import TextNode
from markdown_to_htmlnode import markdown_to_htmlnode


def main():
    document = """ ### Heading text \n\n* Quick list \n* Quick list2"""
    html = markdown_to_htmlnode(document)
    print(html.to_html())


if __name__ == "__main__":
    main()
