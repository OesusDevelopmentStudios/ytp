import sys

from pytubefix import YouTube

from utils.utils import check_link


def main(args: list[str]) -> int:
    if len(args) < 2:
        return 400

    link: str = args[1]
    if not check_link(link):
        return 404

    video = YouTube(link)

    author = video.author
    if " - Topic" in author:
        author = author.replace(" - Topic", "")
    print(author)
    print(video.title)

    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
