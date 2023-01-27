from kafka import KafkaProducer


while True:
    # input
    string = str(input())

    producer = KafkaProducer(bootstrap_servers='kafka:9092')

    byt = bytes(string, 'utf-8')

    future = producer.send('newmsg', byt)
    result = future.get(timeout=60)

    # output
    print(string)
