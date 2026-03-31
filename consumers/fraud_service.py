from utils.kafka_config import get_consumer

consumer = get_consumer("payments", "fraud-group")

for msg in consumer:
    data = msg.value
    print("[FRAUD CHECK]", data)