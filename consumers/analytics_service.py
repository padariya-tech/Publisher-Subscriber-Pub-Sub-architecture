from utils.kafka_config import get_consumer

consumer = get_consumer("orders", "analytics-group")

for msg in consumer:
    data = msg.value
    print("[ANALYTICS] Processing:", data)