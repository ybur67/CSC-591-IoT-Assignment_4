import time
from paho.mqtt import client as mqtt_client

ORG = "4rgdpj"
DEVICE_TYPE = "RaspberryPi"
TOKEN = "example_token"
DEVICE_ID = "b827eb8196c3"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
authMethod = "use-token-auth";
token = TOKEN;
client_id = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

MQTT_TOPICS = ["Door"]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def publish(client, topic, payload, qos = 2, retain = False):
    result = client.publish(topic, payload, qos, retain)
    status = result[0]
    if status == 0:
        print(f"Send to topic `{topic}`:    {payload}")
    else:
        print(f"Failed to send message to topic {topic}")

def run():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(authMethod, token)
    client.connect(server, 1883, 60)
    
    client.on_connect = on_connect
    for i in range(10000):
        if i % 2 == 0:
            payload =  "Open"
        else:
            payload = "Close"    
        publish(client, MQTT_TOPICS[0], payload, 2)
        time.sleep(3)
if __name__ == '__main__':
    run()