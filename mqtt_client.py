import paho.mqtt.client as mqtt

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

# publishing-ul unui string pe topicul "test/test1" catre broker/server
client.publish(topic_name, "hello world from mqtt_client.py")
