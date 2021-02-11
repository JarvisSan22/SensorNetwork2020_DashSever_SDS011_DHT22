# -*- coding: utf-8 -*-
"""
Created on 2021/02/11
@author: Daniel Jarvis
"""

#Basesettings
DATAFOLDER="/home/pi/SensorNetwork2020_DashServer_SDS011_DHT22/AQ_Data/"
RUNFOLDER="/home/pi/SensorNetwork2020_DashServer_SDS011_DHT22/AQ_run/Scripts/"
SERVERFOLDER=""
DEVICERAN="RPI"
#LOC=['Location Name','lat', 'lon'] 
LOC=['Home','', ''] 

#Server display settings "single":Just time series . "multi" Time series and GPS map
Type="single"
#IP Adress  
IP="{IP}" #Reciver at {IP}:8090, Interface at {IP}:5000 

#Check internet connect, URL to ping
URL = 'https://github.com/JarvisSan22/SensorNetwork2021_DashServer_SDS011_DHT22'

######Setting to run sensors of home unit#######
#Data record period(in seconds)
integration=10
#MODE LOG: logs data, new file every day #GPS add lat, long, alt to data if GPS is added #TEST create a new data file ever time scrip is run (GPS does the same as well)
MODE="LOG"  
#Note if GPS is "ON" ,it takes up "/dev/ttyACM0" port

##Desired Pollution sensors to run  (OPCN2 or 2 and SDS011)
OPCON="ON"
RUNSEN=["SDS011_1"]  #add your SDS011 name, if you have more then 1 sds attaced, add the other name to the array  i.e RUNSEN=["SDS011_1,SDS011_2"]
#Sensor ports for deried sensors, if you dont know check the /dev folder
RUNPORT=["/dev/ttyUSB0"] #for multipe SDS011 add a "/dev/ttyUSB#" #=number to this array

#Temp sensors port number, if a DHT11 or 22 is running get the por  
DHTON="ON"
DHTNAMES=["DHT22_1"]
DHTPINS=[14] #check the pin

#Light settings 
LIGHT="OFF" #LEDS option 
LIGHTPIN=[]
BLINKT="OFF"  #BLINkt hat option (Cant fit DHT22 with the BLINKET Hat)
PMVALUE=[10,20,30]  #Set intevals for light colors 



