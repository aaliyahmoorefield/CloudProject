import json
from google.cloud import pubsub_v1

# Configuration
project_id = "your-project-id"
topic_id = "parking-updates"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def report_parking_event(spot_id, is_occupied):
    """Simulates a sensor detecting a car."""
    data = {
        "spot_id": spot_id,
        "status": "occupied" if is_occupied else "available",
        "timestamp": "2026-05-01T10:52:00Z"
    }
    
    # Data must be localized to bytes for Pub/Sub
    message_bytes = json.dumps(data).encode("utf-8")
    
    future = publisher.publish(topic_path, message_bytes)
    print(f"Published message ID: {future.result()}")

# Example: Car pulls into spot A-101
report_parking_event("A-101", True)
