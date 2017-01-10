import os
import sys
import xerox
import requests
import logging
import argparse
import click


def check_file(ctx, param, file_path):
    if os.path.exists(str(file_path)):
        return file_path
    else:
        raise click.BadParameter(
            '{0} file doesn\'t exist'.format(file_path))


def get_data_from_file(file_path):
    syntax = None
    f = open(file_path, "r").read()
    content = f
    extension = file_path.split('.')[-1]
    lang = {"c": "c", "cpp": "cpp", "java": "java", "php": "php", "py": "python", "css": "css", "sh": "bash",
            "cs": "csharp", "html": "html", "js": "js", "m": "matlab", "go": "go", "pl": "perl", "rb": "ruby"}
    if extension in lang:
        syntax = [lang[extension], ]
    else:
        syntax = "text"
    return content, syntax


@click.command()
@click.option('--poster', '-p', default=os.popen('whoami').read(), help='Name of user who is posting content')
@click.option('--file', '-f', callback=check_file, help='Path to file')
def main(poster, file):
    payload = {}
    payload["poster"] = poster
    content, syntax = get_data_from_file(file)
    payload["content"] = content
    payload["syntax"] = syntax
    res = requests.post('http://paste.ubuntu.com', data=payload)
    link = res.url
    print ('link is {}'.format(link))
    xerox.copy(link)
    print ('It\'s copied to the clipboard !')

if __name__ == '__main__':
    main()
