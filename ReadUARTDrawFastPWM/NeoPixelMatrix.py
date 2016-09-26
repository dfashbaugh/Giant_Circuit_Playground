import serial
import time

class NeoPixelMatrix:

	MemorySize = 1536
	ser = serial.Serial()
	LEDMemory = [int]*MemorySize

	def __init__(self, SerialPort):
		self.ser.baudrate = 2000000
		self.ser.port = SerialPort
		self.ser.open()
		print 'Initialized Serial Port'
 
	def Clear(self) :
		for x in range(0, self.MemorySize) :
			self.LEDMemory[x] = 0
		return

	def SetAllRed(self, value) :
		for x in range(0, self.MemorySize) :
			if x%3 == 1 :
				self.LEDMemory[x] = value
			else :
				self.LEDMemory[x] = 0x00
	
	def SetImage(self, image, x, y):
		print "Set an image"

	def DrawLEDMemory(self) :
		self.ser.write('start'.encode())
		for x in range(0, len(self.LEDMemory)) :
			self.ser.write(chr(self.LEDMemory[x]))
		return