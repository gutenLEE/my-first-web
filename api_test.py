# *-* coding: utf-8 *-*

from urllib import response
from urllib.request import urlopen, Request
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import simplejson
import pandas as pd
from kma import Weather
from urllib.error import HTTPError
import json
import xmltodict
import xml.etree.ElementTree as ET



# service_key = "594146617a626e6d3130346942654575"
# url = f"http://openapi.seoul.go.kr:8088/{service_key}/json/bikeList/1/500/".format({}, service_key)
district_code = 1111051500
url = f'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={district_code}'.format({}, district_code)
xml_data = urlopen(url).read().decode('utf-8')
json_data = xmltodict.parse(xml_data)
print(json_data['rss']['channel']['item']['category'])
print(json_data['rss']['channel']['item']['description'])
json_weather = json_data['rss']['channel']['item']['description']['body']['data']

weathers = [data for data in json_weather]
print(weathers)

for weather in weathers:
    print(weather['day'])
    print(weather['hour'])
    print(weather['temp'])
    print(weather['sky'])



# re_data = data['rentBikeStatus']['row']
# station_id = re_data[0]['stationId']
# station_name = re_data[0]['stationName']
# get_rackTotCnt = re_data[0]['rackTotCnt']
# get_bikesCnt = re_data[0]['parkingBikeTotCnt']
# shared = re_data[0]['shared']





# if response_body.status_code != 200:
#     print('Failed to get data:', response_body.status_code)
# else:
#     print('First 100 characters of data are')
#     print(data[:100])



"""
service_key = 'PJsLmdbHRcHiLAUnsUfnTdZaIS0NFpR0Nndy82K1OQwLmf+VgvXhrkoeOMqTW6/dzOJQ5RbF/mDb7oocoMY+YQ=='
api_key_decode = unquote(service_key)


URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'

params = '?' + urlencode({
    quote_plus(
        "serviceKey"): "PJsLmdbHRcHiLAUnsUfnTdZaIS0NFpR0Nndy82K1OQwLmf+VgvXhrkoeOMqTW6/dzOJQ5RbF/mDb7oocoMY+YQ==",
    quote_plus("numOfRows"): "10",  # 한 페이지 결과 수 // default : 10
    quote_plus("pageNo"): "1",  # 페이지 번호 // default : 1
    quote_plus("dataType"): "JSON",  # 응답자료형식 : XML, JSON
    quote_plus("base_date"): "20200225",  # 발표일자 // yyyymmdd
    quote_plus("base_time"): "0600",  # 발표시각 // HHMM, 매 시각 40분 이후 호출
    quote_plus("nx"): "60",  # 예보지점 X 좌표
    quote_plus("ny"): "127"  # 예보지점 Y 좌표
})

request = Request(URL + params)
print(request)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)




# # URL parsing
# req = urllib.request.Request(URL + unquote(params))
# # Get Data from API
# print(req)
# response_body = urlopen(req).read()  # get bytes data
# print(response_body)
# # Convert bytes to json
# data = json.loads(response_body)
# print(data)

"""