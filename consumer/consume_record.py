import os
from confluent_kafka.avro import AvroConsumer
# from utils.parse_command_line_args import parse_command_line_args

TRANSACTIONS_TOPIC = str(os.environ.get('TRANSACTIONS_TOPIC'))
KAFKA_BROKER_URL = str(os.environ.get('KAFKA_BROKER_URL'))
SCHEMA_REGISTRY_URL = str(os.environ.get('SCHEMA_REGISTRY_URL'))

def consume_record(args):
    default_group_name = "default-consumer-group"

    consumer_config = {"bootstrap.servers": args['bootstrap_servers'],
                       "schema.registry.url": args['schema_registry'],
                       "group.id": default_group_name,
                       "auto.offset.reset": "earliest"}

    consumer = AvroConsumer(consumer_config)

    consumer.subscribe([args['topic']])

    while True: 
        try:
            message = consumer.poll(5)
        except Exception as e:
            print(f"Exception while trying to poll messages - {e}")
        else:
            if message:
                print(f"Successfully poll a record from "
                      f"Kafka topic: {message.topic()}, partition: {message.partition()}, offset: {message.offset()}\n"
                      f"message key: {message.key()} || message value: {message.value()}")
                consumer.commit()
            else:
                print("No new messages at this point. Try again later.")

    consumer.close()


if __name__ == "__main__":

    args = {
        'topic': TRANSACTIONS_TOPIC,
        'bootstrap_servers': KAFKA_BROKER_URL,
        'schema_registry': SCHEMA_REGISTRY_URL
    }

    consume_record(args)
