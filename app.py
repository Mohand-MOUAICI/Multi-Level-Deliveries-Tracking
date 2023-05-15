from flask import Flask, render_template, jsonify, request
import requests
from base64 import b64encode

BASE_URL = "http://localhost:8080"
DITTO_USERNAME = "ditto"
DITTO_PASSWORD = "ditto"

app = Flask(__name__)

def get_basic_auth_string(username, password):
    return b64encode(f"{username}:{password}".encode()).decode()

def get_thing(thing_id):
    headers = {
        "Authorization": f"Basic {get_basic_auth_string(DITTO_USERNAME, DITTO_PASSWORD)}",
        "Content-Type": "application/json"
    }
    url = f"{BASE_URL}/api/2/things/{thing_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_package_status/<package_id>', methods=['GET'])
def get_package_status(package_id):
    package = get_thing(f"org.example:{package_id}")
    if "Ontheway" in package["attributes"]["location"]:
        package["attributes"]["sub_location"] = str(package["attributes"]["location"].count("Ontheway"))
    return jsonify(package)

if __name__ == '__main__':
    app.run(debug=True)
