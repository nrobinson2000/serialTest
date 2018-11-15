#!/usr/bin/env python

from __future__ import print_function
import serial
import sys
import time

header = "waterRemaining, rawData, correctedData, creepData, lbs, voltage, stateOfCharge, timeStamp, temp, bottleCount, uptime, resetReason, disconnects, rssi, signalQuality, rippleVersion, particleVersion\n"

try:
    ser = serial.Serial(sys.argv[1])

except IndexError:
    print()
    print("Please provide a serial port!")
    print("Example: ")
    print(sys.argv[0] + " /dev/ttyACM0")
    print()

except serial.serialutil.SerialException:
    print("Could not open serial port: " + sys.argv[1])

else:
    filename = "readings-" + str(time.time()) +".csv"
    f = open(filename, "w")
    f.write(header)
    for i in range(0, 10):
        line = ser.readline()
        f.write(line)
        print(line, end='')
    ser.close()
    f.close()
