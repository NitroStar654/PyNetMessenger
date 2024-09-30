# PyNetMessenger

Welcome to the PyNetMessenger project! This repository contains scripts for creating a simple messaging system over a local network using Python sockets.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
    - [Sender Usage](#sender-usage)
    - [Receiver Usage](#receiver-usage)
- [License](#license)

## Overview

PyNetMessenger provides a simple client-server setup that enables communication between two devices on the same network. The sender sends messages, while the receiver listens for incoming messages on a specified port.

This project is great for learning about Python socket programming and basic networking concepts.

## Installation

Make sure Python is installed on both devices (sender and receiver).

### Clone the Repository

```
git clone https://github.com/NitroStar654/PyNetMessenger.git
cd PyNetMessenger
```
### Install Dependencies

This project does not have any external dependencies besides Python. Ensure you are using Python 3.x.

## Usage

### Sender Usage

The sender.py script allows you to send messages to the server.

#### Running sender.py

```
python sender.py <server_ip> <port>
```

#### Example:
```
python sender.py 192.168.1.10 5000
```

You will then be able to type a message, which will be sent to the server at the specified IP and port.

### Receiver Usage

The receiver.py script sets up the server to listen for incoming messages.

#### Running receiver.py

```
python receiver.py <port>
```

#### Example:
```
python receiver.py 5000
```

The server will then listen on the specified port, waiting for messages from the sender.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

We hope you find PyNetMessenger useful for your learning and development projects! If you have any questions or encounter any issues, feel free to open an issue on GitHub.

---
