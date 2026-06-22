# Build a logger that writes every action to a log file with a timestamp. 

from datetime import datetime

def log_action(action):
    timestamp = datetime.now()
    with open("actions.log", "a") as file:
        file.write(f"{timestamp} - {action}\n")

log_action("Program started")
log_action("User opened the app")
log_action("Program finished")
