# SensorNetwork2020_DashServer_SDS011_DHT22
Author: Daniel Jarvis
Contacts:  jarvissan21@gmail.com

# Status : (Git instruction under construction, GITでマニュアルの作成中)
## 2021/01/31 The Readme and set up instruction are currently a bit of a mess, but will get it sorted and updated by the end of the month 
## 2021 GOAL:  Create sensors interface with all option able to be changed in the interace. 

Successor to [SDS-011-Python](https://github.com/JarvisSan22/SDS-011-Python)
Happy to recive feedback, and implement contributions  

Raspberry pi (RPI) or linux system base for a sensor network, of SDS011 and DHT22. 
Network made up of ESP8266 Sensor nodes sending data to the network base over a local ip. 
Using the previous code in [SDS-011-Python](https://github.com/JarvisSan22/SDS-011-Python), GPS maps walk and logger data can be run on a RPI 
Network data is displated using plotly dash for a nice clean interface.


![DASH1](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/Dash1.png)
![DASH2](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/Dash2.png)

# Kit List 
- [SDS011]
- [RPI3]
- [GPS]
- [DHT22]
- [ESP8266]
- [Battery Pack]

 
RPI3 2019 Setup Video 2019, for previous  
[Set up Video](https://www.youtube.com/watch?v=fvaiyqwaWeM)



#Base Code set up 
```
sudo apt-get update
sudo apt-get upgrade
```

**WIfi set up** 
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
add  your network network
```
network={
   ssid="{your interent name}"
   psk="{your internet password}"
}
```

**Download this repository**
```
git clone https://github.com/SensorNetwork2020_DashServer_SDS011_DHT22
```

# DHT22 Set up 

Intall the package

```
 'sudo python3  SDS-011-Python-master/AQ/Scripts/DHT/setup.py install'
```

# GPS Set up 
GPS Dongle G-mouse, set up video for setting up the dolge GPS as the RPI3 clock !!!
https://www.youtube.com/watch?v=Oag9qYuhMGg


1st get gps module
```
sudo apt-get install gpsd gpsd-clients python-gps chrony
```
2nd  in terminal 
```
sudo nano /etc/default/gpsd
```
set the following
``` 
START_DAEMON=”true”
USBAUTO=”true”
DEVICES=”/dev/ttyACM0″
GPSD_OPTIONS=”-n”
```
3rd  in the terminal 
```
sudo nano /etc/chrony/chrony.conf
```
Add the following line to the end of the file:

```
refclock SHM 0 offset 0.5 delay 0.2 refid NMEA
```
3rd Reboot the RPI3 ""sudo reboot""

4th  check that both are active in the terminal
```
systemctl is-active gpsd
systemctl is-active chronyd
su
```
5th see the data
```
gpsmon -n
```



