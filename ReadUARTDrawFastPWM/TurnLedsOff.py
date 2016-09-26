import serial
import time

def TurnLEDsOff() :
	ser.write('start'.encode())
	for x in range(0, 1536) :
		ser.write("\x00")
	return


print 'Begin Main Code'
print 'Connecting to Serial'
ser = serial.Serial('/dev/cu.usbmodem2115241', 9600)
print 'Done Connecting'
TurnLEDsOff()
print 'Done'