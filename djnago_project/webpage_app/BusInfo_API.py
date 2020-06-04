import json
import urllib
from urllib.parse import quote_plus
from urllib.parse import urlencode
from urllib.parse import unquote
from urllib.request import Request, urlopen


key = 'vzJIPq38c6Mw7Q5fmDYv4vFn1o5fMO2Ml4Z8u5fQMTZERE4iU8aXePUDLelmk8TYl7Iy3iRfebpeKqsvqMsxYQ%3D%3D'

url = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getCtyCodeList'

import requests

def get_request_query(url, operation, serviceKey):
    import urllib.parse as urlparse
    # params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + '&' + 'serviceKey' + '=' + serviceKey
    return request_query


# 요청 URL과 오퍼레이션
URL = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService'
OPERATION = 'getCtyCodeList' # 국경일 + 공휴일 정보 조회 오퍼레이션

# 파라미터
SERVICEKEY = 'vzJIPq38c6Mw7Q5fmDYv4vFn1o5fMO2Ml4Z8u5fQMTZERE4iU8aXePUDLelmk8TYl7Iy3iRfebpeKqsvqMsxYQ%3D%3D'
# solYear  = '2018'  # 연도
# solMonth = '09'   # 월
# PARAMS = {'solYear':solYear, 'solMonth':solMonth}



import requests
api_key = "vzJIPq38c6Mw7Q5fmDYv4vFn1o5fMO2Ml4Z8u5fQMTZERE4iU8aXePUDLelmk8TYl7Iy3iRfebpeKqsvqMsxYQ%3D%3D"
api_key_decode = requests.utils.unquote(api_key)
parameters = {"ServiceKey":api_key_decode}
req = requests.get(url, params = parameters)
request = Request(url + parameters)
response_body = urlopen(request).read()
print(req)
print(response_body)



# request_query = get_request_query(URL, OPERATION, SERVICEKEY)
# print('request_query:', request_query)
# response = requests.get(url=request_query)
# print('status_code:' + str(response.status_code))
#
#
# if True == response.ok:
#     print(response.text)
#
# get_request_query(URL, OPERATION, SERVICEKEY)
