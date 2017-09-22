from ROVClient import transmit, setupSocket, sendReceive
from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')
from time import sleep

s = setupSocket()

while True:
	for event in gamepad.read_loop():
		if (event.type == ecodes.EV_KEY) or (event.type == ecodes.EV_ABS):
			keyevent = categorize(event)
			data = str(keyevent.event.code)+" "+str( keyevent.event.value)
			print "code=" + str(keyevent.event.code), "value=" + str( keyevent.event.value)
			reply = sendReceive(s, data)
			#reply = transmit(data)
			print reply
		print ('wtf')
