#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop():
	if (event.type == ecodes.EV_KEY) or (event.type == ecodes.EV_ABS):
		keyevent = categorize(event)
		print "value=", keyevent.event.value
		print "code=", keyevent.event.code

