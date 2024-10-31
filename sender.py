import sys
import socket
import re

DEFAULT_PORT = 3000
IP_REGEX = r"^\d{1,3}(\.\d{1,3}){3}$"


def send_udp_message(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message.encode(), (ip, port))
    except socket.gaierror as gai_error:
        print(f"Error: Invalid address or hostname, {gai_error}")
        exit_program(1)
    except socket.error as socket_error:
        print(f"Error: {socket_error}")
        exit_program(1)
    finally:
        sock.close()


def get_port():
    while True:
        port_input = input(f"Destination Port (default {DEFAULT_PORT}): ")
        if port_input.strip() == "":
            return DEFAULT_PORT
        try:
            port = int(port_input)
            if 1 <= port <= 65535:
                return port
            else:
                print("Error: Port must be between 1 and 65535.")
        except ValueError:
            print("Error: Destination port must be a valid integer.")


def validate_ip(ip):
    if re.match(IP_REGEX, ip):
        return all(0 <= int(num) <= 255 for num in ip.split("."))
    return False


def exit_program(exit_code=0):
    print("\nProgram stopped")
    sys.exit(exit_code)


if __name__ == "__main__":
    try:
        while True:
            destination_ip = input("Destination IP: ").strip()
            if validate_ip(destination_ip):
                break
            print("Error: Invalid IP address format.")
        destination_port = get_port()
        print("Press Ctrl+C to exit")
        while True:
            message_to_send = input("Message to send: ").strip()
            if message_to_send:
                send_udp_message(destination_ip, destination_port, message_to_send)

    except KeyboardInterrupt:
        exit_program(0)
