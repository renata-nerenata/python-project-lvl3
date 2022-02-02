import re
from page_loader.constants import *


def get_filename(url):
    filename = get_new_name(url)
    return add_extention(filename)


def get_dirname(url):
    filename = get_new_name(url)
    return filename + '_files'


def get_new_name(s):
    page = re.sub(PROTOCOL, "", s)
    page = re.sub(re.compile(NUMBER_LETTERS), '-', page)
    return page


def add_extention(page):
    return page + EXTENSION
