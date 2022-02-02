import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Pages loader')
    parser.add_argument('url')
    parser.add_argument('--path',
                        help='Path of output',
                        default='')
    args = parser.parse_args()
    return args
