from utils.kafka_config import get_producer
import time

producer = get_producer()

for i in range(10):
    msg ={"payment_id":i,"status":"SUCCESS"}
    producer.send("payment",msg)
    print("Payment sent:",msg)
    time.sleep(1)