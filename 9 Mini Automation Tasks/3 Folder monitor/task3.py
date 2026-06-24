# Write a script that prints the name of any new file added to a folder (basic file monitoring)
import os
import time

folder = os.path.dirname(os.path.abspath(__file__))
seen_files = set(os.listdir(folder))
print("Watching for new files...")

while True:
    current_files = set(os.listdir(folder))
    new_files = current_files - seen_files
    for filename in new_files:
        print("New file added:", filename)

    seen_files = current_files
    time.sleep(2)
