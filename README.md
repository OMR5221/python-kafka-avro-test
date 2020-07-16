# python-avro-producer

For a tutorial on how this repository was built and how it works, go to this [article](https://medium.com/@billydharmawan/avro-producer-with-python-and-confluent-kafka-library-4a1a2ed91a24?source=friends_link&sk=b845dae5da1761d3a8c8f53d610eac33) (for Avro Producer part) and [this](https://medium.com/@billydharmawan/consume-messages-from-kafka-topic-using-python-and-avro-consumer-eda5aad64230?source=friends_link&sk=9d64b23845664a41710856270d81f36a) (for Avro Consumer part).

## Updated to move producer/consumer into separate docker-compose files:

- Step 1: Launch local Kakfa Cluster with Control Center and Schema Registry:

```bash
$ docker-compose -f docker-compose.kafka.yml up -d
```

- Step 2: Launch Producer to send Avro files to Kafka Topic create-user-request:

```bash
$ docker-compose -f docker-compose.producer.yml up -d
```

- Step 3: Launch Consumer to ingest messages produced to Topic create-user-request:

```bash
$ docker-compose -f docker-compose.consumer.yml up -d
```

## Teardown

Stop the containers:

```bash
$ docker-compose -f docker-compose.consumer.yml down
$ docker-compose -f docker-compose.producer.yml down
$ docker-compose -f docker-compose.kafka.yml down
```
