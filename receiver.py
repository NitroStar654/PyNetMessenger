import argparse
import socket
import sys
from datetime import datetime, timezone

DEFAULT_PORT = 3000
BUFFER_SIZE = 4096


def parse_args():
    parser = argparse.ArgumentParser(description="UDP Listener")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT, help="Listening port (default: 3000)")
    return parser.parse_args()


def receive_udp_message(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((ip, port))
        print(f"Listening on {ip}:{port}... (Press Ctrl+C to stop)")

        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            message = data.decode().strip()
            current_time = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M:%S UTC")
            print(f"[{current_time}] {addr[0]}:{addr[1]} → {message}")


if __name__ == "__main__":
    try:
        args = parse_args()
        receive_udp_message("0.0.0.0", args.port)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)
