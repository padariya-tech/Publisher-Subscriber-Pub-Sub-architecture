from utils.kafka_config import get_producer
import time

producer = get_producer()

for i in range(10):
    msg = {"user_id": i, "action": "signup"}
    producer.send("users", msg)
    print("User event:", msg)
    time.sleep(1)