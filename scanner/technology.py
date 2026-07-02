import requests


def detect_technology(url):

    try:

        response = requests.get(url, timeout=5)

        headers = response.headers

        result = {

            "server": headers.get("Server", "Unknown"),

            "powered_by": headers.get("X-Powered-By", "Not Detected")

        }

        return result

    except:

        return {

            "server": "Unknown",

            "powered_by": "Unknown"

        }