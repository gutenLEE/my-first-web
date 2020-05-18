# *-* coding: utf-8 *-*
import datetime
import json
import urllib
from urllib.request import urlopen, Request

# district x, y
nx = 60
ny = 127


class Weather_api:
    # 실시간(getUltraSrtFcst) - 기온, 하늘상태, 강수량, 상수확률
    def get_current_weather(nx, ny):

        current_date_time = (datetime.datetime.today() - datetime.timedelta(hours=1)).strftime('%Y%m%d%H00')
        today_date = current_date_time[:8]
        current_time = current_date_time[8:]

        key = 'PJsLmdbHRcHiLAUnsUfnTdZaIS0NFpR0Nndy82K1OQwLmf%2BVgvXhrkoeOMqTW6%2FdzOJQ5RbF%2FmDb7oocoMY%2BYQ%3D%3D'
        url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst?ServiceKey={key}&pageNo=&numOfRows=40&dataType=JSON&base_date={today_date}&base_time={current_time}&nx={nx}&ny={ny}&'
        parse_url = url.format(key, today_date, current_time, nx, ny)


        # to request Weather API
        request = urllib.request.Request(parse_url)
        response_body = urlopen(request).read()
        data = json.loads(response_body)
        re_data = data['response']['body']['items']['item']
        # print(re_data)

        #  기온, 하늘상태, 강수량, 강수확률
        now_temp = []
        sky = []
        precipitation = []
        rain_forecast = []

        for data in re_data:
            if data['category'] == 'T1H':
                now_temp.append(data['fcstValue'])
            if data['category'] == 'SKY':
                sky.append(data['fcstValue'])
            if data['category'] == 'RN1':
                precipitation.append(data['fcstValue'])
            if data['category'] == 'PTY':
                rain_forecast.append(data['fcstValue'])

        # print(now_temp[0])
        # print(sky[0]) // 하늘상태 1:맑음 3:구름많음 4:흐림
        if sky[0] == 1:
            sky = "맑음"
        elif sky[0] == 3:
            sky = "구름많음"
        else: sky = "흐림"


        # 강수량(1 / 5 / 10 / 20 / 40 / 70 / 100)
        print(precipitation[0])
        # 강수확률
        print(rain_forecast[0])

        return now_temp[0], sky, precipitation[0], rain_forecast[0]

    # 하루 예보(getVilageFcst) - 강수확률, 최고, 최저기온 / 이것은 실시간 조회가 아닌 db에 저장해서 사용해야 한다.
    def get_max_min_temp(nx, ny):
        current_date_time = (datetime.datetime.today() - datetime.timedelta(hours=1)).strftime('%Y%m%d0200')
        today_date = current_date_time[:8]
        current_time = current_date_time[8:]
        key = 'PJsLmdbHRcHiLAUnsUfnTdZaIS0NFpR0Nndy82K1OQwLmf%2BVgvXhrkoeOMqTW6%2FdzOJQ5RbF%2FmDb7oocoMY%2BYQ%3D%3D'
        url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?ServiceKey={key}&pageNo=&numOfRows=40&dataType=JSON&base_date={today_date}&base_time={current_time}&nx={nx}&ny={ny}&'
        parse_url = url.format(key, today_date, current_time, nx, ny)


        # to request Weather API
        request = urllib.request.Request(parse_url)
        response_body = urlopen(request).read()
        data = json.loads(response_body)
        re_data = data['response']['body']['items']['item']

        # pop 강수확률, TMN 아침최저기온 TMX 낮 최고기온
        pop = []
        for data in re_data:
            if data['category'] == 'POP':
                pop.append(data['fcstValue'])
            if data['category'] == 'TMN':
                low_temp = data['fcstValue']
            if data['category'] == 'TMX':
                high_temp = data['fcstValue']

        # print(pop[0], low_temp, high_temp)
        return {'min_temp':low_temp, 'max_temp': high_temp}






