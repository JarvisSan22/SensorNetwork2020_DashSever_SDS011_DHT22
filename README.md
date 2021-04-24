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

# Kit List Repository Strucutre 
'''bash
─ AQ_Plot
│   ├── AQMapfunctions.py
│   ├── AQfunctions_Archive_2019.py
├── AQ_Plot_server
│   ├── Index.py
│   ├── dash_server.py
│   └── data_reciver.py
├── AQ_nodes
│   ├── DHT22-Flasknode.ino
├── AQ_run
│   ├── Scriptss
│   │   ├── DHT/
│   │   ├── DHT.py
│   │   ├── GPS2.py
│   │   ├── sds_rec.py
│   │   ├── start.py
│   │   └── status.py
│   ├── data/
│   start.py
│   variables_temp.py
'''

# Kit List 
- Logger/reciver and server host Pi  [SDS011]+[RPI3/4]+ [DHT22] 
- sensor Node [ESP8266] + [DHT22]
- GPSLogger  [SDS011]+[RPI3/4]+ [DHT22] +[Battery Pack] [GPS]

 
## Old RPI3 Setup Video 2019
[Set up Video](https://www.youtube.com/watch?v=fvaiyqwaWeM)




