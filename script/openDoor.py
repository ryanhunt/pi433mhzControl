#!/usr/bin/python

tempFile = '/tmp/GarageDoor.status'
# 1 = opening
# 2 = opened
# 3 = closing
# 4 = closed


import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#open file
target = open(tempFile, 'w')
target.truncate()

if GPIO.input(18):
        print "Already on, closing..."
        target.write("3\n")
        GPIO.output(18,GPIO.LOW)
        target.write("4\n")
else:
        print "Turning on..."
        target.write("1\n")
        GPIO.output(18,GPIO.HIGH)
        target.truncate()
        target.write("2\n")
        
target.close()
        

# This resets all pins
#GPIO.cleanup()
