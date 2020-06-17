import requests
import json


def getCountries(s, p):
    url = "https://jsonmock.hackerrank.com/api/countries/search?name="
    url += s
    response = requests.get(url)
    countdata = json.loads(response.text)
    countrylist = []
    for k, v in countdata.items():
        if k == "data":
            countrylist = v
            break
    for i in countrylist:
        print(i)


try:
    _s = str(input())
except:
    _s = None
_p = int(input())
getCountries(_s, _p)
