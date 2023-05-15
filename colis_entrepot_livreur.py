import requests
import json
from base64 import b64encode

BASE_URL = "http://localhost:8080"
DITTO_USERNAME = "ditto"
DITTO_PASSWORD = "ditto"

def get_basic_auth_string(username, password):
    return b64encode(f"{username}:{password}".encode()).decode()

def create_or_update_thing(thing_id, data, headers):
    url = f"{BASE_URL}/api/2/things/{thing_id}"
    response = requests.put(url, headers=headers, json=data)
    print(f"Response status code for {thing_id} creation: {response.status_code}")
    if response.content:
        print(f"Response content for {thing_id} creation: {json.loads(response.content)}")
    else:
        print("No content in response")

def main():
    auth_string = get_basic_auth_string(DITTO_USERNAME, DITTO_PASSWORD)
    headers = {
        "Authorization": f"Basic {auth_string}",
        "Content-Type": "application/json"
    }

    package_data = {"attributes": {"id": "package1", "status": "In Warehouse", "location": "Warehouse 1", "customer_id": "customer1"}}
    warehouse1_data = {"attributes": {"id": "warehouse1", "location": "Location 1", "packages": []}}
    warehouse2_data = {"attributes": {"id": "warehouse2", "location": "Location 2", "packages": []}}
    delivery_person_data = {"attributes": {"id": "delivery_person1", "current_location": "Location 1", "packages": []}}

    create_or_update_thing("org.example:package1", package_data, headers)
    create_or_update_thing("org.example:warehouse1", warehouse1_data, headers)
    create_or_update_thing("org.example:warehouse2", warehouse2_data, headers)
    create_or_update_thing("org.example:delivery_person1", delivery_person_data, headers)

if __name__ == "__main__":
    main()
