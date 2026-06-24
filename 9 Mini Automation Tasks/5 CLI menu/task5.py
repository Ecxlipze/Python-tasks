# Bonus: put all of the above behind a small CLI menu (1 = organize files, 2 = view


import os
import shutil
import time
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def organize_files():
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    doc_extensions = [".txt", ".pdf", ".doc", ".docx"]

    for filename in os.listdir(BASE_DIR):
        if filename == os.path.basename(__file__):
            continue
        source_path = os.path.join(BASE_DIR, filename)
        if os.path.isdir(source_path):
            continue
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        if extension in image_extensions:
            target_folder = os.path.join(BASE_DIR, "images")
        elif extension in doc_extensions:
            target_folder = os.path.join(BASE_DIR, "docs")
        else:
            target_folder = os.path.join(BASE_DIR, "others")
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        destination_path = os.path.join(target_folder, filename)
        shutil.move(source_path, destination_path)

    print("Files organized.")


def view_log():
    log_path = os.path.join(BASE_DIR, "actions.log")

    try:
        with open(log_path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No log file found.")


def watch_folder():
    seen_files = set(os.listdir(BASE_DIR))
    print("Watching for new files. Press Ctrl+C to stop.")

    while True:
        current_files = set(os.listdir(BASE_DIR))
        new_files = current_files - seen_files

        for filename in new_files:
            print("New file added:", filename)

        seen_files = current_files
        time.sleep(2)


def reminder():
    while True:
        print("Reminder: take a short break")
        time.sleep(5)


def log_action(action):
    log_path = os.path.join(BASE_DIR, "actions.log")
    timestamp = datetime.now()

    with open(log_path, "a") as file:
        file.write(f"{timestamp} - {action}\n")


while True:
    print("1. Organize files")
    print("2. View log")
    print("3. Watch folder")
    print("4. Reminder")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        log_action("Organize files selected")
        organize_files()
    elif choice == "2":
        log_action("View log selected")
        view_log()
    elif choice == "3":
        log_action("Watch folder selected")
        watch_folder()
    elif choice == "4":
        log_action("Reminder selected")
        reminder()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
