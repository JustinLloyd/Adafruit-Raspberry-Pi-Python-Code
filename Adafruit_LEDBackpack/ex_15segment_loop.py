import time
import random
from Adafruit_LEDBackpack import LEDBackpack
seg = LEDBackpack(address=0x70, debug=False)

anim = [
[[ 3, 0x0001 ]], [[ 3, 0x0002 ]], [[ 3, 0x0004 ]], [[ 3, 0x0008 ]], [[ 2, 0x0008 ]], [[ 1, 0x0008 ]],
[[ 0, 0x0008 ]], [[ 0, 0x0010 ]], [[ 0, 0x0020 ]], [[ 0, 0x0001 ]], [[ 1, 0x0001 ]], [[ 2, 0x0001 ]],
[[ 3, 0x0002 ]], [[ 3, 0x0080 ]], [[ 3, 0x0040 ]], [[ 2, 0x0080 ]], [[ 2, 0x0040 ]], [[ 1, 0x0080 ]], 
[[ 1, 0x0040 ]], [[ 0, 0x0080 ]], [[ 0, 0x0040 ]], [[ 0, 0x0020 ]], [[ 0, 0x0100 ]], [[ 0, 0x2000 ]], 
[[ 0, 0x4000 ]], [[ 1, 0x0800 ]], [[ 1, 0x0400 ]], [[ 2, 0x0100 ]], [[ 2, 0x2000 ]], [[ 2, 0x4000 ]], 
[[ 3, 0x0800 ]], [[ 3, 0x0400 ]], [[ 3, 0x0002 ]], [[ 3, 0x0004 ]], [[ 3, 0x4000 ]], [[ 3, 0x2000 ]], 
[[ 3, 0x0100 ]], [[ 2, 0x0400 ]], [[ 2, 0x0800 ]], [[ 1, 0x4000 ]], [[ 1, 0x2000 ]], [[ 1, 0x0100 ]], 
[[ 0, 0x0400 ]], [[ 0, 0x0800 ]], [[ 0, 0x0010 ]], [[ 0, 0x0040 ]], [[ 0, 0x0080 ]], [[ 1, 0x0040 ]], 
[[ 1, 0x0080 ]], 

[[ 1, 0x0006 ], [ 2, 0x0030 ] ], [[ 1, 0x1200 ], [ 2, 0x1200 ] ], [[ 1, 0x0030 ], [ 2, 0x0006 ] ], 
[[ 0, 0x0006 ], [ 3, 0x0030 ] ], [[ 0, 0x1200 ], [ 3, 0x1200 ] ], [[ 0, 0x0030 ], [ 3, 0x0006 ] ], 

[[ 0, 0x0001 ], [ 3, 0x0008 ] ], [[ 1, 0x0001 ], [ 2, 0x0008 ] ], [[ 1, 0x0008 ], [ 2, 0x0001 ] ], 
[[ 0, 0x0008 ], [ 3, 0x0001 ] ], [[ 0, 0x0010 ], [ 3, 0x0002 ] ], [[ 0, 0x0020 ], [ 3, 0x0004 ] ],

[[ 0, 0x0100 ], [ 3, 0x2000 ] ], [[ 0, 0x2000 ], [ 3, 0x0100 ] ], [[ 1, 0x0800 ], [ 2, 0x0400 ] ],
[[ 1, 0x0400 ], [ 2, 0x0800 ] ], [[ 1, 0x0002 ], [ 2, 0x0020 ] ],

[[ 1, 0x3FC0 ], [ 2, 0x3FC0 ] ], [[ 1, 0x3FC0 ], [ 2, 0x3FC0 ], [ 0, 0x3FC0 ], [ 3, 0x3FC0 ] ],
[[ 0, 0x3FC0 ], [ 3, 0x3FC0 ] ],
]

while(True):
	for sequence in anim:
		for bit in sequence:
			seg.setBufferRow(bit[0], bit[1])
		time.sleep(0.1)
		for bit in sequence:
			seg.setBufferRow(bit[0], 0)
	time.sleep(1)
