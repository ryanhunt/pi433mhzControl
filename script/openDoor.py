#!/usr/bin/python

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

if GPIO.input(18):
        print "Already on, quitting."
else:
        print "Turning on..."
        GPIO.output(18,GPIO.HIGH)

# This resets all pins
#GPIO.cleanup()
