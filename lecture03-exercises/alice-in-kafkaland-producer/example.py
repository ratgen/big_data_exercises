from hdfs import InsecureClient
from kafka import KafkaProducer

# Create an insecure client that can read from HDFS
client = InsecureClient('http://namenode:9870', user='root')

first_line = ''

producer = KafkaProducer(bootstrap_servers='kafka:9092')

# Read the alice in wonderland text file from HDFS
with client.read('/alice-in-wonderland.txt', encoding='utf-8', delimiter='\n') as reader:
    # Write each sentence in alice in wonderland
    # to a kafka topic with a KafkaProducer
    for line in reader:
        byt = bytes(line, 'utf-8')
        future = producer.send('alice', byt)
