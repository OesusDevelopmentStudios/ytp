import sys

from pytubefix import Playlist

from utils.utils import check_link


def main(args: list[str]) -> int:
    if len(args) < 2:
        return 400

    link: str = args[1]
    if not check_link(link):
        return 404

    links: list[str] = []
    playlist = Playlist(link)
    for video in playlist.videos:
        links.append("https://www.youtube.com/watch?v=" + video.video_id)
    print(links)

    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
