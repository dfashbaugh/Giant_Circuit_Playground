import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround

circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
neoMatrix = NeoPixelMatrix('/dev/cu.usbmodem2115241')
neoMatrix.SetAllRed(255)

circuitPlayground.Read()

while 1:
	neoMatrix.DrawLEDMemory()
	circuitPlayground.Read()
	#print circuitPlayground.Light
	neoMatrix.SetAllRed(circuitPlayground.Light)