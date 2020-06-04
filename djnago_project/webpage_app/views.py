import datetime
from pprint import pprint
from urllib.request import urlopen
import simplejson

import xmltodict
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import test_db
from .pymongoTEST import MongoManager
from .WeatherAPI import Weather_api
from .Station_db import subway, bus_name_ID
from .subway_info_API import realtime_sub_Info, parse_station, timeTable, timetable_in_range, Timetable

nx = 60
ny = 127


def main(request):
    # 주소 3차원 배열
    addre = MongoManager.city_gu_dong
    json_addre = simplejson.dumps(addre)
    cities = []

    # 도시 리스트
    for d in addre:
        if d[0] not in cities:
            cities.append(d[0])

    context = {'addre': json_addre,
               'cities': cities,
               'test': simplejson.dumps(subway),
               'parse_station': simplejson.dumps(parse_station)}

    return render(request, 'main.html', context)

#
# def index(request):
#     # 현재 기온 / default 서울
#     # 0:temp / 1:sky status / 2:precipitation / 3:rain pop
#     temp = Weather_api.getUltraSrtFcst(nx=60, ny=127)
#     now_temp = temp[0]
#     sky_status = temp[1]
#     rain_pop = temp[3] + ' %'
#
#     # 주소 3차원 배열
#     addre = MongoManager.city_gu_dong
#     json_addre = simplejson.dumps(addre)
#     cities = []
#     for d in addre:
#         if d[0] not in cities:
#             cities.append(d[0])
#
#     # get XY
#     xy = MongoManager.get_XY("서울특별시")
#     x = xy['x']
#     y = xy['y']
#
#     # get max, min temp
#     temp = Weather_api.getVilageFcst(x, y)
#     max_temp = temp['max_temp'] + '℃'
#     min_temp = temp['min_temp'] + '℃'
#
#     # 전달할 데이터
#     context = {
#         'now_temp': now_temp,
#         'sky_status': sky_status,
#         'rain_pop': rain_pop,
#         'max_temp': max_temp,
#         'min_temp': min_temp,
#         'cities': cities,
#         'addre': json_addre,
#         # 'STATN_NM' : simplejson.dumps(STATN_NM),
#         'test': simplejson.dumps(subway),
#         'bus_name_ID': simplejson.dumps(bus_name_ID),
#     }
#     return render(request, 'index.html', context)
#
#
# def address(request):
#     print("i am address")
#     print("값 넘어온다야", request.GET.get('city_select'))
#     print("값 넘어온다야", request.GET.get('gu_select'))
#     print("값 넘어온다야", request.GET.get('option1'))
#     print("값 넘어온다야", request.GET.get('option2'))
#
#     # selected_city -> search 'gu' in DB
#     selected_city = request.GET.get('city_select')
#     gu_list = MongoManager.get_gu_name(selected_city)
#
#     # selected_gu -> search 'dong' in DB
#     selected_gu = request.GET.get('gu_select')
#     dong_list = MongoManager.get_dong_name(selected_city, selected_gu)
#
#     test_db.city = request.GET.get('city_select')
#     test_db.gu = request.GET.get('gu_select')
#
#     print("db", test_db.city)
#     print("db", test_db.gu)
#     # print(gu_list)
#     # print(dong_list)
#
#     context = {
#         "gu_list": gu_list,
#         "dong_list": dong_list,
#         "selected_city": selected_city,
#         "seleted_dong": selected_gu,
#     }
#
#     return render(request, 'index.html', context)
#
#
# def weather(request):
#     return render(request, 'weather_index.html')
#
#
# def transportaion(request):
#     print(request.GET.get('myInput'))
#     print(request.GET.get('ma'))
#     print(request.GET.get('line_code'))
#     line_code = request.GET.get('line_code')
#     station = request.GET.get('myInput') + '역'
#     subway_line = request.GET.get('ma')
#
#     # List 목록
#     arv_Msg = []
#     arv_Msg2 = []
#     expect_arv_Time = []
#     last_LineNm = []
#     up_Line = []
#
#     # subway info 함수 호출
#     a = request.GET.get('myInput')
#     b = line_code = request.GET.get('line_code')
#     result = realtime_sub_Info(a, b)
#
#     for re in result:
#         if re['subwayId'] == str(line_code):
#             arv_Msg.append(re['arvlMsg2'])
#             arv_Msg2.append(re['arvlMsg3'])
#             expect_arv_Time.append(re['barvlDt'])
#             last_LineNm.append(re['trainLineNm'])
#             up_Line.append(re['updnLine'])
#             pprint(re)
#     print(arv_Msg, arv_Msg2, expect_arv_Time)
#
#     context = {'station': station,
#                'subway_line': subway_line,
#                'line_code': line_code,
#                'arv_Msg': arv_Msg,
#                'arv_Msg2': arv_Msg2,
#                'expect_arv_Time': expect_arv_Time,
#                'last_LineNm': last_LineNm,
#                'up_Line': up_Line,
#                'result': simplejson.dumps(result)}
#
#     return render(request, 'transportaion_index.html', context)
#
#
# def get_weather(request):
#     print(request.GET)
#     # wb -> data
#     select_city = request.GET.get('city_select')
#     select_gu = request.GET.get('gu_select')
#     select_dong = request.GET.get('dong_select')
#     print(select_city, select_gu, select_dong)
#
#     # get XY
#     xy_location = MongoManager.get_XY(select_city, select_gu, select_dong)
#     x = xy_location['x']
#     y = xy_location['y']
#
#     # 0:temp 1:sky status 2:precipitation 3:rain pop
#     now_temp = Weather_api.getUltraSrtFcst(x, y)
#
#     # get max, min temp
#     temp = Weather_api.getVilageFcst(x, y)
#     max_temp = temp['max_temp'] + '℃'
#     min_temp = temp['min_temp'] + '℃'
#
#     context = {
#         "select_city": select_city,
#         "select_gu": select_gu,
#         "select_dong": select_dong,
#
#         "now_temp": now_temp[0] + '℃',
#         "sky_status": now_temp[1],
#         "rain_pop": now_temp[3] + '%',
#         "max_temp": max_temp,
#         "min_temp": min_temp
#     }
#
#     return render(request, 'submit_page.html', context)


