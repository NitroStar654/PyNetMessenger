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
    finally:
        sock.close()


if __name__ == "__main__":
    try:
        destination_ip = input("Destination IP: ")

        while True:
            destination_port = input("Destination Port: ")
            try:
                destination_port = int(destination_port)
                break
            except ValueError:
                print("Error: Destination port must be a valid integer.")

        print("Press Ctrl+C to exit")
        while True:
            message_to_send = input("Message to send: ")
            send_udp_message(destination_ip, destination_port, message_to_send)
    except KeyboardInterrupt:
        print("\nProgram stopped")
        sys.exit(0)
