import pika
import time


def send_test_order():
    conn = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = conn.channel()

    channel.queue_declare(queue="orders")

    test_order = {
        "order_id": 999999999,
        "order_time": time.time(),
        "product_title": "Test product",
        "product_description": "Just a test product.",
        "amount": 1,
        "manufacturer_id": 999,
        "customer_id": 998,
    }

    channel.basic_publish(
        exchange="",
        routing_key="orders",
        body=str(test_order),
    )

    return test_order
