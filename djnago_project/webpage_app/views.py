from urllib.request import urlopen
import xmltodict
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

# def index(request):
#     print("============================")
#     return render(request, 'index.html')

def index(request):
    global cal
    global title

    district_code = 1111051500
    url = f'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={district_code}'.format({}, district_code)
    xml_data = urlopen(url).read().decode('utf-8')
    json_data = xmltodict.parse(xml_data)
    json_weather = json_data['rss']['channel']['item']['description']['body']['data']

    weathers = [data for data in json_weather]
    tmp_list = []

    for key, value in weathers[0].items():
        tmp_list.append(value)
        print(key, value)
    cal = tmp_list[3] + ' 도'
    # cal = 2+2
    title = "기온"
    return render(request, 'index.html', {'title': title, 'cal':cal})

def weather(request):
    return render(request, 'weather index.html')

def transportaion(request):
    return render(request, 'transportaion index.html')