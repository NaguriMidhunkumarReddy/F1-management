import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (only if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate("/Users/Annesha/fastapi-f1-management/app/firebase_config.json")  # Ensure correct path
    firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()

# Function to add a driver to Firestore
def add_driver(driver_data):
    """
    Adds a new driver to the Firestore database.
    :param driver_data: Dictionary containing driver details.
    """
    try:
        drivers_ref = db.collection("drivers")
        drivers_ref.add(driver_data)  # Firestore auto-generates an ID
        print("Driver added successfully!")
    except Exception as e:
        print("Error adding driver:", e)

# Function to retrieve all drivers
def get_all_drivers():
    """
    Retrieves all drivers from Firestore.
    :return: List of driver dictionaries.
    """
    try:
        drivers_ref = db.collection("drivers").stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in drivers_ref]
    except Exception as e:
        print("Error retrieving drivers:", e)
        return []

import firebase_admin
from firebase_admin import firestore

# Ensure Firebase is initialized
if not firebase_admin._apps:
    from firebase_admin import credentials
    cred = credentials.Certificate("app/firebase_config.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Add a new team
def add_team(team_data):
    try:
        teams_ref = db.collection("teams")
        teams_ref.add(team_data)
        return True
    except Exception as e:
        print(f"Error adding team: {e}")
        return False

# Get all teams
def get_all_teams():
    try:
        teams_ref = db.collection("teams").stream()
        return [team.to_dict() for team in teams_ref]
    except Exception as e:
        print(f"Error fetching teams: {e}")
        return []
