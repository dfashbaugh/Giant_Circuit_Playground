import serial
import time

class CircuitPlayGround:

	ser = serial.Serial()

	X = 0
	Y = 0
	Z = 0
	Temp = 0
	SlideSwitch = 0
	L_Button = 0
	R_Button = 0
	Light = 0
	Sound = 0
	Cap2 = 0
	Cap3 = 0
	Cap0 = 0
	Cap1 = 0
	Cap9 = 0
	Cap10 = 0
	Cap6 = 0
	Cap12 = 0

	def __init__(self, SerialPort):
		self.ser.baudrate = 9600
		self.ser.port = SerialPort
		self.ser.open()
		self.ser.timeout = 1
		print 'Initialized CircuitPlayGround Serial Port'
 
	def Read(self):
		theString = self.ser.readline()
		myList = theString.split('	')
		if len(myList) == 17 :
			self.X = float(myList[0])
			self.Y = float(myList[1])
			self.Z = float(myList[2])
			self.Temp = float(myList[3])
			self.SlideSwitch = int(myList[4])
			self.L_Button = int(myList[5])
			self.R_Button = int(myList[6])
			self.Light = int(myList[7])
			self.Sound = int(myList[8])
			self.Cap2 = int(myList[9])
			self.Cap3 = int(myList[10])
			self.Cap0 = int(myList[11])
			self.Cap1 = int(myList[12])
			self.Cap9 = int(myList[13])
			self.Cap10 = int(myList[14])
			self.Cap6 = int(myList[15])
			self.Cap12 = int(myList[16])
		return theString
