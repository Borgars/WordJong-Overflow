#!usr/bin/python

# This script is used to correct the CRC of WordJong DS (U) Saves

# Used for argv and exit
import sys

# Used for creating new file
from shutil import copy2

try:
    # Used for CRC Generation
    from pwn import *
except ImportError:
    print("Error importing pwntools - please make sure you have it installed")
    sys.exit(1)

# Used to convert hex to little-endian
from textwrap import wrap

# Used for dumping files as hex bytes
import binascii


# Function that calculates the CRC
def calculateCRC(data):
    # Convert string into bytes type
    message = bytes.fromhex(data)
    # Parameters used for CRC Formula
    poly = int("04C11DB7", 16)
    init = int("FFFFFFFF", 16)
    refin = True
    refout = True
    xor = int("00000000", 16)
    crc = pwnlib.util.crc.generic_crc(message, poly, 32, init, True, True, xor)
    return hex(crc)


# If invalid argument number
if len(sys.argv) != 3:
    print("Usage: python3 patch.py [INPUT FILE] [OUTPUT FILE]")
    print("NOTE: On some systems it may be 'python'" +
          " or 'py' in place of 'python3'")
    print("NOTE: Arguments must contain a fullstop/period")
    sys.exit(1)

try:
    f = open(sys.argv[1], "rb")
except FileNotFoundError:
    print("Couldn't find file:", sys.argv[1])
    sys.exit(1)

dump = binascii.hexlify(f.read())  # Dump as hex

oldCRC = str(dump)[2:10].upper()  # Current CRC
saveFile = str(dump)[10:-1]  # Save without CRC
print("FOUND OLD CRC:", oldCRC)
newCRC = calculateCRC(saveFile)[2:]  # Calculated CRC
# Pads CRC if there needs to be extra 0s
while len(newCRC) < 8:
    newCRC = "0" + newCRC
# Converting to little-endian
newCRC = wrap(newCRC, 2)
flippedCRC = ""
for i in range(len(newCRC)-1, -1, -1):
    flippedCRC += newCRC[i]
# Compares CRCs and creates new file if needed
newCRC = flippedCRC.upper()
if (oldCRC == newCRC):
    print("Input File already has a valid CRC, not creating a new file...")
else:
    print("CALCULATED CRC:", newCRC)
    copy2(sys.argv[1], sys.argv[2])
    f = open(sys.argv[2], "wb")
    f.write(bytes.fromhex(newCRC))
    f.write(bytes.fromhex(saveFile))
    f.close()
    print(sys.argv[2], "created")
sys.exit(0)
