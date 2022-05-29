# HTTP requests
import requests
# Regex
import re
# Image processing
from PIL import Image
import io
# Misc
from enum import Enum

base_url = "https://scannables.scdn.co/uri/plain/png/000000/white/"
headers = {'content-type': 'image/png'}
spotify_regex = r"https://open.spotify.com/(\w*)/([\w\d]*)\?si=[\w\d]*"


class Sizes:
    SMALL = 320
    MEDIUM = 640
    BIG = 1080


def get_spotify_code_image(spotify_url: str, size=640):
    """Gets and return the spotify code of a track/playlist/album from a spotify url

    :param spotify_url: the spotify url of the track/playlist/album
                        that you get by clicking the 3 ••• and selecting share > copy the link to ...
    :type spotify_url: str
    :param size: width of the output image, must be a valid size (320, 480, 640, 720, 940, 1080...)
    :type size: int
    :return: an image corresponding to the spotify code
    :rtype: Image
    """
    url = _generate_scannables_url(spotify_url, size)
    if url:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return _get_image_from_bytes(r.content)
    return None


def _generate_scannables_url(spotify_url: str, size=640):
    """Generate the callable scannables url to fetch the spotify code

    :param spotify_url: the spotify url of the track/playlist/album
                        that you get by clicking the 3 ••• and selecting share > copy the link to <resource>
    :type spotify_url: str
    :param size: width of the output image, must be a valid size (320, 480, 640, 720, 940, 1080...)
    :type size: int
    :return: scannables url to access the resource
    :rtype: str
    """
    m = re.match(spotify_regex, spotify_url)
    if m:
        return base_url + str(size) + '/spotify:' + m.group(1) + ':' + m.group(2)
    return None


def _get_image_from_bytes(b: bytes):
    return Image.open(io.BytesIO(b))
