from page_loader.get_args import get_args
from page_loader.download import download


def main():
    args = get_args()
    filepath = download(args.url, args.path)
    print("Find your page in {}".format(filepath))


if __name__ == '__main__':
    main()
