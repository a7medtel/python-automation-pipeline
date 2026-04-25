import os
import json
from config import OUTPUT_FOLDER

SNAPSHOT_FILE = os.path.join(OUTPUT_FOLDER, "snapshot.json")

def has_new_data(current_count):

    if not os.path.exists(SNAPSHOT_FILE):
        save_snapshot(current_count)
        return True

    with open(SNAPSHOT_FILE, "r") as f:
        snapshot = json.load(f)

    last_count = snapshot.get("user_count", 0)

    if current_count != last_count:
        save_snapshot(current_count)
        return True

    return False

def save_snapshot(count):
    with open(SNAPSHOT_FILE, "w") as f:
        json.dump({"user_count": count}, f)