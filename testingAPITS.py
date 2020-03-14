import requests

response = requests.get('https://api.thingspeak.com/channels/1019045/feeds.json?results=2')
fieldresponse = requests.get('https://api.thingspeak.com/channels/1019045/fields/1.json?results=1');
print(response)
print(fieldresponse)
