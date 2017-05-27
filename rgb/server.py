import time
import RPi.GPIO as GPIO
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

# LED pin mapping.
red = 11
green = 12
blue = 13

# GPIO setup.
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Set up colours using PWM so we can control individual brightness.
RED = GPIO.PWM(red, 100)
GREEN = GPIO.PWM(green, 100)
BLUE = GPIO.PWM(blue, 100)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'

def setColour(rgb = []):
    # Convert 0-255 range to 0-100.
    rgb = [(x / 255.0) * 100 for x in rgb]
    RED.ChangeDutyCycle(rgb[0])
    GREEN.ChangeDutyCycle(rgb[1])
    BLUE.ChangeDutyCycle(rgb[2])

#Function for handling connections. This will be used to create threads
def clientthread(conn):
         
    #Receiving from client
    data = conn.recv(1024)
    print 'Setting led to rgb:'
    print data.rstrip('\n\r').split(' ')
    setColour(map(int, data.rstrip('\n\r').split(' ')))
    conn.close()
     
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()

