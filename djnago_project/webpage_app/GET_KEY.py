import json



class KEY:
    def __init__(self):
        with open('APIkey/API_keys.json') as json_file:
            self.json_data = json.load(json_file)

    def getBusKey(self):
        json_busKey = self.json_data['busInfo_API']
        return json_busKey

    def getSubwayKey(self):
        json_busKey = self.json_data['realtimeArrive_API']
        return json_busKey

key = KEY()
print(key.getBusKey())
print(key.getSubwayKey())