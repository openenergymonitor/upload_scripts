#!/usr/bin/env python

# Automated upload and test
# Upload code to ATmega328 via ISP / Serial and check for RF data received

# By Glyn Hudson
# Part of the openenergymonitor.org project


import serial, sys, string, commands, time, subprocess
from subprocess import Popen, PIPE, STDOUT

###################################################### DEFENITIONS ###################################################################
rx_device = False # Is Rx device present?
rx_port = '/dev/ttyUSB1'
rx_baud = 38400
rx_group = '210g'
rx_frequency = '4b'

firmware_base_path = '/home/oem/firmware/'
emontx_path = 'emonTxFirmware/emonTxV3/RFM/emonTxV3.4/emonTxV3_4_DiscreteSampling/compiled/'
emonth_path = 'emonTH/emonTH_DHT22_DS18B20_RFM69CW_Pulse/compiled/'
emonpi_path = 'emonpi//Atmega328/emonPi_RFM69CW_RF12Demo_DiscreteSampling/compiled/'

device = 'ATMEGA328P'
upload_port = '/dev/ttyUSB0'
upload_baud = '115200'
new_serial_baud = '38400'
new_serial_baud = '9600'

isp_upload_default = '-V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:'
serial_upload_default = '-u -c arduino -p' + device + '-P' + upload_port  + '-b' + upload_baud + '-U flash:w:'

#####################################################################################################################################

print 'OpenEnergyMonitor Upload & Test'
print ' '
print "Select Upload"

while(True):
    print "MENU: "
    print 'Make selection then hit Enter >'
    print "(1) for emonTx (Firmware V2.3)"
    print "(2) for emonTH (Firmware V2.6)"
    print "(3) for emonPi (Firmware V2.0)"
    print "(4) for RFM69Pi (Firmware V1.3)"
    print ' '
    print "(5) to view serial window"
    print "(e) to EXIT"
    nb = raw_input('> ')
    if nb=='1':
	    print "(1) for emonTx RFM69CW 433Mhz"
	    print "(2) for emonTx RFM69CW 868Mhz"
	    nb2 = raw_input('> ')
	    if nb2=='1':
		    while True:
			    print "emonTx RFM69CW 433Mhz"
			    cmd = serial_upload_default + firmware_base_path + emontx_path + 'emonTxV3_RFM69CW_latest_433.hex'
			    subprocess.call(cmd, shell=True)
			    time.sleep(1)
          	    ser = serial.Serial(upload_port, new_serial_baud, timeout=2)
          	    serial = ser.readline()
          	    print serial
          	    choice = raw_input('Hit Enter to upload again or any other key then Enter to return to menu>')
          	    if choice == '':
          		    print 'upload again...'
          		if choice != ''
          		    break
