import requests
import re

base_url = "https://scannables.scdn.co/uri/plain/png/000000/white/640/spotify:"
spotify_regex = r"https://open.spotify.com/(\w*)/([\w\d]*)\?si=[\w\d]*"


def get_spotify_code_image(spotify_url: str):
    """Gets and return the spotify code of a track/playlist/album from a spotify url

    :param spotify_url: the spotify url of the track/playlist/album
                        that you get by clicking the 3 ••• and selecting share > copy the link to ...
    :type spotify_url: str
    :return: an image corresponding to the spotify code
    :rtype: img
    """
    url = _generate_scannables_url(spotify_url)
    if url:
        r = requests.get(url)
        if r.status_code == 200:
            return r.content
    return None


def _generate_scannables_url(spotify_url: str):
    """Generate the callable scannables url to fetch the spotify code

    :param spotify_url: the spotify url of the track/playlist/album
                        that you get by clicking the 3 ••• and selecting share > copy the link to <resource>
    :type spotify_url: str
    :return: scannables url to access the resource
    :rtype: str
    """
    m = re.match(spotify_regex, spotify_url)
    if m:
        return base_url + m.group(1) + ':' + m.group(2)
    return None