def show(request):
    # 타이머 시간
    print(request.GET.get('real_time'))
    event_time = request.GET.get('real_time')
    evenTime = (event_time).split(":")
    event_hour = int(evenTime[0])
    event_minute = int(evenTime[1])

    # 역 input
    print(request.GET.get('myInput'))
    print(request.GET.get('ma'))
    print(request.GET.get('line_code'))
    station_NM = request.GET.get('myInput')
    station_line = request.GET.get('ma')
    station_code = request.GET.get('line_code')

    # 시, 구, 동 주소
    city_select = request.GET.get('city_select')
    gu_select = request.GET.get('gu_select')
    dong_select = request.GET.get('dong_select')

    if gu_select is None:
        gu_select = ""
    if dong_select is None:
        dong_select = ""

    # get XY
    xy_location = MongoManager.get_XY(city_select, gu_select, dong_select)
    x = xy_location['x']
    y = xy_location['y']

    # 초단기 실황 - 0: 기온, 2: 강수량, 3: 강수형태
    getUltraSrtNcst = Weather_api.getUltraSrtNcst(x, y)
    # 초단기예보 - 0:기온 1:하늘상태 2:강수량 3:강수확률
    getUltraSrtFcst = Weather_api.getUltraSrtFcst(x, y)
    # 동네예보 - 최고, 최저기온
    temp = Weather_api.getVilageFcst(x, y)

    realtime_temp = getUltraSrtNcst[0]
    realtime_precipitation = getUltraSrtNcst[1]
    realtime_rain = getUltraSrtNcst[2]
    realtime_sky = getUltraSrtFcst[1]

    max_temp = temp['max_temp']
    min_temp = temp['min_temp']
    pop = temp['pop']
    print(pop)

    # subway info 함수 호출
    result = realtime_sub_Info(station_NM,  station_code)

    # List 목록
    arv_Msg = []
    arv_Msg2 = []
    expect_arv_Time = []
    last_LineNm = []
    up_Line = []
    for re in result:
        if re['subwayId'] == str(station_code):
            arv_Msg.append(re['arvlMsg2'])
            arv_Msg2.append(re['arvlMsg3'])
            expect_arv_Time.append(re['barvlDt'])
            last_LineNm.append(re['trainLineNm'])
            up_Line.append(re['updnLine'])
            pprint(re)
    print(arv_Msg, arv_Msg2, expect_arv_Time)

    # +- 15분 사이 도착하는 열차 시간표
    subway = Timetable()

    Indays_time = subway.getIndays(station_code)
    Outdays_time = subway.getOutdays(station_code)
    UserTimeStr = event_time+":00"
    up = timetable_in_range(UserTimeStr, Indays_time)
    down = timetable_in_range(UserTimeStr, Outdays_time)


    context = {'event_hour': event_hour,
               'event_minute': event_minute,

               'realtime_temp':realtime_temp,
               'realtime_sky':realtime_sky,
               'realtime_precipitation':realtime_precipitation,
               'max_temp': max_temp,
               'min_temp': min_temp,
               'pop': pop[3],

               'station': station_NM,
               'subway_line': station_line,
               'line_code': station_code,
               'arv_Msg': arv_Msg,
               'arv_Msg2': arv_Msg2,
               'expect_arv_Time': expect_arv_Time,
               'last_LineNm': last_LineNm,
               'up_Line': up_Line,
               'result': simplejson.dumps(result),

               'up' : simplejson.dumps(up),
               'down' : simplejson.dumps(down)
               }

    return render(request, 'show.html', context)
