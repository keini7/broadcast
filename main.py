import argparse
import subprocess
import sys
import os

def start_server():
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "server.py")])

def start_client():
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "client.py")])

def main():
    parser = argparse.ArgumentParser(description="Broadcast Server CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("start", help="Start the broadcast server")
    subparsers.add_parser("connect", help="Connect to the broadcast server as a client")

    args = parser.parse_args()

    if args.command == "start":
        start_server()
    elif args.command == "connect":
        start_client()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
