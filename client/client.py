import socket
import argparse

def send_message(args):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((args.ip, int(args.port)))
        s.sendall(args.message.encode("utf-8"))
        s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LEDuino Client CLI")

    parser.add_argument(
        '--ip', '-i', help="LEDuino IP Address", required=True)
    parser.add_argument(
        '--port', '-p', help="LEDuino Port", required=True)
    parser.add_argument(
        '--message', '-m', help="Message to Send", required=True)

    args = parser.parse_args()
    send_message(args)