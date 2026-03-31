from utils.kafka_config import get_consumer

consumer = get_consumer("orders", "notification-group")

for msg in consumer:
    data = msg.value
    print("[NOTIFICATION] Sending email for:", data)