import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (only if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate("/Users/Annesha/fastapi-f1-management/app/firebase_config.json")  # Ensure correct path
    firebase_admin.initialize_app(cred)

# Now create Firestore client
db = firestore.client()

try:
    doc_ref = db.collection("test_collection").document("test_doc")
    doc_ref.set({"message": "Firestore is working!"})
    print("✅ Firestore test successful!")
except Exception as e:
    print(f"❌ Firestore test failed: {e}")
