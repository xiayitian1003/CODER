import requests


def pick_point_search_for_city(cityname, countryname):
    forward_city_url = "https://api.pickpoint.io/v1/forward/"
    parmas = {'key': "4dhMZBJzyxPyEck7wJey", 'city': cityname, 'country': countryname}
    r = requests.get(forward_city_url, parmas)
    print(r.url)
    print(r.status_code)
    print(r.json())
    if len(r.json()) == 0:
        return None
    else:
        ans_dic = r.json()[0]
        print(ans_dic['lat'] + "," + ans_dic['lon'])
        return {'lat': float(ans_dic['lat']), 'lon': float(ans_dic['lon'])}


def gaode_search_for_city(cityname, countryname):
    # ?address = 9, Madison Avenue, 曼哈顿, 纽约, 纽约州, 美国 & country = us & language = zh & key = < ⽤户的key >
    gaode_url = " https://restapi.amap.com/v3/geocode/geo"
    parmas = {'address': cityname, 'key': "f50480ce1dfb3fd6aa8634f067a559c4", 'country': countryname, 'language': "zh"}
    r = requests.get(gaode_url, parmas)
    print(r.url)
    print(r.status_code)
    print(r.json())


# gaode_search_for_city("巴林", "bh")
# pick_point_search_for_city("巴林", "巴林")
