# API → Data → CSV → AI → Email
import requests
import pandas as pd
import os
from config import OUTPUT_FOLDER

def fetch_users():
    url = "https://dummyjson.com/users?limit=160"

    response = requests.get(url)
    data = response.json()

    users = []

    for user in data["users"]:
        users.append({
            "name": f"{user['firstName']} {user['lastName']}",  # DummyJSON ما فيه name جاهز
            "email": user["email"],
            "city": user["address"]["city"]
        })

    df = pd.DataFrame(users)

    output_path = os.path.join(OUTPUT_FOLDER, "users.csv")
    df.to_csv(output_path, index=False)

    print(f"Fetched {len(df)} users")
    return len(df)