# -*- coding: utf-8 -*-
import datetime
from pprint import pprint
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import xmltodict
import json
import pymongo
from pymongo import MongoClient
import datetime
import calendar
import time

info_set = []


def realtime_sub_Info(a, b):
    station = a
    print(a)
    line = b
    # station = name
    key = '546a717361626e6d39374c64714b74'
    station_NM = quote(station)

    url = f'http://swopenapi.seoul.go.kr/api/subway/{key}/xml/realtimeStationArrival/0/20/{station_NM}'
    print(url)
    parse_url = url.format(key, station_NM)
    request = urlopen(parse_url)
    data = request.read().decode('utf8')
    json_data = json.loads(json.dumps(xmltodict.parse(data)))
    result = json_data['realtimeStationArrival']['row']
    pprint(result)
    return result


client = MongoClient('localhost', 27017)
db = client['test_db']
collection_currency = db['subwayCode']

# with open('subway_code.json',encoding='UTF8') as f:
#     file_data = json.load(f)

# collection_currency.insert_one(file_data)
# client.close()

line_num = []
data = collection_currency.find({})
for data in collection_currency.find({}):
    re_data = data

re_data = re_data['DATA']
for val in re_data:
    a = val['line_num']
    if a not in line_num:
        line_num.append(a)
line_num = sorted(line_num)

parse_station = []
for line in line_num:
    for val in re_data:
        if line == val['line_num']:
            a = val['station_nm']
            b = line
            c = val['station_cd']
            d = val['fr_code']
            parse_station.append([a, b, c, d])


##########################################################################


def timeTable(code, in_out):
    client = MongoClient('localhost', 27017)
    db = client['test_db']
    collection = db['Subway_collection']
    myquery = {'station_code': code}
    inout = {in_out: True}
    aa = collection.find_one(myquery, inout)
    print(aa[in_out])
    return aa[in_out]


class Timetable:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['test_db']
        self.collection = db['Subway_collection']

    def getIndays(self, code):

        myquery = {'station_code': code}
        timeData = self.collection.find_one(myquery, {'in_days': True})
        return timeData['in_days']

    def getOutdays(self, code):
        myquery = {'station_code': code}
        timeData = self.collection.find_one(myquery, {'out_Days': True})
        return timeData['out_Days']

    def getInSat(self, code):
        myquery = {'station_code': code}
        timeData = self.collection.find_one(myquery, {'in_Sat': True})
        return timeData['in_Sat']

    def getInWeekend(self, code):
        myquery = {'station_code': code}
        timeData = self.collection.find_one(myquery, {'in_Weekend': True})
        return timeData['in_Weekend']

    def getOutSat(self, code):
        myquery = {'station_code': code}
        timeData = self.collection.find_one(myquery, {'out_Sat': True})
        return timeData['out_Sat']

    def getOutWeekend(self, code):
        myquery = {'station_code': code}
        timeData = self.collection.find_one(myquery, {'out_Weekend': True})
        return timeData['out_Weekend']


# 서울시 역코드로 지하철역별 열차 도착 정보 검색 (역명포함)
# 평일:1, 토요일:2, 휴일/일요일:3
# 상행,내선:1, 하행,외선:2
# (G:일반(general) D: 급행(direct))

# def get_timeTable(code, week_tag, inout_tag):
#     key = '546a717361626e6d39374c64714b74'
#     # code = '0311'
#     url = f'http://openAPI.seoul.go.kr:8088/{key}/json/SearchSTNTimeTableByIDService/1/500/{code}/{week_tag}/{inout_tag}/'
#     parse_url = url.format(key, code)
#     request = urlopen(parse_url)
#     data = request.read().decode('utf8')
#     json_data = json.loads(data)
#     time_table = json_data['SearchSTNTimeTableByIDService']['row']
#
#     # 역 시간표 리스트
#     timeStrList = []
#     test = []
#     for time in time_table:
#         timeStrList.append(time['ARRIVETIME'])
#         a = time['ARRIVETIME']
#         b = time['SUBWAYSNAME']
#         c = time['SUBWAYENAME']
#         d = time['EXPRESS_YN']
#
#         test.append([a, b, c, d])
#
#     return test


def addsub_minutes(UserTimeStr, bool):
    """timeStr parameter is user input time"""
    Thistime = datetime.datetime.strptime(UserTimeStr, '%H:%M:%S')

    if bool == 1:
        after = Thistime + datetime.timedelta(minutes=15)
    else:
        after = Thistime - datetime.timedelta(minutes=15)

    time = after.strftime('%H:%M:%S')
    hour = int(time[0:2])
    minutes = int(time[3:5])
    sec = int(time[6:8])

    return hour, minutes, sec


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]
       x is user input time"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def timetable_in_range(UserTimeStr, test):
    timeStr_result = []
    for timeStr in test:
        hour = int(timeStr[0][0:2])
        minutes = int(timeStr[0][3:5])
        sec = int(timeStr[0][6:8])

        if hour == 24 or hour == 25:
            hour = 0

        after = addsub_minutes(UserTimeStr, bool=1)
        before = addsub_minutes(UserTimeStr, bool=0)

        start = datetime.time(before[0], before[1], before[2])
        end = datetime.time(after[0], after[1], after[2])
        result = time_in_range(start, end, datetime.time(hour, minutes, sec))

        if result is True:
            timeStr_result.append(timeStr)

    return timeStr_result

# UserTimeStr = "22:55:00"
# timeStrList = timeTable(code='0311', in_out='in_days')
# aa = timetable_in_range(UserTimeStr, timeStrList)

# with open('station.csv', encoding='utf-8-sig') as f:
#     file_data = json.load(f)
# collection_currency.insert_one(file_data)
# client.close()


# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
#
# now = datetime.datetime.now()
# my_time_string = "23:59:60"
# my_time_string = now.strftime("%Y-%m-%d") + " " + my_time_string # I am supposing the date must be the same as now
# my_time = time.strptime(my_time_string, "%Y-%m-%d %H:%M:%S")
# my_datetime = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(my_time))
# if (now > my_datetime):
#     print("Foo")


# # 첫차, 막차 정보요
# station = '왕십리'
# key = '546a717361626e6d39374c64714b74'
# station_NM = quote(station)
# url = f'http://swopenAPI.seoul.go.kr/api/subway/{key}/json/firstLastTimetable/0/5/{station_NM}'
# parse_url = url.format(key, station_NM)
# request = urlopen(parse_url)
# data = request.read().decode('utf8')
# json_data = json.loads(data)
#
# data_set = json_data['timeTableList']
#
# up_in = []
# down_out = []
# for data in data_set:
#     if data['statnNm'] == '왕십리' and data['subwayId'] == '1002':
#         if data['updnLine'] == '0':
#             a = data['weekendTranHour']
#             b = data['subwayename']
#             c = data['expressyn']
#             set = [a,b,c]
#             up_in.append(set)
#
#         elif data['updnLine'] == '1':
#             a = data['weekendTranHour']
#             b = data['subwayename']
#             c = data['expressyn']
#             set = [a, b, c]
#             down_out.append(set)
# print(up_in)
# print(down_out)
