# PyNetMessenger

Welcome to the PyNetMessenger project! This repository contains scripts for creating a simple messaging system over a
local network using Python sockets.

## Table of Contents

- [Overview](#Overview)
- [Installation](#Installation)
- [Usage](#Usage)
    - [Sender Usage](#Sender-Usage)
    - [Receiver Usage](#Receiver-Usage)
- [Contributing](#contributing)
- [License](#License)

## Overview

PyNetMessenger provides a simple client-server setup that enables communication between two devices on the same network.
The sender sends messages, while the receiver listens for incoming messages on a specified port.

This project is great for learning about Python socket programming and basic networking concepts.

## Installation

Make sure Python 3 is installed on both devices (sender and receiver). This project does not have any external
dependencies.

### Clone the Repository

```bash
git clone https://github.com/NitroStar654/PyNetMessenger.git
cd PyNetMessenger
```

## Usage

### Sender Usage

The `sender.py` script allows you to send messages to the receiver.

#### Running sender.py

```bash
python sender.py -i <Destination IP> -p <Destination Port>
```

#### Example:

```bash
python sender.py -i 192.168.0.25 -p 5215
You will send messages to 192.168.0.25:5215
Message to send: Hello!
```

You will then be able to type a message, which will be sent to the receiver at the specified IP and port.

### Receiver Usage

The `receiver.py` script sets up the receiver to listen for incoming messages.

#### Running receiver.py

```bash
python receiver.py -p <Listener Port>
```

#### Example:

```bash
python receiver.py -p 5215
Listening on 0.0.0.0:5215... Press Ctrl+C to exit
[20/10/2024 20:49:23 UTC] 192.168.0.20:5215 → Hello!
```

The server will then listen on the specified port, waiting for messages from the sender. The default 0.0.0.0 address is
used to listen on all network interfaces.

## Contributing

We welcome contributions to PyNetMessenger! If you'd like to improve the project, feel free to:

- Report bugs or suggest features by opening an issue.
- Submit a pull request with enhancements, bug fixes, or documentation improvements.
- Share your feedback and ideas to help us make PyNetMessenger even better.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

We hope you find PyNetMessenger useful for your learning and development projects! If you'd like to contribute, check
out the [Contributing](#Contributing) section. Your feedback and improvements are always welcome!

---
