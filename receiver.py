import socket
import sys
from datetime import datetime, timezone

DEFAULT_PORT = 3000


def get_listen_port():
    while True:
        port_input = input(f"Listener Port (default {DEFAULT_PORT}): ")
        if not port_input:
            return DEFAULT_PORT
        try:
            port = int(port_input)
            if 1 <= port <= 65535:
                return port
        except ValueError:
            pass
        print("Error: Port must be a valid integer between 1 and 65535.")


def receive_udp_message(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((ip, port))
        print(f"Listening on {ip}:{port}... Press Ctrl+C to exit")
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode().strip()
            current_time = datetime.now(timezone.utc).strftime('%H:%M:%S UTC')
            print(f"{current_time} - Received message from {addr[0]}: {message}")


if __name__ == "__main__":
    try:
        listen_ip = '0.0.0.0'
        listen_port = get_listen_port()
        receive_udp_message(listen_ip, listen_port)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)
