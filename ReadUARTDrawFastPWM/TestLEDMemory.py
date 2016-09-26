import serial
import time

LEDMemory = [int]*1536

def DrawLEDMemory() :
	ser.write('start'.encode())
	for x in range(0, len(LEDMemory)) :
		ser.write(chr(LEDMemory[x]))
	return

print 'Begin Main Code'
print 'Connecting to Serial'
ser = serial.Serial('/dev/cu.usbmodem2115241', 9600)
print 'Done Connecting'

lastTime = time.time()
lastMod = 0;

for x in range(0, len(LEDMemory)/2) :
	if x%3 == lastMod :
		LEDMemory[x] = 0x10
	else :
		LEDMemory[x] = 0x0
for x in range(len(LEDMemory)/2, len(LEDMemory)) :
	if x%3 == lastMod + 1 :
		LEDMemory[x] = 0x10
	else :
		LEDMemory[x] = 0x00

while 1:
	if time.time() - lastTime > 0.2 :
		lastTime = time.time()
		for x in range(0, len(LEDMemory)/2) :
			if x%3 == lastMod :
				LEDMemory[x] = 0x10
			else :
				LEDMemory[x] = 0x00

		for x in range(len(LEDMemory)/2, len(LEDMemory)) :
			if x%3 == lastMod + 1 :
				LEDMemory[x] = 0x10
			else :
				LEDMemory[x] = 0x00

		lastMod = (lastMod+1)%2

	DrawLEDMemory()

print 'Done'