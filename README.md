# PyNetMessenger

Welcome to the PyNetMessenger project! This repository contains scripts for creating a simple messaging system over a
local network using Python sockets.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
    - [Sender Usage](#sender-usage)
    - [Receiver Usage](#receiver-usage)
- [License](#license)

## Overview

PyNetMessenger provides a simple client-server setup that enables communication between two devices on the same network.
The sender sends messages, while the receiver listens for incoming messages on a specified port.

This project is great for learning about Python socket programming and basic networking concepts.

## Installation

Make sure Python 3 is installed on both devices (sender and receiver). This project does not have any external
dependencies.

### Clone the Repository

```
git clone https://github.com/NitroStar654/PyNetMessenger.git
cd PyNetMessenger
```

## Usage

### Sender Usage

The `sender.py` script allows you to send messages to the receiver.

#### Running sender.py

```
python sender.py
```

#### Example:

```
python sender.py
Destination IP: 192.168.0.25
Destination Port (default 3000): 5215
Message to send: Hello!
```

You will then be able to type a message, which will be sent to the receiver at the specified IP and port.

### Receiver Usage

The `receiver.py` script sets up the receiver to listen for incoming messages.

#### Running receiver.py

```
python receiver.py
```

#### Example:

```
python receiver.py
Listener Port (default 3000): 5215
Listening on 0.0.0.0:5215... Press Ctrl+C to exit
20:49:23 GMT - Received message from 192.168.0.20: Hello!
```

The server will then listen on the specified port, waiting for messages from the sender. The default 0.0.0.0 address is
used
to listen on all network interfaces.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

We hope you find PyNetMessenger useful for your learning and development projects! If you have any questions or
encounter any issues, feel free to open an issue on GitHub.

---
