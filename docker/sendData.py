import paho.mqtt.client as mqtt

class SendDataViaMQTT(object):

    def __init__(self,MQTTConnector, fragment = 'c8yTestFragment', series, value, unit):
        self.MQTTConnector = MQTTConnector
        self.fragment = fragment
        self.series = series
        self.value = value
        self.unit = unit

    def publish(self):
        self.MQTTConnector.client.publish(self.MQTTConnector.baseTopic, "200",self.fragment,self.seris,self.value,self.unit)

class MQTTConnector(object):

    def __init__(self, mqtt_host,mqtt_port = 1883, user, password, clientID, tenantID):
        self.mqttHost = mqttHost
        self.tenantID = tenantID
        self.clientID = clientID
        self.__user = user
        self.__password = password
        self.baseTopic = 's/us/'

    def connect(self):
        self.client = mqtt.Client(client_id=self.clientID)
        self.client.username_pw_set(self.tenantID+'/'+ self.__user, self.__password)
        self.client.connect(self.mqttHost, self.mqttPort)
