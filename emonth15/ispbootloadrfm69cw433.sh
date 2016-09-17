
		echo "starting ISP bootlaoder upload emonTx V3.4 433Mhz RFM69CW"
		sudo avrdude -V -u -p atmega328p -c avrispmkII -P usb -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xFF:m -U flash:w:/home/oem/firmware/emonTH/emonTH_V1.5/emonTH_DHT22_DS18B20_RFM69CW_Pulse/compiled/emonTH_latest_Bootloader.hex:i  -Ulock:w:0x0F:m


