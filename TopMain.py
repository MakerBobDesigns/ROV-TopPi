from functools import partial

# use fast C version if available
try:
    import cPickle as pickle
except ImportError:
    import pickle

# easy access to load(s)
load = pickle.load
loads = pickle.loads

# easy access to dump(s) AND
# use the modern binary format
dump = partial(pickle.dump, protocol=pickle.HIGHEST_PROTOCOL)
dumps = partial(pickle.dumps, protocol=pickle.HIGHEST_PROTOCOL)

from ROVClient import transmit
from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop():
	if (event.type == ecodes.EV_KEY) or (event.type == ecodes.EV_ABS):
		keyevent = categorize(event)
		data = str(keyevent.event.code)+" "+str( keyevent.event.value)
		#data = dumps(data)
		print "code=" + str(keyevent.event.code), "value=" + str( keyevent.event.value)
		reply = transmit(data)
		print reply
