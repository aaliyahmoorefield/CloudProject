import base64
import json
from google.cloud import firestore

# Initialize Firestore Client
db = firestore.Client()

def process_parking_update(event, context):
    """Triggered by a message on a Cloud Pub/Sub topic."""
    
    # 1. Decode the Pub/Sub message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(pubsub_message)
    
    spot_id = data.get('spot_id')
    status = data.get('status')

    # 2. Update Firestore (The Real-time Database)
    doc_ref = db.collection('campus_lots').document(spot_id)
    doc_ref.set({
        'status': status,
        'last_updated': firestore.SERVER_TIMESTAMP
    }, merge=True)

    print(f"Updated spot {spot_id} to {status}.")
