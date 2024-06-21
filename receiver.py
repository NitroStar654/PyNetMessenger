import socket
from datetime import datetime, timezone
import sys


def receive_udp_message(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((ip, int(port)))
        print("Press Ctrl+C to exit")
        print(f"Listening on {ip}:{port}...")
        while True:
            data, addr = sock.recvfrom(1024)
            current_time = datetime.now(timezone.utc).strftime('%H:%M:%S GMT')
            print(f"{current_time} - Received message from {addr[0]}: {data.decode()}")
    except ValueError:
        print("Error: Port must be an integer")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    listen_ip = '0.0.0.0'
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
            print("\nProgram stopped")
            sys.exit(0)
