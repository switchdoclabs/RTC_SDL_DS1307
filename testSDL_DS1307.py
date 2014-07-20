#!/usr/bin/env python
#
# Test SDL_DS1307
# John C. Shovic, SwitchDoc Labs
# 07/10/2014
#
# Evaluation of the following RTC Clocks
#
#	DS1307
#	MCP79400
#	DS3231 
# 	PCF8563 
#

# imports

import sys
import time
import datetime

import SDL_DS1307

# Main Program

print ""
print "Test SDL_DS1307 Version 1.0 - SwitchDoc Labs"
print ""
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
ds1307.write_now()

# Main Loop - sleeps 10 minutes, then reads and prints values of all clocks


while True:

	currenttime = datetime.datetime.utcnow()

	deltatime = currenttime - starttime
 
	print ""
	print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
	
	print "DS1307=\t\t%s" % ds1307.read_datetime()

	time.sleep(10.0)
