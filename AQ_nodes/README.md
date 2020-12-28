# AQ_nodes

# Current Nodes
- [DHT22-Flasknode.ino] ESP8266_DHT22 NODE


**ESP8266_DHT22 NODE SETUP**
*Software*
https://www.arduino.cc/en/software

1. ESP8266 board install 
First the EPS866 board need to be installed on Arduino
まず Adduinoでは、EPS866のボルドはインストールしなければなりません。

@File> Preferences@
Add the past the followng line in Additional Boards Managers URLs;
追加のボードマネージャのURLの空間では、下記のURLを貼り付けます。
https://arduino.esp8266.com/stable/package_esp8266com_index.json
![DHT22_ARDUINO_INSTALL](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/DHT22_ARDUINO_INSTALL.jpg)

Now to load the board, in Boards Manager
Tools > Board > Boards Manager…
Then type eps8266 and install the board.
今　ボードマネージャでは、ボードを読み込みましょう。
シール＞ボード＞ボードマネージャ
そこで、eps8266を書いて、ボードをインストールをしてください。
![Board_Manger_eps_JP](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/Board_Manger_eps_JP.jpg)
![Board_Manger_JP](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/Board_Manger_JP.jpg)

Lastely we have to select the board
Tools>Boards: >  Generic ESP8266 Module 
最後にボードを選択しましょう。
ツール＞ボード>Generic ESP8266 Module 







2. DHT sensors Libary
Click libary manager setting, Search from DHT22 and install DHT Ssensor libaray 
![DHT22](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/DHT22_ARDUINO_INSTALL.jpg)

![DHT22](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/DHT22_ARDUINO_INSTALL.jpg)


https://qiita.com/mono_taro/items/80bcf6da049d87d54eac
https://randomnerdtutorials.com/esp8266-dht11dht22-temperature-and-humidity-web-server-with-arduino-ide/
https://randomnerdtutorials.com/how-to-install-esp8266-board-arduino-ide/
