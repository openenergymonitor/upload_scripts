while :
	do
		echo "starting avrdude upload emonPi Serial upload"
		avrdude  -u -c arduino -p ATMEGA328P -P /dev/ttyUSB0 -b 115200 -U flash:w:/home/oem/firmware/emonpi/Atmega328/emonPi_RFM69CW_RF12Demo_DiscreteSampling/compiled/emonPi_latest_bootloader.hex
		sleep 5
done
