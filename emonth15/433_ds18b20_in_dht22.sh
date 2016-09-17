
		echo "starting avrdude upload emonTH V1.5 433Mhz DS18B20 in DHT22 Socket"
		avrdude  -u -c arduino -p ATMEGA328P -P /dev/ttyUSB0 -b 115200 -U flash:w:/home/oem/firmware/emonTH/emonTH_V1.5/emonTH_DHT22_DS18B20_RFM69CW_Pulse/compiled/emonTH_DS18B20_in_DHT22_socket.cpp.hex

