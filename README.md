#  Broadcast Server (Python 3.10)

A simple real-time broadcast server built with Python and WebSockets that supports:
- Multiple clients
- Message broadcasting
- Message history saved to file
- Automatic sync of past messages when new clients connect

---

##  Features

-  Multiple clients can connect simultaneously
-  Clients send messages → broadcast to all others
-  Messages are saved in `chat.log`
-  When a client connects, they receive all previous messages (chat history)
-  Clean shutdown and disconnection handling
-  Each client gets a random ID

---

##  Requirements

- Python 3.10+
- [`websockets`](https://pypi.org/project/websockets/) library

Install dependencies:

```bash
pip install -r requirements.txt

