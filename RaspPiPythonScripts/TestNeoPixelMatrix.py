import time
import serial
from NeoPixelMatrix import NeoPixelMatrix
from CircuitPlayGround import CircuitPlayGround
from PIL import Image
from PIL import ImageDraw

image = Image.new("RGB", (320, 32))
#image = Image.open("digikeyx10.png")
draw = ImageDraw.Draw(image)
draw.line( (0,0,31,31), fill=(0,255,0) )
draw.line( (0, 31, 31, 0), fill=(0,255,0) )
draw.line( (32,0,63,31), fill=(255,0,0) )
draw.line( (32, 31, 63, 0), fill=(255,0,0) )

draw.rectangle((64, 0, 95, 31), fill=(0, 0, 255), outline=(255,0,0))
draw.rectangle((96, 0, 127, 31), fill=(0, 255, 255), outline=(255,0,0))
draw.rectangle((128, 0, 159, 31), fill=(255, 255, 0), outline=(255,0,0))
draw.rectangle((160, 0, 191, 31), fill=(255, 0, 0), outline=(255,0,0))
draw.rectangle((192, 0, 223, 31), fill=(0, 255, 0), outline=(255,0,0))
draw.rectangle((224, 0, 255, 31), fill=(255, 0, 255), outline=(255,0,0))
draw.rectangle((256, 0, 287, 31), fill=(255, 255, 255), outline=(255,0,0))
draw.rectangle((256, 0, 287, 31), fill=(0, 0, 0), outline=(255,255,0))
image.show()

lastDrawTime = 0
animationTime = 0
counter = 0
goingUp = 1

circuitPlayground = CircuitPlayGround('/dev/cu.usbmodem1411')
neoMatrix = NeoPixelMatrix('/dev/cu.usbmodem2115241')

neoMatrix.Clear()
neoMatrix.SetImage(image, 0, 0)

while 1:
	if time.time() - lastDrawTime > 0.03 :
		neoMatrix.DrawLEDMemory()
		lastDrawTime = time.time()

	circuitPlayground.Read()
	capValue = circuitPlayground.Cap12/10
	#neoMatrix.SetAllRed(circuitPlayground.Cap12/10)

	#if time.time() - animationTime > 0.2 :
	#	draw.rectangle( (0,0, 319, 31), fill = (0,0,0), outline=(0,0,0))
	#	draw.rectangle((capValue, 0, capValue+31, 31), fill=(255, 0, 0), outline=(255,0,0))
	#	neoMatrix.SetImage(image, 0, 0)
