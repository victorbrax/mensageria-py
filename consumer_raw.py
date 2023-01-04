# pip install pika
import pika

def minha_callback(ch, method, properties, body): # Ação condicional
    print(body)
    print(type(body))


# Conexão
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Criação de canal
channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare( # Declaração de Queue
    queue="data_queue",
    durable=True
)

# Consumo
channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f'Listen RabbitMQ on port 5672')
channel.start_consuming()