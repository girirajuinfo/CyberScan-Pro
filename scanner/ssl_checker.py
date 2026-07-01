import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime


def check_ssl_certificate(url):

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443), timeout=5) as sock:

        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:

            cert = secure_sock.getpeercert()

    issuer = dict(x[0] for x in cert["issuer"])

    expiry_date = datetime.strptime(
        cert["notAfter"],
        "%b %d %H:%M:%S %Y %Z"
    )

    days_left = (expiry_date - datetime.utcnow()).days

    return {
        "issuer": issuer.get("organizationName", "Unknown"),
        "expiry": expiry_date.strftime("%Y-%m-%d"),
        "days_left": days_left,
        "valid": days_left > 0
    }