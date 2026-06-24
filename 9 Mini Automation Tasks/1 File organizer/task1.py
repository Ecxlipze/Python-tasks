# Write a script that moves all files in a folder into subfolders by type (images, docs, etc)
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
doc_extensions = [".txt", ".pdf", ".doc", ".docx"]

for filename in os.listdir(BASE_DIR):
    if filename == "task1.py":
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
