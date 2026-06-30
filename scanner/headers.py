import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(url):

    response = requests.get(url, timeout=5)

    headers = response.headers

    results = {}

    for header in SECURITY_HEADERS:

        if header in headers:
            results[header] = "Present"
        else:
            results[header] = "Missing"

    return results