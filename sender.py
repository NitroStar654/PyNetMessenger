import argparse
import re
import socket
import sys

DEFAULT_PORT = 3000
IP_REGEX = r"^\d{1,3}(\.\d{1,3}){3}$"


def validate_ip(ip):
    return re.match(IP_REGEX, ip) and all(0 <= int(num) <= 255 for num in ip.split("."))


def parse_arguments():
    parser = argparse.ArgumentParser(description="UDP Sender")
    parser.add_argument("-i", "--ip", required=True, help="Destination IP address")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT,
                        help=f"Destination port (default: {DEFAULT_PORT})")
    args = parser.parse_args()

    if not validate_ip(args.ip):
        print("Error: Invalid IP address format.")
        sys.exit(1)

    if not (1 <= args.port <= 65535):
        print("Error: Port must be a valid integer between 1 and 65535.")
        sys.exit(1)

    return args.ip, args.port


def send_udp_message(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.sendto(message.encode(), (ip, port))
        except (socket.gaierror, socket.error) as sock_error:
            print(f"Error: {sock_error}")
            sys.exit(1)


if __name__ == "__main__":
    try:
        destination_ip, destination_port = parse_arguments()
        print("Press Ctrl+C to exit")
        print(f"You will send messages to {destination_ip}:{destination_port}")

        while True:
            if message_to_send := input("Message to send: ").strip():
                send_udp_message(destination_ip, destination_port, message_to_send)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)
