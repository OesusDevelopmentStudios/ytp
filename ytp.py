import sys

from ytp_scripts import (
    check_link,
    download,
    get_info,
    get_videos,
)


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
