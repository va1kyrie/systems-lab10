import serial
import paho.mqtt.client as mqtt
import string
import sys

import time
import datetime
import json
import binascii
import base64
import struct

# python script that counts to 10 by passing a value between the xDot and the pivot server

# there are two 'clients' - one is the xDot and one is the python script (via an MQTT client)

# global variables
network = "pivot.iuiot.org"


pl1 = "{\"data\":\""
pl2 = "\",\"deveui\":\"00-80-00-00-04-00-51-87\"}"


'''
def hexes(bstr):
    hx = []
    for b in bstr:
        hx.append(struct.unpack('!f', b.decode('hex'))[0])
    return hx

'''
#pivot client stuff
def on_message(client, userdata, msg):
    pl = ""
    # for s in msg.payload:
    #     pl += binascii.b2a_qp(s)
    # dj = json.dumps(pl)
    # js = json.load(dj)
    info = base64.b64decode(json.loads(msg.payload)['data'])
    strs = info.split('&');
    #print(strs)
    #print('info = ' + string(info))

    # need to convert the hex into floats
    # get 96 hex numbers: each set of 4 is a float number
    #also need to check the endianness

    dump = open("./light.txt",mode='a+')
    tm = time.ctime()
    dump.write('\n' + tm)
    for s in strs:
        dump.write('\n' + str(s))
    dump.close()

    #print('temp  = ' + str(t))
    #print('pressure = ' + str(p))
    #dump.close()


pivot = mqtt.Client()
pivot.on_message = on_message
pivot.connect(network)
pivot.subscribe("lora/00-80-00-00-04-00-51-87/up")
#pivot.loop_forever()

def test():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    print(ser.name)
    pivot.loop_start()
    while 1:
        print('testing...')
        time.sleep(2)
        ser.write('s')
    print('something is very wrong')

def measure():
    #ser = serial.Serial('/dev/ttyACM0', 115200)
    #print(ser.name)
    pivot.loop_start()
    hrs = 0
    while hrs < 49:
        print('measuring data')
        #time.sleep(3600)
    print('measuring finished')
    pivot.loop_stop()
