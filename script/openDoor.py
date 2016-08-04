#!/usr/bin/python

tempFile = '/tmp/GarageDoor.opened'

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#open file
target = open(tempFile, 'w')
target.truncate()

if GPIO.input(18):
        print "Already on, quitting."
else:
        print "Turning on..."
        GPIO.output(18,GPIO.HIGH)
        target.write("1")
        target.close()
        

# This resets all pins
#GPIO.cleanup()
