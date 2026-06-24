# Build a logger that writes every action to a log file with a timestamp. 

import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "actions.log")


def log_action(action):
    timestamp = datetime.now()
    with open(LOG_PATH, "a") as file:
        file.write(f"{timestamp} - {action}\n")


log_action("Program started")
log_action("User opened the app")
log_action("Program finished")
