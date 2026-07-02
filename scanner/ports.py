import socket
from urllib.parse import urlparse


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}


def scan_ports(url):

    parsed = urlparse(url)
    hostname = parsed.hostname

    results = {}

    for port, service in COMMON_PORTS.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        status = sock.connect_ex((hostname, port))

        if status == 0:
            results[port] = service

        sock.close()

    return results