# Installation
# $pip3 install libsvm-official
# If you ran into error such as (ERROR: Could not build wheels for scipy which use PEP 517 and cannot be installed directly)
# Try update pip
# $pip3 install --upgrade pip
# https://stackoverflow.com/questions/61365790/error-could-not-build-wheels-for-scipy-which-use-pep-517-and-cannot-be-installe
from libsvm.svmutil import *
import wiotp.sdk.application
import time

client_id = "1"
MQTT_TOPICS = ["Door"]
"""
# Read data in LIBSVM format. Replace 'combine_open_close.txt' with your training dataset.
y, x = svm_read_problem('combine_open_close.txt')
# Generate model
m = svm_train(y, x)
# Save trained model
svm_save_model('trained.model', m)
"""

# Load model
trained_model = svm_load_model('trained.model')

# label
y_2 = [-1]
"""
# vector
x_2 = [{1: 3.5267175572519083, 2: 0.20610687022900764, 3: -0.3893129770992366, 4: 1.05419921875, 5: -0.01123046875, 6: 0.13134765625}]
"""

def publish(topic, payload):
    print(f"Send to topic `{topic}`:    {payload}")

def connect_ibm():
    options = wiotp.sdk.application.parseConfigFile("application.yaml")
    client = wiotp.sdk.application.ApplicationClient(config=options)
    client.connect()
    return(client)

# label [+1] or [-1]
# vector [{1: 3.5267175572519083, 2: 0.20610687022900764, 3: -0.3893129770992366, 4: 1.05419921875, 5: -0.01123046875, 6: 0.13134765625}]
def run_prediction(label, vector, model, client, lastDecision):
    client_id = "1"
    MQTT_TOPICS = ["Door"]
    n = 0
    p_labs, p_acc, p_vals = svm_predict(label, vector, model)
    # print(f"p_labs: {p_labs}")
    decision = 'Open' if p_labs == [1.0] else 'Close'
    """
    options = wiotp.sdk.application.parseConfigFile("application.yaml")
    client = wiotp.sdk.application.ApplicationClient(config=options)
    client.connect()
    """
    payload = decision
    eventData = {'Door' : payload}
    if lastDecision != decision:
        client.publishEvent(typeId="RaspberryPi", deviceId=client_id, eventId=MQTT_TOPICS[n], msgFormat="json", data=eventData, qos = 2, onPublish=publish(topic = MQTT_TOPICS[n], payload = payload))
        print(f"Decision: {decision}")
    time.sleep(1)
    return(decision)
"""
if __name__ == "__main__":
    run_prediction(y_2, x_2, trained_model)
"""