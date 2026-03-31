# Kafka Pub/Sub System (Production-style)

## Overview

This project simulates a real-world event-driven architecture using Kafka (Redpanda).

### Components:

* 3 Producers (orders, payments, users)
* 5 Consumers (notification, analytics, fraud, logging, billing)
* Kafka-compatible broker (Redpanda)

---

## Architecture

Producers → Topics → Consumer Groups

Each consumer group receives all messages independently.

---

## Setup

### 1. Start Kafka (Redpanda)

```bash
docker compose up -d
```

### 2. Create Topics

```bash
bash topics/create_topics.sh
```

---

## Run Producers

```bash
python producers/order_producer.py
python producers/payment_producer.py
python producers/user_producer.py
```

---

## Run Consumers

```bash
python consumers/notification_service.py
python consumers/analytics_service.py
python consumers/fraud_service.py
python consumers/logging_service.py
python consumers/billing_service.py
```

---

## Key Concepts

* **Consumer Groups** → isolation between services
* **Partitions** → scaling within a service
* **Offsets** → tracking progress
* **Replay** → reprocessing data

---

## Production Concepts Covered

* Event-driven architecture
* Decoupled services
* Parallel processing
* Fault tolerance
* Data replay

---

## Future Improvements

* Add FastAPI for APIs
* Add database storage
* Add monitoring (Prometheus/Grafana)
* Add schema validation (Avro)

---
