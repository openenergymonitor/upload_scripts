# Script for RaspberryPi with RFM12Pi 
# Automated upload and test 
# Upload code to emonTx via ISP and check for RF data received 

# By Glyn Hudson 11/02/2015
# Part of the openenergymonitor.org project


import serial, sys, string, commands, time, subprocess
from subprocess import Popen, PIPE, STDOUT

print' '
print 'OpenEnergyMonitor all unit Upload & test 15/04/15'
print ' ' 
print 'Select Upload:'

print 'setting Rx module to receive on 433Mhz and 210 network group....'
ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
ser.write("210g")
time.sleep(1)
ser.write("4b")
ser.close()

while(1):
	print ' ' 
	print 'Enter >' 
	print '(x) for emonTx'
	print '(h) for emonTH'
	print '(i) for emonPi'
	print '(r) for RFM69Pi'
	print '(e) to EXIT and shutdown'
	nb = raw_input('> ')
        print(nb)

	if nb=='x': 
		print 'emonTx V3.4 RFM69CW 433Mhz'
		print 'Attempting RFM69CW  433Mhz emonTx firmware upload via ISP....'
		cmd = 'sudo avrdude -V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:/home/pi/emonTxFirmware/emonTxV3/RFM/emonTxV3.4/emonTxV3_4_DiscreteSampling/V1_6_emonTxV3_RFM69CW_DiscreteSampling_433_bootloader.cpp.hex:i  -Ulock:w:0x0F:m'
		subprocess.call(cmd, shell=True)
                time.sleep(1)
		ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
		linestr = ser.readline()
		print linestr
		#print len(linestr)
		if (len(linestr)>0):
			if (int(linestr[3] + linestr[4])==10): 
				print 'PASS!...RF RECEIVE SUCCESS from emonTx on node 10'
			else:
				print 'FAIL...RF received but not from the emonTx on node 10'
		else: 
			print 'FAIL...no RF received'
		ser.close()

	if nb=='h': 
		print 'emonTH RFM69CW 433Mhz'
		print 'RFM69CW 433Mhz emonTH firmware upload via ISP....'
		cmd = 'sudo avrdude -V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:/home/pi/emonTH/emonTH_DHT22_DS18B20_RFM69CW/emonTH_V1.5_RFM69CW_Bootloader.hex:i  -Ulock:w:0x0F:m'
		subprocess.call(cmd, shell=True)
                time.sleep(1)
		ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
		linestr = ser.readline()
		print linestr
		if (len(linestr)>0):
			if (int(linestr[3] + linestr[4])==19): 
				print 'PASS!...RF RECEIVE SUCCESS from emonTH RFM69CW on node 19'
			else:
				print 'FAIL...RF received but not from the emonTH on node 19 (Check DIP switch setting?)'
		else: 
			print 'FAIL...no RF received'
		ser.close()

	if nb=='r': 
		print 'RFM69Pi 433Mhz'
		print 'RFM69Pi firmware upload via ISP....'
		cmd = 'sudo avrdude -V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xE2:m -U flash:w:/home/pi/RFM2Pi/firmware/RFM69CW_RF_Demo_ATmega328/Optiboot328_8mhz_RFM69CW_RF12_Demo_ATmega328.cpp.hex:i'
		subprocess.call(cmd, shell=True)
                time.sleep(1)
		print 'Check JeeLink transmitter connected > Flashing RED LED on the RFM69Pi = SUCCESS?'

	if nb=='i': 
		print 'emonPi RFM69CW 433Mhz'
		print 'RFM69CW 433Mhz emonPi firmware upload via ISP....'
		cmd = 'sudo avrdude -V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:/home/pi/emonpi/Atmega328/emonPi_RFM69CW_RF12Demo_DiscreteSampling/compiled/emonPi_latest_bootloader.hex:i'

		subprocess.call(cmd, shell=True)
                time.sleep(1)
		ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
		linestr = ser.readline()
		print linestr
		if (len(linestr)>0):
			if (int(linestr[2] + linestr[3])==5): 
				print 'PASS!...RF RECEIVE SUCCESS from emonPi'
			else:
				print 'FAIL...RF received but not from the emonPi on node 5'
		else: 
			print 'FAIL...no RF received'
		ser.close()

	if nb=='e':
		print 'END'
		print 'Raspberry Pi Shutdown NOW!....'
		time.sleep(2)
		cmd = 'sudo halt'
		subprocess.call(cmd, shell=True)
        	sys.exit







	#if ((nb!=8) and (nb!=4)):
	#	print 'Invalid selection, please restart script and select b or w'

