import serial

# Global Variables
# Mode == 1 : Attract Mode
# Mode == 2 : Sound Reactive Mode
# Mode == 3 : Simon
mode = 2
frame = 0
SimulationMode = 1

def RunAttractMode() :
	print 'Attract'
	print frame
	return

def RunSoundReactiveMode(soundLevel) :
	print 'Sound React'
	print soundLevel
	return

def RunSimonMode() :
	print 'Simon'
	return

def ReadCircuitPlayGround():
	if SimulationMode == 0 :
		myStr = ReadCircuitPlayGround()
	else :
		myStr = '0.54	0.05	9.75	28.61	1	0	0	128	340	4	8	2	4	4	3	4	3'
	return myStr

def RunCircuitPlayGroundCode():
	circuitPlaygroundLine = ReadCircuitPlayGround()
	print circuitPlaygroundLine

	myList = circuitPlaygroundLine.split('	')
	cpX = float(myList[0])
	cpY = float(myList[1])
	cpZ = float(myList[2])
	cpTemp = float(myList[3])
	cpSlideSwitch = int(myList[4])
	cpL_Button = int(myList[5])
	cpR_Button = int(myList[6])
	cpLight = int(myList[7])
	cpSound = int(myList[8])
	cpCap2 = int(myList[9])
	cpCap3 = int(myList[10])
	cpCap0 = int(myList[11])
	cpCap1 = int(myList[12])
	cpCap9 = int(myList[13])
	cpCap10 = int(myList[14])
	cpCap6 = int(myList[15])
	cpCap12 = int(myList[16])

	global frame
	frame = frame + 1

	if mode == 1:
		RunAttractMode()
	elif mode == 2:
		RunSoundReactiveMode(cpSound)
	elif mode == 3:
		RunSimonMode()

	return


print 'Begin Main Code'
print 'Connecting to Serial Port'
if SimulationMode == 0 :
	ser = serial.Serial('/dev/tty.usbserial-00001014', 9600)
print 'Done Connecting'

while 1 :
	RunCircuitPlayGroundCode()

print 'Done'

