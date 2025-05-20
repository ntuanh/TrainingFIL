import pika

def send_message(msg: str):
    # Step 1: Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Step 2: Make sure the queue exists
    channel.queue_declare(queue='ntuanh')

    # Step 3: Send the message to the 'hello' queue
    channel.basic_publish(exchange='',
                          routing_key='ntuanh',
                          body=msg)

    print(f" [x] Sent '{msg}'")
    connection.close()

send_message("The new message 5st")