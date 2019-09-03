# -*- coding: utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
import json
import xmltodict

API_KEY = 'API_KEY'
URL = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?ServiceKey='
year = 2019
pageNo = 1
numOfRows = 100

URL = URL + API_KEY + '&'

params = urlencode({quote_plus('year') : year, quote_plus('pageNo') : pageNo, quote_plus('numOfRows') : numOfRows})
request = Request(URL + params)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read().decode('utf-8')
parsed = xmltodict.parse(response_body)

# with open('dust_request.json', 'w', encoding='UTF-8') as f:
#     json.dump(parsed, f, indent=4, ensure_ascii=False)


def recent_alert():
    return parsed['response']['body']['items']['item'][0]['districtName']


