# Automated upload and test
# Upload code to ATmega328 via ISP / Serial and check for RF data received

# By Glyn Hudson
# Part of the openenergymonitor.org project


import serial, sys, string, commands, time, subprocess
from subprocess import Popen, PIPE, STDOUT

###################################################### DEFENITIONS ###################################################################
RX = False # Is Rx device present?
RX_PORT = "/dev/ttyUSB1"
RX_BAUD = 38400
RX_GROUP = "210g"
RX_FREQUENCY = "4b"

FIRMWARE_BASE_PATH = "/home/oem/firmware/"
DEVICE = "ATMEGA328P"
UPLOAD_PORT = "/dev/ttyUSB0"
UPLOAD_BAUD = 115200
NEW_SERIAL_BAUD = 38400
OLD_SERIAL_BAUD = 9600

ISP_UPLOAD_DEFAULT = "-V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:"
SERIAL_UPLOAD_DEFAULT = "-u -c arduino -p" + DEVICE + "-P" + UPLOAD_PORT  + "-b" + str(UPLOAD_BAUD) + "-U flash:w:"



#####################################################################################################################################




print' '
print 'OpenEnergyMonitor Upload & Test'
print ' '
print 'Select Upload:'


if RX:
  print 'setting Rx module to receive on 433Mhz and 210 network group....'
  ser = serial.Serial(RX_PORT, RX_BAUD, timeout=1)
  ser.write(RX_GROUP)
  time.sleep(1)
  ser.write(RX_FREQUENCY)
  ser.close()

while(1):
	print ' '
	print 'Enter >'
	print '(x) for emonTx'
	print '(h) for emonTH'
	print '(i) for emonPi'
	print '(r) for RFM69Pi'
	print '(e) to EXIT'
	nb = raw_input('> ')
        print(nb)

	if nb=='x':
		print 'emonTx RFM69CW 433Mhz'
		cmd = SERIAL_UPLOAD_DEFAULT + FIRMWARE_BASE_PATH + "emonTxFirmware/emonTxV3/RFM/emonTxV3.4/emonTxV3_4_DiscreteSampling/compiled/emonTxV3_RFM69CW_latest_433.hex"+":i"
		subprocess.call(cmd, shell=True)
                time.sleep(1)
		ser = serial.Serial(UPLOAD_PORT, NEW_SERIAL_BAUD, timeout=1)
		linestr = ser.readline()
		print linestr

	if nb=='e':
		print 'Exit'
		sys.exit







	#if ((nb!=8) and (nb!=4)):
	#	print 'Invalid selection, please restart script and select b or w'

