#  UDP-Pinger

The goal of this project is to build a local ping server and allow clients to ping the server. Unlike the standard ICMP protocol, this implementation uses UDP as the transport-layer protocol, where packet loss may occur. The client will display statistics such as average Round Trip Time (RTT) and packet loss percentage.

This repository contains two main Python scripts: `ServerMain.py` for the server and `ClientMain.py` for the client. This project was created for my Computer Networks course in Spring 2024.

### Key Features:
- Simulated packet loss to demonstrate UDP's unreliability.
- RTT calculation for each ping message.
- Statistics on minimum, maximum, and average RTT.


## Server Features

The server code is located in `ServerMain.py`. The server is designed to echo the messages it receives back to the client, using UDP for communication. The server creates a socket of type `SOCK_DGRAM` and binds it to a specified host address and port. 

Once started, the server enters listening mode, awaiting incoming client messages. Each received message has a 70% chance of being echoed back, with a 30% chance of no response to simulate packet loss, making the process unpredictable.


## Client Features

The client code is located in `ClientMain.py`. To communicate with the server, the client must know the server's IP address and port. Similar to the server, the client creates a `SOCK_DGRAM` socket to send UDP messages. Since UDP is connectionless, no handshake is required.

The client sends 10 UDP messages to the server. However, as the server might not respond to every message due to simulated packet loss, a timeout of 1 second is set. If no response is received within the timeout, the client assumes the packet was lost and handles the timeout exception.

The client will display the RTT for each message and calculate the minimum, maximum, and average RTT at the end of the communication.


## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
