#!/usr/bin/env python
import os
import json
import uuid

from confluent_kafka.avro import AvroProducer

from utils.load_avro_schema_from_file import load_avro_schema_from_file
# from utils.parse_command_line_args import parse_command_line_args


TRANSACTIONS_TOPIC = str(os.environ.get('TRANSACTIONS_TOPIC'))
KAFKA_BROKER_URL = str(os.environ.get('KAFKA_BROKER_URL'))
SCHEMA_REGISTRY_URL = str(os.environ.get('SCHEMA_REGISTRY_URL'))


def send_record(args):
    if args['record_value'] is None:
        raise AttributeError("--record-value is not provided.")

    if args['schema_file'] is None:
        raise AttributeError("--schema-file is not provided.")

    key_schema, value_schema = load_avro_schema_from_file(args['schema_file'])

    producer_config = {
        "bootstrap.servers": args['bootstrap_servers'],
        "schema.registry.url": args['schema_registry']
    }

    producer = AvroProducer(producer_config, default_key_schema=key_schema, default_value_schema=value_schema)

    for rec in args['record_value']:
        key = args['record_key'] if args['record_key'] else str(uuid.uuid4())
        value = json.loads(rec)
        try:
            producer.produce(topic=args['topic'], key=key, value=value)
        except Exception as e:
            print(f"Exception while producing record value - {value} to topic - {args['topic']}: {e}")
        else:
            print(f"Successfully producing record value - {value} to topic - {args['topic']}")

        producer.flush()


if __name__ == "__main__":
    
    args = {
        'topic': TRANSACTIONS_TOPIC,
        'bootstrap_servers': KAFKA_BROKER_URL,
        'schema_file': 'create-user-request.avsc',
        'schema_registry': SCHEMA_REGISTRY_URL,
        'record_key': None,
        'record_value': [
            '{"email": "email@email.com", "firstName": "Bob", "lastName": "Jones"}',
            '{"email": "email2@email.com", "firstName": "Jane", "lastName": "Smith"}'
            ]
    }

    send_record(args)
