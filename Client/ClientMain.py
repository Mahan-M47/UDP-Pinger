import time
from socket import *

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000


def main():

    # Connect to the server
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(1)

    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"UDP connection to {SERVER_HOST}:{SERVER_PORT}")

    rtt_list = []

    for i in range(1, 11):
        try:
            time_sent = time.time()
            request = f"Ping {i} - sent= {time_sent:.3f}"
            client_socket.sendall(request.encode())

            response = client_socket.recv(1024)
            time_received = time.time()
            rtt = time_received - time_sent
            print(response.decode() + f" - RTT= {rtt}")

            rtt_list.append(rtt)

        except ConnectionResetError:
            print("Connection failed")
        except timeout:
            print("Request timed out")

    client_socket.close()

    print(f"\nMinimum RTT= {min(rtt_list)}")
    print(f"Maximum RTT= {max(rtt_list)}")
    print(f"Average RTT= {sum(rtt_list)/len(rtt_list)}")
    print(f"Packet Loss= {((10 - len(rtt_list))/10)*100}%")


if __name__ == "__main__":
    main()
