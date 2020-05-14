from urllib.request import urlopen

import xmltodict
from django.shortcuts import render

from .models import test_db
from .pymongoTEST import mongoManager


def index(request):
    global cal
    global title
    # 날씨 data 호출
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
        # print(key, value)

    # 현재기온, 하늘상태, 강수확률, 최저, 최고
    now_temp = tmp_list[3] + ' 도'
    max_temp = tmp_list[4]
    min_temp = tmp_list[5]
    sky_status = tmp_list[8]
    rain_pop = tmp_list[10] + ' %'


    # 도/시 리스트
    cities = mongoManager.cities

    # 구 리스트
    gu_list = mongoManager.get_gu_name('서울특별시')
    gu_list = ','.join([str(i) for i in gu_list])
    print(gu_list[2])





    context = {
        'now_temp': now_temp,
        'sky_status': sky_status,
        'rain_pop': rain_pop,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'gu_list': gu_list,
        'cities': cities,
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
    gu_list = mongoManager.get_gu_name(selected_city)

    # seleted_gu -> search 'dong' in DB
    seleted_gu = request.GET.get('gu_select')
    dong_list = mongoManager.get_dong_name(selected_city,seleted_gu)

    test_db.city = request.GET.get('city_select')
    test_db.gu = request.GET.get('gu_select')

    print("db", test_db.city)
    print("db", test_db.gu)
    # print(gu_list)
    # print(dong_list)

    context = {
        "gu_list": gu_list,
        "dong_list": dong_list,
        "selected_city" : selected_city,
        "seleted_dong" : seleted_gu,
    }

    return render(request, 'index.html', context)



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
    context = {
        "select_city": select_city,
        "select_gu": select_gu,
        "select_dong": select_dong,
    }

    return render(request, 'index2.html', context)

def index_submit(request):
    print(request.GET.getlist('city_select[]'))
    print(request.POST.getlist('city_select[]'))




def test(request):
    print(request.GET)
    print(request.POST)
    print("나는test views.py")
    gu_list = mongoManager.get_gu_name('서울특별시')
    city_list = mongoManager.get_dong_name('서울특별시', '서초구')

    context = {
        "data": "heoo",
        "dong test": "dong_test",
        "list": gu_list,
        "dong": city_list,

    }
    return render(request, 'test.html', context)


posts = [
    {
        'author': 'alex',
        'title': 'america',
        'content': 'thriller',
        'date_posted': '11/23'
    },
    {
        'author': 'mika',
        'title': 'german',
        'content': 'romance',
        'date_posted': '11/23'
    }

]


def get(request):
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def basee(request):
    return render(request, 'base.html')
