import os
from datetime import datetime
from paths import *

def log_message(message):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file_name = f"{date_str}.txt"
    log_folder_path = os.path.join(ROOT, SAVED, "Logs")
    os.makedirs(log_folder_path, exist_ok=True)
    log_file_path = os.path.join(log_folder_path, log_file_name)

    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

def log_deletion(file_path):
    log_message(f"Deleted: {file_path}")

def log_move(original_path, new_path):
    log_message(f"Moved: From {original_path} to {new_path}")
