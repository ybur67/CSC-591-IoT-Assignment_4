from pydoc_data.topics import topics
import time
import json
import wiotp.sdk.application
from flask import Flask, render_template

app = Flask(__name__)

decision = ''

def DoorCallback(evt):
    global decision
    payload = json.dumps(evt.data).strip("{\" }").replace('"','').split(":")
    command = payload[1].lstrip(' ')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + command)
    decision += f"Decision: {command}\n"
    print(decision)

print('1')
options = wiotp.sdk.application.parseConfigFile("application.yaml")
print('2')
client = wiotp.sdk.application.ApplicationClient(config=options)
print('3')
client.connect()
print('4')
client.subscribeToDeviceEvents(eventId="Door")
print('5')
client.deviceEventCallback = DoorCallback
print('6')

@app.route("/")
def hello_world():
    print('>>>>>>>>>>>>>>>>>>>>>>>>')
    return render_template('index.html', decision=decision)
