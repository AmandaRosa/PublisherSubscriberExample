import paho.mqtt.client as mqtt
import time
import random

# Define the broker address
broker_address = "localhost"  # Replace with the actual broker address

# Define the topics
topics = ["test/topic1", "test/topic2", "test/topic3"]

# Create a list of numbers from 0 to 10
numbers = list(range(11))

# Create a new MQTT client instance
client = mqtt.Client(client_id="Publisher")

# Connect to the broker
client.connect(broker_address)

# Publish data to the topics
while True:
    # Select a random number and a random topic
    message = str(random.choice(numbers))
    topic = random.choice(topics)
    client.publish(topic, message)
    print(f"Published '{message}' to topic '{topic}'")
    time.sleep(5)  # Wait for 5 seconds before publishing again
