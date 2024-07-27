import os
import sys

from pytubefix import YouTube

from utils.utils import check_link


def download(link: str) -> int:
    video = YouTube(link)
    title:str = video.title + ".mp3"

    stream = video.streams.get_audio_only()
    file = stream.download()
    os.rename(file, title)
    return 0


def main(args: list[str]) -> int:
    if len(args) < 2:
        return 400
    link: str = args[1]
    if not check_link(link):
        return 404
    download(link)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
