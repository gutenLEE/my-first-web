

from urllib.parse import quote_plus
from urllib.parse import urlencode
from urllib.parse import unquote
from urllib.request import Request, urlopen

key = 'vzJIPq38c6Mw7Q5fmDYv4vFn1o5fMO2Ml4Z8u5fQMTZERE4iU8aXePUDLelmk8TYl7Iy3iRfebpeKqsvqMsxYQ%3D%3D'
decode_key = unquote(key)
url = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getCtyCodeList'
queryParams = '?' + urlencode({quote_plus('ServiceKey') : decode_key})
print(url+queryParams)
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)


# url = f'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getCtyCodeList?ServiceKey={key}'

