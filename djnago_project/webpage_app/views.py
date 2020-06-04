import datetime
from urllib.request import urlopen
import simplejson

import xmltodict
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import test_db
from .pymongoTEST import MongoManager
from .WeatherAPI import Weather_api
from .Station_db import STATN_NM, subway, bus_name_ID


nx = 60
ny = 127

def index(request):

    # 현재 기온 / default 서울
    # 0:temp / 1:sky status / 2:precipitation / 3:rain pop
    temp = Weather_api.get_current_weather(nx=60, ny=127)
    now_temp = temp[0] + '℃'
    sky_status = temp[1]
    rain_pop = temp[3] + ' %'


    # 주소 3차원 배열
    addre = MongoManager.city_gu_dong
    json_addre = simplejson.dumps(addre)
    cities = []
    for d in addre:
        if d[0] not in cities:
            cities.append(d[0])

    #get XY
    xy = MongoManager.get_XY("서울특별시")
    x = xy['x']
    y = xy['y']

    #get max, min temp
    temp = Weather_api.get_max_min_temp(x, y)
    max_temp = temp['max_temp'] + '℃'
    min_temp = temp['min_temp'] + '℃'

    # 전달할 데이터
    context = {
        'now_temp': now_temp,
        'sky_status': sky_status,
        'rain_pop': rain_pop,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'cities': cities,
        'addre' : json_addre,
        # 'STATN_NM' : simplejson.dumps(STATN_NM),
        'test' : simplejson.dumps(subway),
        'bus_name_ID': simplejson.dumps(bus_name_ID),
    }
    return render(request, 'index.html', context)



def address(request):
    print("i am address")
    print("값 넘어온다야", request.GET.get('city_select'))
    print("값 넘어온다야", request.GET.get('gu_select'))
    print("값 넘어온다야", request.GET.get('option1'))
    print("값 넘어온다야", request.GET.get('option2'))

    # selected_city -> search 'gu' in DB
    selected_city = request.GET.get('city_select')
    gu_list = MongoManager.get_gu_name(selected_city)

    # selected_gu -> search 'dong' in DB
    selected_gu = request.GET.get('gu_select')
    dong_list = MongoManager.get_dong_name(selected_city, selected_gu)

    test_db.city = request.GET.get('city_select')
    test_db.gu = request.GET.get('gu_select')

    print("db", test_db.city)
    print("db", test_db.gu)
    # print(gu_list)
    # print(dong_list)

    context = {
        "gu_list": gu_list,
        "dong_list": dong_list,
        "selected_city": selected_city,
        "seleted_dong": selected_gu,
    }

    return render(request, 'index.html', context)


def weather(request):
    return render(request, 'weather_index.html')


def transportaion(request):
    print("지하철 정보", request.GET)
    return render(request, 'transportaion_index.html')


def get_weather(request):
    print(request.GET)
    # wb -> data
    select_city = request.GET.get('city_select')
    select_gu = request.GET.get('gu_select')
    select_dong = request.GET.get('dong_select')
    print(select_city, select_gu, select_dong)


    # get XY
    xy_location = MongoManager.get_XY(select_city)
    x = xy_location['x']
    y = xy_location['y']

    # 0:temp 1:sky status 2:precipitation 3:rain pop
    now_temp = Weather_api.get_current_weather(x, y)

    # get max, min temp
    temp = Weather_api.get_max_min_temp(x, y)
    max_temp = temp['max_temp'] + '℃'
    min_temp = temp['min_temp'] + '℃'

    context = {
        "select_city": select_city,
        "select_gu": select_gu,
        "select_dong": select_dong,

        "now_temp" : now_temp[0] + '℃',
        "sky_status": now_temp[1],
        "rain_pop": now_temp[3] + '%',
        "max_temp": max_temp,
        "min_temp": min_temp
    }

    return render(request, 'submit_page.html', context)


