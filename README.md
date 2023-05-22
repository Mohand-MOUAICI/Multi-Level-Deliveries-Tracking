# Package Tracking System
# Introduction
This system is designed to simulate and track the movement of a package through various stages from the factory to the customer. It is composed of three Python scripts and a web frontend.

# Components
Python Scripts
simulate_movement.py :
This script uses the requests library to simulate package movement by periodically updating the location and status of a package in the Eclipse Ditto system. The package moves through the following locations: Factory, Warehouse 1, On the way to Warehouse 2, Warehouse 2, On the way to the customer, and finally to the customer.

colis_entrepot_livreur.py :
This script uses the requests library to create or update "things" in the Eclipse Ditto system, such as packages, warehouses, and delivery people. It sets up initial data for a package, two warehouses, and a delivery person.

Web Frontend
app.py :
This script sets up a Flask web server that serves the frontend and provides an API for fetching the current status of a package.

index.html :
The frontend is a simple HTML page that allows the user to enter a package ID and see the current status of that package. It updates the status every second to give a real-time tracking experience.

# Setup and Running
Ensure that you have Python and Flask installed, and that the Eclipse Ditto system is running and accessible.

Run colis_entrepot_livreur.py to set up the initial data.

Then start the package movement simulation.
python colis_entrepot_livreur.py


Finally, start the Flask server.
python simulate_movement.py


Now you can open your browser and go to localhost:5000 to track the package.
python app.py
"# Multi-Level-Deliveries-Tracking" 
