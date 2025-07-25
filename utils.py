import random
import string
from datetime import datetime

def generate_client_id(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def current_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def format_message(sender_id: str, message: str):
    return f"[{current_timestamp()}] {sender_id}: {message}"
