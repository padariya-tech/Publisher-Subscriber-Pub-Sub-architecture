from utils.kafka_config import get_consumer

consumer = get_consumer("users", "logging-group")

for msg in consumer:
    print("[LOG]", msg.value)