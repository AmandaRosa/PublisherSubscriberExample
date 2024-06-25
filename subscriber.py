import paho.mqtt.client as mqtt

# Define the broker address
broker_address = "localhost"  # Replace with the actual broker address

# Define the topics
topics = ["test/topic1", "test/topic2", "test/topic3"]

# Initialize a variable to keep the sum
total_sum = 0

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    global total_sum
    # Decode the incoming message and convert to an integer
    number = int(message.payload.decode())
    # Add the number to the total sum
    total_sum += number
    print(f"Received number '{number}' on topic '{message.topic}'")
    print(f"Current total sum: {total_sum}")

# Create a new MQTT client instance
client = mqtt.Client(client_id="Subscriber")

# Attach the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_address)

# Subscribe to the topics
for topic in topics:
    client.subscribe(topic)

# Start the MQTT client loop
client.loop_forever()
