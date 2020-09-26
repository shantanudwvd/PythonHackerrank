import requests
import json


def getNumberOfMovies(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title={0}".format(key=substr)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data = payload)
    Data = json.loads(response.text.encode('utf8'))
    return Data["total"]


substr = input("Enter the string: ")
res = getNumberOfMovies(substr)


