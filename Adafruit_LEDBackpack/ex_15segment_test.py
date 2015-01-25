import time
import random
from Adafruit_LEDBackpack import LEDBackpack
seg = LEDBackpack(address=0x70, debug=False)
while(True):
	for i in range(4):
		seg.setBufferRow(i, 0xFFFF)
	time.sleep(2)
	for i in range(4):
		seg.setBufferRow(i, 0x0000)
	time.sleep(1)
