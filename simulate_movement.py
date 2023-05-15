import requests
import time
from base64 import b64encode

BASE_URL = "http://localhost:8080"
DITTO_USERNAME = "ditto"
DITTO_PASSWORD = "ditto"

def get_basic_auth_string(username, password):
    return b64encode(f"{username}:{password}".encode()).decode()

def update_thing(thing_id, path, value, headers):
    url = f"{BASE_URL}/api/2/things/{thing_id}/attributes/{path}"
    response = requests.put(url, headers=headers, json=value)
    print(f"Response status code for {thing_id} {path} update: {response.status_code}")

def simulate_movement(thing_id, headers):
    locations = ["Factory", "Warehouse1", "Ontheway1", "Warehouse2", "Ontheway2", "Customer"]
    statuses = ["In Factory", "In Warehouse 1", "On the Way to Warehouse 2", "In Warehouse 2", "On the Way to Customer", "Delivered"]
    while True:  # Boucle infinie pour la simulation continue
        for location, status in zip(locations, statuses):
            update_thing(thing_id, "location", location, headers)
            update_thing(thing_id, "status", status, headers)
            time.sleep(5)  # Pause de 5 secondes pour simuler le temps pris pour le déplacement


def main():
    auth_string = get_basic_auth_string(DITTO_USERNAME, DITTO_PASSWORD)
    headers = {
        "Authorization": f"Basic {auth_string}",
        "Content-Type": "application/json"
    }

    simulate_movement("org.example:package1", headers)

if __name__ == "__main__":
    main()

