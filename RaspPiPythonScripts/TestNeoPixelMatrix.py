import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround

lastDrawTime = 0

circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
neoMatrix = NeoPixelMatrix('/dev/cu.usbmodem2115241')

while 1:
	if time.time() - lastDrawTime > 0.03 :
		neoMatrix.DrawLEDMemory()
		lastDrawTime = time.time()

	circuitPlayground.Read()
	neoMatrix.SetAllRed(circuitPlayground.Cap12/10)

	print circuitPlayground.Cap12/10