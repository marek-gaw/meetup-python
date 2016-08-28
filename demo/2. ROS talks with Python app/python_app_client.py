# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:40:18 2016

@author: http://stackoverflow.com/questions/29145442/threaded-non-blocking-websocket-client-in-python
"""

import websocket
import threading
from time import sleep

def on_message(ws, message):
    print message

def on_close(ws):
    print "### closed ###"

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9090", on_message = on_message, on_close = on_close)
    wst = threading.Thread(target=ws.run_forever)
    wst.daemon = True
    wst.start()

    conn_timeout = 5
    while not ws.sock.connected and conn_timeout:
        sleep(1)
        conn_timeout -= 1
        print "##### subscribing to /chatter"
        json_string='{ "op": "subscribe", "topic":"/listener", "type":"std_msgs/String" }'
        ws.send(json_string)	
        
        
    while ws.sock.connected:
#        ws.send('Hello world %d'%msg_counter)
        print "still alive."
        sleep(1)
