import time
import datetime
from Adafruit_15Segment import FifteenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = FifteenSegment()

print "Press CTRL+Z to exit"

segment.writeChar(0, "T")
segment.writeChar(1, "I")
segment.writeChar(2, "M")
segment.writeChar(3, "E")
time.sleep(1)

segment.writeChar(0, "C")
segment.writeChar(1, "L")
segment.writeChar(2, "C")
segment.writeChar(3, "K")
time.sleep(1)

segment.writeChar(0, "T")
segment.writeChar(1, "E")
segment.writeChar(2, "S")
segment.writeChar(3, "T")
time.sleep(1)

# Continually update the time on a 4 char, 15-segment display
while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  # Set hours
  segment.writeDigit(0, int(hour / 10))     # Tens
  segment.writeDigit(1, hour % 10)          # Ones
  # Set minutes
  segment.writeDigit(2, int(minute / 10))   # Tens
  segment.writeDigit(3, minute % 10)        # Ones
  # Toggle colon
  # segment.setColon(second % 2)              # Toggle colon at 1Hz
  # Wait one second
  time.sleep(1)