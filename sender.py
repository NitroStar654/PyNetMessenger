import sys
import socket


def send_udp_message(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message.encode(), (ip, port))
    except socket.gaierror as gai_error:
        print(f"Error: Invalid address or hostname, {gai_error}")
        sys.exit(1)
    except socket.error as socket_error:
        print(f"Error: {socket_error}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
    finally:
        sock.close()


def get_port():
    while True:
        port_input = input("Destination Port (default 7777): ")
        if port_input.strip() == "":
            return 7777
        try:
            port = int(port_input)
            if 1 <= port <= 65535:
                return port
            else:
                print("Error: Port must be between 1 and 65535.")
        except ValueError:
            print("Error: Destination port must be a valid integer.")


if __name__ == "__main__":
    try:
        destination_ip = input("Destination IP: ")

        destination_port = get_port()

        print("Press Ctrl+C to exit")
        while True:
            message_to_send = input("Message to send: ")
            send_udp_message(destination_ip, destination_port, message_to_send)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
