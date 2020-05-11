# *-* coding: utf-8 *-*
import datetime
import json
import urllib
from urllib.request import urlopen, Request
from urllib.parse import urlencode, unquote, quote_plus




current_date_time = (datetime.datetime.today() - datetime.timedelta(hours=1)).strftime('%Y%m%d%H00')
today_date = current_date_time[:8]
current_time = current_date_time[8:]
print(current_time)

# district x, y
nx = 60
ny = 127


def get_current_weather(today_date, current_time, nx, ny):
    key = 'PJsLmdbHRcHiLAUnsUfnTdZaIS0NFpR0Nndy82K1OQwLmf%2BVgvXhrkoeOMqTW6%2FdzOJQ5RbF%2FmDb7oocoMY%2BYQ%3D%3D'
    url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst?ServiceKey={key}&pageNo=&numOfRows=40&dataType=JSON&base_date={today_date}&base_time={current_time}&nx={nx}&ny={ny}&'

    parse_url = url.format(key, today_date, current_time, nx, ny)
    print(parse_url)

    # to request Weather API
    request = urllib.request.Request(parse_url)
    response_body = urlopen(request).read()
    data = json.loads(response_body)
    re_data = data['response']['body']['items']['item']
    print(re_data)

    # to design data - 기온, 하늘상태, 강수량, 강수확률
    temp = []
    sky = []
    precipitation = []
    rain_forecast = []

    for data in re_data:
        if data['category'] == 'T1H':
            temp.append(data['fcstValue'])
        if data['category'] == 'SKY':
            sky.append(data['fcstValue'])
        if data['category'] == 'RN1':
            precipitation.append(data['fcstValue'])
        if data['category'] == 'PTY':
            rain_forecast.append(data['fcstValue'])

    print(temp)
    print(sky)
    print(precipitation)
    print(rain_forecast)

    return temp, sky, precipitation, rain_forecast

get_current_weather(today_date, current_time, nx, ny)






"""
params = f'&pageNo=&numOfRows=40&dataType=JSON&base_date={today_date}&base_time={current_time}&nx={nx}&ny={ny}&'
def get_url(params, nx, ny):
    key = 'PJsLmdbHRcHiLAUnsUfnTdZaIS0NFpR0Nndy82K1OQwLmf%2BVgvXhrkoeOMqTW6%2FdzOJQ5RbF%2FmDb7oocoMY%2BYQ%3D%3D'
    url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst?ServiceKey={key}'
    params = params.format(today_date, current_time, nx, ny)
    callback_url = url+params
    return callback_url
"""



# service_key = 
# url = f"http://openapi.seoul.go.kr:8088/{service_key}/json/bikeList/1/500/".format({}, service_key)
# district_code = 1111051500
# url = f'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={district_code}'.format({}, district_code)
# xml_data = urlopen(url).read().decode('utf-8')
# json_data = xmltodict.parse(xml_data)
# print(json_data['rss']['channel']['item']['category'])
# print(json_data['rss']['channel']['item']['description'])
# json_weather = json_data['rss']['channel']['item']['description']['body']['data']
#
# weathers = [data for data in json_weather]
# print(weathers)
# tmp_list = []
# print(weathers[0])
#
# weathers = [data for data in json_weather]
# tmp_list = []
#
# for key, value in weathers[0].items():
#     tmp_list.append(value)
#     print(key, value)
#
# now_temp = tmp_list[3] + ' 도'
# title = "기온"
# print(now_temp)



