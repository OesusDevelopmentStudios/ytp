import sys

from utils.utils import check_link

from ytp_download import download
from ytp_info import get_info
from ytp_playlist import get_videos


PLAYLIST_PATTERN: str = "&list="


def main(args: list[str]) -> int:
    if len(args) < 2:
        print("Please provide link")
    link: str = args[1]
    if not check_link(link):
        print("Not a valid link")
    videos: list[str] = [link]
    if PLAYLIST_PATTERN in link:
        videos = get_videos(link)

    for video in videos:
        info = get_info(video)
        print("Downloading " + info[0] + " by " + info[1])
        download(video)

    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
