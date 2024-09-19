import socket
import requests
import threading
import time

# Adresse IP du destinataire (à remplacer par l'IP de réception)
dest_ip = "localhost"
dest_port = 6666


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def send_ip_periodically():
    local_ip = get_local_ip()
    while True:
        send_ip(local_ip)
        time.sleep(60)


def send_ip(local_ip):
    try:
        response = requests.post(f"http://{dest_ip}:{dest_port}/receive_ip", json={'ip': local_ip})
        response.raise_for_status()
        print(f"IP sent successfully to {dest_ip}:{dest_port}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send IP: {e}")


if __name__ == "__main__":
    threading.Thread(target=send_ip_periodically, daemon=True).start()

    while True:
        time.sleep(1)
