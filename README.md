# Giant Circuit Playground

This project contains all of the firmware and software necessary to make a giant circuit playground.

-----------------------------------------------------------

## Setup

### Actual Circuit Playground Firmware

The circuit playground firmware is in the "CircuitPlayGround2Ft" folder. 

Treat this as any other .ino file, and just flash it to the Actual Circuit Playground

### Teensy Firmware

The Teensy firmware is in the "TestEthern" folder. 

To flash the teensy, you will need to install Teensyduino into Arduino. The firmware should compile after Teensyduino has been setup.

After the firmware has been compiled, press the reset button on the Teensy to flash it.

### Raspberry Pi Python Script

The Raspberry Pi python scripts are in the "RaspPiPythonScripts" folder.

If this is a new setup, you will need to open the file TestNeoPixelMatrix.py and follow these steps:
* Scroll down to line 12 and set the SystemType variable as follows
 * SystemType = 0 for the 4 foot playground
 * SystemType = 1 for the 2 foot playground
* Test that running TestNeoPixelMatrix.py works.
* If it works, then we need to set this up to be called on reboot.
 * Find the path to the TestNeoPixelMatrix.py file
 * Edit /etc/rc.local as root
 * Write "sudo /usr/bin/python <path from first step> &" on the last line of the file
 * Save the file and reboot!
 
---------------------------------------
 
## Modes
 
### Attract Mode
 
Shows a series of animations, bright colors, and the DigiKey logo. Designed to grab attention from far away
 
### VJ Mode
 
Uses Accelerometers to spin a rainbow. Players can experiment with making the rainbow move faster, slower, reverse direction, and stop!
 
### Simon Mode
 
Play Simon! Hopefully we can call it "Simon" legally.

### Audio Reactive Mode
 
The circuit playground acts as a giant VU meter!

------------------------------------------------

## Troubleshooting

### My Circuit Playground won't respond to button presses!

Reset the circuit playground. 

The Circuit Playground library continuously auto calibrates its capacitive touch which can cause it to be unresponsive if left for long periods of time.
Resetting the system will make it responsive again.

### Circuit playground will not light up on boot

Plug the circuit playground into the Raspberry Pi and reboot the system.

This is a known bug. The python code will not start if a circuit playground is not plugged into the Raspberry Pi on startup.


------------------------------------------------

## Wiring

### 2ft CP

Raspberry Pi 3 connects over Ethernet to a [Teensy 3.2](https://www.pjrc.com/store/teensy32.html) with [Ethernet Shield](https://www.pjrc.com/store/wiz820_sd_adaptor.html)/[WIZ820IO](http://www.digikey.com/product-detail/en/wiznet/WIZ820IO/1278-1015-ND/3829655) and an [OCTOWS shield](https://www.pjrc.com/store/octo28_adaptor.html).

The [Adafruit 8x8 matrices](https://www.adafruit.com/products/1487) are connected clockwise from the top right Matrix to output 1. 1-6 are in order, output 7 connects to matrix 7 & 8, output 8 connects to matrix 9 & 10.

### 4ft CP
Raspberry Pi 3 with a LED [matrix shield](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/adapter/active-3) from [OSHpark](https://oshpark.com/shared_projects/bFtff2GR). Matrices are connected in line clockwise beginning with the top right matrix with 16 pin IDC cables.



