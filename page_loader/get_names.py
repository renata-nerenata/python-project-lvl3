import re
import os
from page_loader.constants import *


def get_filename(url):
    filename, extension = get_new_name(url)
    return add_extension(filename, extension)


def get_dirname(url):
    filename, _ = get_new_name(url)
    return filename + '_files'


def get_new_name(s):
    page, extension = os.path.splitext(s)
    if extension:
        pass
    else:
        extension = '.html'
    page = re.sub(PROTOCOL, "", s)
    page = re.sub(re.compile(NUMBER_LETTERS), '-', page)
    return page, extension


def add_extension(page, extension):
    return page + extension
