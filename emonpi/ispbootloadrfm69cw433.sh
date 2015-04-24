
		echo "starting ISP bootlaoder upload emonTx V3.4 433Mhz RFM69CW"
		sudo avrdude -V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:/home/oem/firmware/emonpi/Atmega328/emonPi_RFM69CW_RF12Demo_DiscreteSampling/compiled/emonPi_latest_bootloader.hex:i  -Ulock:w:0x0F:m


