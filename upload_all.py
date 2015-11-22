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
EMONTX_PATH = "emonTxFirmware/emonTxV3/RFM/emonTxV3.4/emonTxV3_4_DiscreteSampling/compiled/"
EMONTH_PATH = "emonTH/emonTH_DHT22_DS18B20_RFM69CW_Pulse/compiled/"
EMONPI_PATH = "

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
  print 'MENU: \n'
	print 'Make selection then hit Enter >'
	print '(1) for emonTx'
	print '(2) for emonTH'
	print '(3) for emonPi'
	print '(4) for RFM69Pi'
	print ' '
	print '5) to view serial window
	print '(e) to EXIT'
	nb = raw_input('> ')

	if nb=='1': #emonTx --------------------------------------------------------------------------------------------------------
	  print '(1) for emonTx RFM69CW 433Mhz'
	  print '(2) for emonTx RFM69CW 868Mhz'
	  nb2 = raw_input('> ')
	  
	  if nb2=='1':
	    while True:
		    print 'emonTx RFM69CW 433Mhz'
		    cmd = SERIAL_UPLOAD_DEFAULT + FIRMWARE_BASE_PATH + EMONTX_PATH + "emonTxV3_RFM69CW_latest_433.hex"
		    subprocess.call(cmd, shell=True)
          time.sleep(1)
		    ser = serial.Serial(UPLOAD_PORT, NEW_SERIAL_BAUD, timeout=2)
		    print = ser.readline()
		    choice = raw_input("Hit Enter to upload again or any other key then Enter to return to menu")
		    if choice == '':
		      print "upload again...\n"
		    else:
		      break # return to menu
		    

	
	if nb=='2': #emonTH--------------------------------------------------------------------------------------------------------
	print 'emonTH RFM69CW 433Mhz'
	cmd = SERIAL_UPLOAD_DEFAULT + FIRMWARE_BASE_PATH + EMONTH_PATH "emonTH_latest.hex"
	subprocess.call(cmd, shell=True)
    time.sleep(1)
	ser = serial.Serial(UPLOAD_PORT, OLD_SERIAL_BAUD, timeout=2)
	for num in range(1,5)
	  print = ser.readline()
		

	if nb=='e':
		print 'Exit'
		sys.exit
		
	else:
	  "Invalid input"


