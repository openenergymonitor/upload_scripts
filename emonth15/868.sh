
		echo "starting avrdude upload emonTH V1.5 868Mhz"
		avrdude  -u -c arduino -p ATMEGA328P -P /dev/ttyUSB0 -b 115200 -U flash:w:/home/oem/firmware/emonTH/emonTH_DHT22_DS18B20_RFM69CW_Pulse/compiled/emonTH_latest_868.hex

