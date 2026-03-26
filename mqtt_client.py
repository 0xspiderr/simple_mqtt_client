import paho.mqtt.client as mqtt
import json
import time

# variabile pentru stabilirea conexiunii
port: int = 1883
host: str = "localhost"
client_name: str = "test_client"

# variabile mqtt
topic_name: str = "test/test1"

# creearea obiectului de tip client MQTT
client = mqtt.Client(client_name)

# stabilirea conexiunii clientului la server/broker
client.connect(host, port)

# subscribe la un topic
client.subscribe(topic_name)

client.loop_start()
# publishing-ul unui dictionar JSON pe topicul "test/test1" catre broker/server
while True:
	mesaj_input: str = input("introduce un mesaj:")
	if mesaj_input in ["q", ""]:
		print("iesire din program cu succes")
		break
	timestamp: float = time.time()
	payload: dict = {"msg":mesaj_input, "timestamp":timestamp}

	# publicarea dictionarului sub format json catre broker-ul mqtt
	client.publish(topic_name, json.dumps(payload))
client.loop_stop()
