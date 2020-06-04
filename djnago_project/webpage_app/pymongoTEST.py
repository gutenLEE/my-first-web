import pymongo


class MongoManager:
    global xy
    _instance = None
    client = pymongo.MongoClient('localhost', 27017)
    collection = client['test_db']['kor_district_code']
    second = collection.find({}, {"1단계": True, '2단계': True, '3단계': True})

    def get_XY(city, gu, dong):

        client = pymongo.MongoClient('localhost', 27017)
        collection = client['test_db']['kor_district_code']

        momo = collection.find({"1단계": city, '2단계': gu, '3단계': dong}, {"격자 X": True, '격자 Y': True})
        for xy in momo:
            print(xy)

        return {'x': xy['격자 X'], 'y': xy['격자 Y']}

    #도시, 구, 동 리스트
    city_gu_dong = []
    for d in second:
        null = []
        a = d['1단계']
        b = d['2단계']
        c = d['3단계']
        null.append(a)
        null.append(b)
        null.append(c)

        city_gu_dong.append(null)

    # 도시만 추출
    city = []
    get_city = collection.find({}, {"1단계": True})
    for get in get_city:
        city.append(get['1단계'])

    #도시 리스트
    cities = list(set(city))

