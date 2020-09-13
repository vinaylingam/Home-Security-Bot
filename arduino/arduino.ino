#include "ThingSpeak.h"
#include <DHT.h>
#include <ESP8266WiFi.h>
  
//----------- Enter you Wi-Fi Details---------//
char ssid[] = "xxxxxxxx"; //SSID
char pass[] = "yyyyyyyy"; // Password
//-------------------------------------------//

#define DHTPIN 0          //pin where the dht11 is connected
DHT dht(DHTPIN, DHT11);

const int trigger = 16;
const int echo = 5;
long T;
float distanceCM;
float temperature;
WiFiClient  client;

unsigned long myChannelID = 123456; // Channel ID
const char * myWriteAPIKey = "xxxxxxxxxxx"; // Your write API Key

void setup()
{
  Serial.begin(115200);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  WiFi.mode(WIFI_STA);
  ThingSpeak.begin(client);
}
void loop()
{
  if (WiFi.status() != WL_CONNECTED)
  {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    while (WiFi.status() != WL_CONNECTED)
    {
      WiFi.begin(ssid, pass);
      Serial.print(".");
      delay(5000);
    }
    Serial.println("\nConnected.");
  }
      
  delayMicroseconds(10);
  T = pulseIn(echo, HIGH);
  distanceCM = T * 0.034;
  distanceCM = distanceCM / 2;
  Serial.print("Distance in cm: ");
  Serial.println(distanceCM);
  temperature = dht.readTemperature();
  Serial.print("Temperature in Degrees:");
  Serial.println(temperature);
  ThingSpeak.writeField(myChannelID, [1, 2], [temperature, distanceCM], myWriteAPIKey);
  delay(1000);
}
