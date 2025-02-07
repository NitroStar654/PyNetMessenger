import re
import socket
import sys

DEFAULT_PORT = 3000
IP_REGEX = r"^\d{1,3}(\.\d{1,3}){3}$"


def validate_ip(ip):
    return re.match(IP_REGEX, ip) and all(0 <= int(num) <= 255 for num in ip.split("."))


def get_port():
    while True:
        port_input = input(f"Destination Port (default {DEFAULT_PORT}): ")
        if not port_input:
            return DEFAULT_PORT
        try:
            port = int(port_input)
            if 1 <= port <= 65535:
                return port
        except ValueError:
            pass
        print("Error: Port must be a valid integer between 1 and 65535.")


def send_udp_message(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.sendto(message.encode(), (ip, port))
        except (socket.gaierror, socket.error) as sock_error:
            print(f"Error: {sock_error}")
            sys.exit(1)


if __name__ == "__main__":
    try:
        while not (destination_ip := input("Destination IP: ").strip()) or not validate_ip(destination_ip):
            print("Error: Invalid IP address format.")
        destination_port = get_port()
        print("Press Ctrl+C to exit")
        while True:
            if message_to_send := input("Message to send: ").strip():
                send_udp_message(destination_ip, destination_port, message_to_send)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)
