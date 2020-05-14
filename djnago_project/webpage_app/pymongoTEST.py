import pymongo
from pymongo import MongoClient


class mongoManager:
    _instance = None
    client = pymongo.MongoClient('localhost', 27017)
    collection = client['test_db']['kor_district_code']

    qestion = "==========================================="

    # 도시만 추출
    city = []
    get_city = collection.find({}, {"1단계": True})
    for get in get_city:
        city.append(get['1단계'])
    #도시 리스트
    cities = list(set(city))



    def get_gu_name(city_name):
        client = pymongo.MongoClient('localhost', 27017)
        collection = client['test_db']['kor_district_code']
        get_dong = collection.find({'1단계': city_name})

        gu = []
        for a in get_dong:
            gu.append(a['2단계'])
        gu = list(filter(lambda v: v, gu))
        gu_list = set(gu)
        gu_list = list(gu_list)
        return gu_list


    def get_dong_name(city_name, gu_name):
        client = pymongo.MongoClient('localhost', 27017)
        collection = client['test_db']['kor_district_code']
        second_district = collection.find({'1단계': city_name, '2단계': gu_name}, {'3단계': True})

        dong_list = []
        for gu in second_district:
            dong_list.append(gu['3단계'])
        dong_list = list(filter(lambda v: v, dong_list))
        dong_list = list(set(dong_list))

        return dong_list

mongoManager.get_gu_name('서울특별시')

# second = collection.find({"1단계": '서울특별시', '2단계': '종로구', '3단계': '평창동'},{'격자 X': True, '격자 Y':True})
client = pymongo.MongoClient('localhost', 27017)
collection = client['test_db']['kor_district_code']

city = []
get_city = collection.find({}, {"1단계": True})
for get in get_city:
    city.append(get['1단계'])
# 도시 리스트
cities = list(set(city))
print(cities)

gu = []
get_dong = collection.find({"1단계":"서울특별시"},{'2단계': True})
for a in get_dong:
    gu.append(a['2단계'])
gu_list = set(gu)
gu_list = list(gu_list)
print(gu_list)

"""
second = collection.find({},{"1단계": True, '2단계': True})
first_district = []
second_district = []
third_district = []

for seco in second:
    first_district.append(seco['1단계'])
city_name = list(set(first_district))

def get_dong_name(city,dong):
    second_district = collection.find({'1단계': city, '2단계':dong}, {'3단계': True})
    for gu in second_district:
        print(gu['3단계'])

get_dong_name(city='서울특별시', dong='서초구')

"""


# dong_list = []
# for dong in get_dong:
#     dong_list.append([dong['격자 X'], dong['격자 Y']])
# dong_list = list(filter(lambda v: v, dong_list))
#
# print(dong_list)
#


# client = pymongo.MongoClient('localhost', 27017)
# collection = client['test_db']['kor_district_code']
# get_dong = collection.find({'1단계': city_name, '2단계': gu_name})
#
# XY_list = []
# for dong in get_dong:
#     XY_list.append([dong['3단계'], dong['격자 X'], dong['격자 Y']])
# XY_list = list(filter(lambda v: v, XY_list))
#
# print(XY_list)
