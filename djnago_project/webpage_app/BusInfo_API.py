import json
from pprint import pprint
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen
import requests
import xmltodict
import os

with open('static/API_keys.json') as json_file:
    json_data = json.load(json_file)
json_busKey = json_data['busInfo_API']
api_key_decode = requests.utils.unquote(json_busKey)

# 지정된 좌표와 반경 범위 내의 정류소 목록을 조회한다.
url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos'
queryParams = '?' + urlencode({quote_plus('ServiceKey'): api_key_decode,
                               quote_plus('tmX'): '126.98633090000001',
                               quote_plus('tmY'): '37.563398',
                               quote_plus('radius'): '500'})

request = urlopen(url + queryParams)
print(url + queryParams)
data = request.read().decode('utf8')
json_data = json.loads(json.dumps(xmltodict.parse(data)))
data = json_data['ServiceResult']['msgBody']['itemList']

stationOnMap = []
for i in range(0, len(data)):
    a = {
        "gpsX": str(data[i]['gpsX']),
        "gpsY": str(data[i]['gpsY']),
        "stationNm": str(data[i]['stationNm'])
    }
    stationOnMap.append(a)


def stations_in_range_500m(lon, lat):
    # THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    # my_file = os.path.join(THIS_FOLDER, '\static\API_keys.json')

    with open('static/API_keys.json') as json_file:
        json_data = json.load(json_file)
    json_busKey = json_data['busInfo_API']
    api_key_decode = requests.utils.unquote(json_busKey)

    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos'
    queryParams = '?' + urlencode({quote_plus('ServiceKey'): api_key_decode,
                                   quote_plus('tmX'): str(lon),
                                   quote_plus('tmY'): str(lat),
                                   quote_plus('radius'): '500'})

    request = urlopen(url + queryParams)
    print(url + queryParams)
    data = request.read().decode('utf8')
    json_data = json.loads(json.dumps(xmltodict.parse(data)))
    data = json_data['ServiceResult']['msgBody']['itemList']

    stationOnMap = []
    for i in range(0, len(data)):
        a = {
            "gpsX": str(data[i]['gpsX']),
            "gpsY": str(data[i]['gpsY']),
            "stationNm": str(data[i]['stationNm'])
        }
        stationOnMap.append(a)

    pprint(stationOnMap)
    return stationOnMap

# lon= 126.98710488814648
# lat = 37.564544272951764
#
# stations_in_range_500m(lon, lat)


# a = {"arsId": data[i]['arsId'],
#       "dist": data[i]['dist'],
#       "gpsX": str(data[i]['gpsX']),
#       "gpsY": str(data[i]['gpsY']),
#       "stationId": str(data[i]['stationId']),
#       "stationNm": str(data[i]['stationNm']),
#       "stationTp": str(data[i]['stationTp'])}
