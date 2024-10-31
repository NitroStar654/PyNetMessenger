import socket
import sys
from datetime import datetime, timezone

DEFAULT_LISTEN_PORT = 3000
sock = None


def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def receive_udp_message(ip, port):
    global sock
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((ip, port))
            print(f"Listening on {ip}:{port}... Press Ctrl+C to exit")

            while True:
                data, addr = sock.recvfrom(1024)
                message = data.decode().strip()
                current_time = datetime.now(timezone.utc).strftime('%H:%M:%S GMT')
                print(f"{current_time} - Received message from {addr[0]}: {message}")

    except ValueError:
        print("Error: Port must be an integer")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)


def get_listen_port():
    while True:
        port_input = input(f"Listener Port (default {DEFAULT_LISTEN_PORT}): ")
        if not port_input:
            return DEFAULT_LISTEN_PORT
        try:
            return int(port_input)
        except ValueError:
            print("Error: Destination port must be a valid integer.")


if __name__ == "__main__":
    listen_ip = '0.0.0.0'
    try:
        listen_port = get_listen_port()
        receive_udp_message(listen_ip, listen_port)

    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
