import logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d %b %Y, %H:%M:%S",
)
import os
import shutil
from config import INPUT_FOLDER, OUTPUT_FOLDER


def organize_files():
    files = os.listdir(INPUT_FOLDER)

    for file in files:
        file_name = file.lower()
        source_path = os.path.join(INPUT_FOLDER, file)

        if file_name.endswith(".pdf"):
            destination_folder = os.path.join(OUTPUT_FOLDER, "pdfs")

        elif file_name.endswith((".png", ".jpg", ".jpeg")):
            destination_folder = os.path.join(OUTPUT_FOLDER, "images")

        elif file_name.endswith(".txt"):
            destination_folder = os.path.join(OUTPUT_FOLDER, "texts")

        else:
            destination_folder = os.path.join(OUTPUT_FOLDER, "others")

        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        message = f"Moved {file} -> {destination_folder}"
        print(message)
        logging.info(message)