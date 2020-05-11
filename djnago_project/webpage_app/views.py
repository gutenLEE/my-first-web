from urllib.request import urlopen
import xmltodict
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar

# def index(request):
#     print("============================")
#     return render(request, 'index.html')

def index(request):
    global cal
    global title
    #날씨 data 호출
    district_code = 1111051500
    url = f'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={district_code}'.format({}, district_code)
    xml_data = urlopen(url).read().decode('utf-8')
    json_data = xmltodict.parse(xml_data)
    json_weather = json_data['rss']['channel']['item']['description']['body']['data']

    weathers = [data for data in json_weather]
    tmp_list = []

    # 현재시간 + 3시간의 날씨만 추출
    for key, value in weathers[0].items():
        tmp_list.append(value)
        print(key, value)

    # 현재기온, 하늘상태, 강수확률, 최저, 최고
    now_temp = tmp_list[3] + ' 도'
    max_temp = tmp_list[4]
    min_temp = tmp_list[5]
    sky_status = tmp_list[8]
    rain_pop = tmp_list[10] + ' %'


    return render(request, 'index.html', {'now_temp': now_temp,
                                          'sky_status': sky_status,
                                          'rain_pop': rain_pop,
                                          'max_temp': max_temp,
                                          'min_temp': min_temp
                                          })

def weather(request):
    return render(request, 'weather_index.html')

def transportaion(request):
    return render(request, 'transportaion index.html')


def get_weather(request):
    print(request.GET)
    print(request.POST)

    select_city = request.GET.get('city_select')
    select_gu = request.GET.get('gu_select')
    select_dong = request.GET.get('dong_select')
    print(select_city, select_gu, select_dong)
    context = {}
    return render(request, 'weather_index.html', context)

