from kafka import KafkaConsumer
import sys

consumer = KafkaConsumer(
    "topic-test-1",
    bootstrap_servers='localhost:29092'
)

for msg in consumer:
    print("Topic Name=%s, Message=%s" %(msg.topic, msg.value))

sys.exit()