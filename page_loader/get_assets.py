import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from page_loader.get_names import get_filename


def download_assets(page_html, page_url, directory, path_assets):
    soup = BeautifulSoup(page_html, 'html.parser')
    tags = soup.find_all(['link', 'script', 'img'])

    for tag in tags:
        extra_content = get_type(tag.name)
        full_url_assets = urljoin(page_url + '/',
                                       tag.get(extra_content))

        if urlparse(full_url_assets).netloc == urlparse(page_url).netloc:
            filename = get_filename(full_url_assets)
            full_path_assets = os.path.join(path_assets, filename)

            download_asset(full_url_assets, full_path_assets)

            tag[extra_content] = os.path.join(
                directory,
                filename
            )
    return soup.prettify()


def get_type(tag):
    if tag == 'img':
        return 'src'
    elif tag == 'link':
        return 'href'
    elif tag == 'script':
        return 'src'


def download_asset(url, full_path_assets):
    response = requests.get(url, stream=True)
    with open(full_path_assets, 'wb') as output_file:
        output_file.write(response.content)
