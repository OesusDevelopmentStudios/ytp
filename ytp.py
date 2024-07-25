import requests
import sys

from pytubefix import YouTube


YT_MATCHER = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'


def check_link(link: str) -> bool:
    remote = requests.get(link)
    if remote.status_code == 200:
        print("Site does not exist")
        return False
    return False if YT_MATCHER in remote.text else True


def main(args: list[str]) -> int:
    if len(args) < 2:
        return 400

    link: str = args[1]
    if not check_link(link):
        return 404

    video = YouTube(link)
    title:str = video.title + ".mp3"

    stream = video.streams.get_audio_only()
    stream.download(output_path=title)

    print(video.author)
    print(video.title)

    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
