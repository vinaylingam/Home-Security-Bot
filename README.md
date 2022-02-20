# Home-Security-Bot
A Telegram API implemented Bot to notify a user regarding Home Security with Arduino and Thingspeak

## Contents
1. Working of **Home-Security-Bot**
2. Commands
3. run it in your local

## Working of Home-Security-Bot
Two sensors are connected to Node MCU (Esp8266), **Ultra sonic sensor** and **DHT 11**. Ultra sonic sensor will measure the distance between sensor and nearest obstacle with echoes. DHT 11 will measure Temperature and Humidity. with Node MCU calculated distances and temperature are stored in **ThingSpeak**(An Open source IoT application and API to store and retrieve data).

now we will set the Ultra sonic sensor some where near door such that if there door is moved, sensor should sense some distance. this distance will be sent to ThingSpeak and our [HomeSecurityenderBot](https://t.me/HomeSecurityenderBot)(telegram bot) will compare the data sent from ThingSpeak and a threshold(which we set). if the distance is too much then a notification will be sent to User immediately that the door is moved.

## Commands
The following commands are included in bot.
> /distance - currently measured distance by sensor.

> /temperature - temperature in the house.

> /setDistance - threshold to compare distance from ThingSpeak

## run it in your local
i hid the `Token` in TOKEN.py file and git ignored it. so if u run HomeSecurityenderBot.py file, u will probably get an error.
so create a `TOKEN.py` file in the same folder and include the following line.

> token = 'xxxxxxxxxxxxxxxxxx'

replace the xxxxxxxxxxx with the `Token` u got from [BotFather](https://t.me/BotFather)

```
for any queries, contact.
gmail - vinaylingam18@gmail.com
telegram - vinaylingam
discord - vinay#4904
```
