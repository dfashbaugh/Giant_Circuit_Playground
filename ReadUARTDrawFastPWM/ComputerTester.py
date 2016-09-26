import serial
import time

def LightAllRed() :
	ser.write('start'.encode())
	for x in range(0, 1536) :
		if x % 3 == 1 :
			ser.write("\x22")
		else :
			ser.write("\x00")
	return

def LightAllBlue() :
	ser.write('start'.encode())
	for x in range(0, 1536) :
		if x % 3 == 2 :
			ser.write("\x22")
		else :
			ser.write("\x00")
	return

def LightAllGreen() :
	ser.write('start'.encode())
	for x in range(0, 1536) :
		if x % 3 == 0 :
			ser.write("\x22")
		else :
			ser.write("\x00")
	return

print 'Begin Main Code'
print 'Connecting to Serial'
ser = serial.Serial('/dev/cu.usbmodem2115241', 9600)
print 'Done Connecting'

while 1 :
	LightAllRed()
	time.sleep(0.2)
	LightAllBlue()
	time.sleep(0.2)
	LightAllGreen()
	time.sleep(0.2)

print 'Done'