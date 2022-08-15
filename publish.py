from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("device1")

myMQTTClient.configureEndpoint("a2hvoauz56nf89-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./private.pem.key", "./certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

msg = "Sample data from the device";
topic = "general/inbound"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")