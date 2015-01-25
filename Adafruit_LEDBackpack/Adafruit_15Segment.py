#!/usr/bin/python

import time
import datetime
from Adafruit_LEDBackpack import LEDBackpack

# ===========================================================================
# 15-Segment Display
# ===========================================================================

# This class is meant to be used with the four-character, fifteen segment
# displays available from Adafruit

class FifteenSegment:
  disp = None
  digits = [
    0x0C3F, # 0
    0x0006, # 1
    0x00DB, # 2
    0x00CF, # 3
    0x00E6, # 4
    0x00ED, # 5
    0x00FD, # 6
    0x0007, # 7
    0x00FF, # 8
    0x00E7, # 9
    0x00F7, # A
    0x00FC, # B
    0x0039, # C
    0x00DE, # D
    0x0079, # E
    0x0071, # F
  ]

  ascii = [
    0x0000, # <SPACE> 
    0x5200, # !
    0x0220, # "
    0x0000, # #
    0x3309, # $
    0x0000, # %
    0x0000, # &
    0x0000, # '
    0x0000, # (
    0x0000, # )
    0x3FC0, # *
    0x12C0, # +
    0x0000, # ,
    0x00C0, # -
    0x4000, # .
    0x0C00, # /
    0x0C3F, # 0
    0x0006, # 1
    0x00DB, # 2
    0x00CF, # 3
    0x00E6, # 4
    0x00ED, # 5
    0x00FD, # 6
    0x0007, # 7
    0x00FF, # 8
    0x00E7, # 9
    0x0000, # :
    0x0000, # ;
    0x2400, # <
    0x00C8, # =
    0x0900, # >
    0x1083, # ?
    0x0000, # @
    0x00F7, # A
    0x00FC, # B
    0x0039, # C
    0x00DE, # D
    0x0079, # E
    0x0071, # F
    0x00BD, # G
    0x00F6, # H
    0x1209, # I
    0x001E, # J
    0x2470, # K
    0x0038, # L
    0x0536, # M
    0x2136, # N
    0x003F, # O
    0x00F3, # P
    0x203F, # Q
    0x20F3, # R
    0x2109, # S
    0x1201, # T
    0x003E, # U
    0x0C30, # V
    0x2836, # W
    0x2D00, # X
    0x1500, # Y
    0x0C09, # Z
    0x0039, # [
    0x000F, # ]
    0x0000, # ^
    0x0008, # _
    0x0000, # `
    0x00F7, # a
    0x00FC, # b
    0x0039, # c
    0x00DE, # d
    0x0079, # e
    0x0071, # f
    0x00BD, # g
    0x00F6, # h
    0x1209, # i
    0x001E, # j
    0x2470, # k
    0x0038, # l
    0x0536, # m
    0x2136, # n
    0x003F, # o
    0x00F3, # p
    0x203F, # q
    0x20F3, # r
    0x2109, # s
    0x1201, # t
    0x003E, # u
    0x0C30, # v
    0x2836, # w
    0x2D00, # x
    0x1500, # y
    0x0C09, # z
    0x0000, # {
    0x1200, # |
    0x0000, # }
    0x0000, # ~
    ]

  # Constructor
  def __init__(self, address=0x70, debug=False):
    if (debug):
      print "Initializing a new instance of LEDBackpack at 0x%02X" % address
    self.disp = LEDBackpack(address=address, debug=debug)

  def writeDigitRaw(self, charNumber, value):
    "Sets a digit using the raw 16-bit value"
    if (charNumber > 7):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, value)

  def writeChar(self, charNumber, character, dot=False):
    "Sets a single alphanumeric character"
    if (charNumber > 7):
      return
    if ((ord(character) < 0x20) or (ord(character) > 0x7E)):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, self.ascii[ord(character) - 0x20] | (dot << 7))

  def writeDigit(self, charNumber, value, dot=False):
    "Sets a single alphanumeric character"
    if (charNumber > 7):
      return
    if ((value < 0x0) or (value > 0xF)):
      return
    # Set the appropriate digit
    self.disp.setBufferRow(charNumber, self.digits[value] | (dot << 7))

