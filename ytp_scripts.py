import os
import requests
import validators

from pytubefix import (
    Playlist,
    YouTube
)


YT_LINK_PATTERN = "https://www.youtube."
YT_MATCHER = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'


def check_link(link: str) -> bool:
    if not link.startswith(YT_LINK_PATTERN):
        return False
    if not validators.url(link):
        return False
    try:
        remote = requests.get(link)
    except:
        return False
    if remote.status_code != 200:
        return False

    return False if YT_MATCHER in remote.text else True


def download(link: str) -> bool:
    video = YouTube(link)
    title:str = video.title + ".mp3"

    try:
        stream = video.streams.get_audio_only()
        file = stream.download()
    except:
        return False
    os.rename(file, title)
    return True


def get_info(link: str) -> list[str]:
    video = YouTube(link)
    author = video.author
    if " - Topic" in author:
        author = author.replace(" - Topic", "")
    return [video.title, author]


def get_videos(link: str) -> list[str]:
    links: list[str] = []
    playlist = Playlist(link)
    for video in playlist.videos:
        links.append("https://www.youtube.com/watch?v=" + video.video_id)
    return links
