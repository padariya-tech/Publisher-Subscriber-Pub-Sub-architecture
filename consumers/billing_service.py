from utils.kafka_config import get_consumer

consumer = get_consumer("payments", "billing-group")

for msg in consumer:
    print("[BILLING]", msg.value)