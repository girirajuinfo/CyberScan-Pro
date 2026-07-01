import requests
from urllib.parse import urlparse


def check_robots_and_sitemap(url):

    parsed = urlparse(url)

    base_url = f"{parsed.scheme}://{parsed.netloc}"

    robots_url = base_url + "/robots.txt"
    sitemap_url = base_url + "/sitemap.xml"

    result = {}

    # robots.txt

    try:

        response = requests.get(robots_url, timeout=5)

        result["robots"] = response.status_code == 200

    except:

        result["robots"] = False

    # sitemap.xml

    try:

        response = requests.get(sitemap_url, timeout=5)

        result["sitemap"] = response.status_code == 200

    except:

        result["sitemap"] = False

    return result