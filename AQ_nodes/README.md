

 [English](/README-jp.md)/[日本語](/README-jp.md)
# AQ_nodes

### Current Nodes
- [DHT22-Flasknode.ino] ESP8266_DHT22 NODE


#### ESP8266_DHT22 NODE SETUP
- **Software**
https://www.arduino.cc/en/software

1. ESP8266 board install \
First the EPS866 board need to be installed on Arduino \
まず Adduinoでは、EPS866のボルドはインストールしなければなりません。

**File> Preferences**
Add the past the followng line in Additional Boards Managers URLs \
追加のボードマネージャのURLの空間では、下記のURLを貼り付けます。\
https://arduino.esp8266.com/stable/package_esp8266com_index.json


Now to load the board, in Boards Manager \
Tools > Board > Boards Manager…\

Then type eps8266 and install the board. \
今　ボードマネージャでは、ボードを読み込みましょう。\
シール＞ボード＞ボードマネージャ \
そこで、eps8266を書いて、ボードをインストールをしてください。 \
![Board_Manger_eps_JP](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/Board_Manger_eps_JP.png)
![Board_Manger_JP](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/Board_Manager_JP.png)

2. Board select ボードを選択
Lastely we have to select the board
Tools>Boards: >  Generic ESP8266 Module 
最後にボードを選択しましょう。
ツール＞ボード>Generic ESP8266 Module 
![Board Select](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/Board_Select_JP.png)

3. DHT22 Set up  DHT22の設定
Select the libary manager, search for DHT22 and install "DHT sensor libary by Adafruit"\
Tools> Libary mangager\
ライブラリ整理を選択して、「DHT22」を探索して、 "DHT sensor libary by Adafruit"をインストールしてください。
ツール>ライブラリ整理
![DHT22_ARDUINO_INSTALL](https://github.com/JarvisSan22/SensorNetwork2020_DashServer_SDS011_DHT22/blob/main/AQ_nodes/DHT22_ARDUINO_INSTALL.jpg)


4. Code set up コードのセットアップする
Internet credention, data reciver ip, location of sensors and DHT22 pin need to be altered or checked.//
インタネットの設定、データを受信器のIP、センターのところの名と DHT22のポートを更新し確認します。/

```C++
// Replace with your network credentials
const char* ssid = "{ Internet name}";
const char* password = "{Internet password}";
String server= "{Data reciver ip}"; //IP displayed when running data_reciver.py
String nodename="DHT22"; //Node nane 
String nodeloc = "{Location}"; 
String pingdata = "";
String url = "";
IPAddress ip;                    // Gets IP address of your node
//unsigned long time;
#define DHTPIN 5     // Digital pin connected to the DHT sensor
```




#### Refrences 参考 /

* https://qiita.com/mono_taro/items/80bcf6da049d87d54eac
* https://randomnerdtutorials.com/esp8266-dht11dht22-temperature-and-humidity-web-server-with-arduino-ide/
* https://randomnerdtutorials.com/how-to-install-esp8266-board-arduino-ide/
