from utils.kafka_config import get_producer
import time

producer = get_producer()

for i in range(10):
    msg ={"order_id":i,"amount":100+i}
    producer.send("orders",msg)
    print("Order Sent:",msg)
    time.sleep(1)