import os
import requests
from page_loader.get_names import get_filename, get_dirname
from page_loader.get_assets import download_assets
import logging


def create_if_not_exists(path):
    if not os.path.exists(path):
        logging.warning('Path is not exists. Directory was created: {}'.format(path))
        os.mkdir(path)


def download(url, path=''):
    data = requests.get(url)
    if data.status_code != 200:
        logging.warning('URL Problems: {}'.format(data.status_code))

    path_saving = os.path.join(os.getcwd(), path)
    path_page = os.path.join(path_saving, get_filename(url))
    path_assets = os.path.join(path_saving, get_dirname(url))

    create_if_not_exists(path_assets)

    assets = download_assets(data.text,
                             url,
                             get_dirname(url),
                             path_assets)
    
    with open(path_page, 'w') as file:
        file.write(assets)
    return path_page
