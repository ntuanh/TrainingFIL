import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

def start_receiving(queue_name):
    # Step 1: Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Step 2: Make sure the queue exists
    channel.queue_declare(queue=queue_name)

    # Step 3: Tell RabbitMQ to call `callback` when a message is received
    channel.basic_consume(queue= queue_name,
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


start_receiving('ntuanh')