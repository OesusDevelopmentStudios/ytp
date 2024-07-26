import requests
import validators


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
