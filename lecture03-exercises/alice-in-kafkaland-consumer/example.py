from hdfs import InsecureClient
from kafka import KafkaConsumer

client = InsecureClient('http://namenode:9870', user='root')

# Create a KafkaConsumer that consumes messages from the topic 'alice-in-kafkaland'
consumer = KafkaConsumer('alice', bootstrap_servers=['kafka:9092'], group_id='group1')

full_msg = ''
# Combine all the messages into a single string
for msg in consumer:
    str = msg.value.decode()
    full_msg = full_msg + str

print(full_msg)

with client.write('/alice-in-kafkaland.txt', encoding='utf-8', overwrite=True) as writer:
    writer.write(full_msg)
    writer.write('\n')

    # Write the string to HDFS in a file called 'alice-in-kafkaland.txt'

