import re

markdown_image_pattern = r"!\[(.*?)\]\((.*?)\)"
markdown_link_pattern = r"\[(.*?)\]\((.*?)\)"

def extract_markdown_images(text):
    return re.findall(markdown_image_pattern, text)


def replace_markdown_images(text, repl):
    return re.sub(markdown_image_pattern, repl, text)


def extract_markdown_links(text):
    return re.findall(markdown_link_pattern, text)


def replace_markdown_links(text, repl):
    return re.sub(markdown_link_pattern, repl, text)