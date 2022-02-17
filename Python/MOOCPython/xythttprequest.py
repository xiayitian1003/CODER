import requests


def pick_point_search_for_city(cityname, countryname):
    forward_city_url = "https://api.pickpoint.io/v1/forward/"
    parmas = {'key': "4dhMZBJzyxPyEck7wJey", 'q': cityname, 'city': cityname, 'country': countryname,
              'accept-language': "zh-CN"}
    r = requests.get(forward_city_url, parmas)
    print(r.url)
    print(r.status_code)
    print(r.json())
    if len(r.json()) == 0:
        return None
    else:
        ans_dic = r.json()[0]
        print(ans_dic['lat'] + "," + ans_dic['lon'])
        return {'lat': float(ans_dic['lat']), 'lon': float(ans_dic['lon']), 'display_name': ans_dic['display_name']}


# 26.1551249, 50.5344606
def pick_point_reverse_geo_code(lat, lon):
    # https://restapi.amap.com/v3/geocode/regeo?output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all
    url = "https://api.pickpoint.io/v1/reverse/"
    pick_point_key = "4dhMZBJzyxPyEck7wJey"
    parmas = {'key': pick_point_key, 'lat': lat, 'lon': lon, 'accept-language': "zh-CN", 'namedetails': 1}
    r = requests.get(url, parmas)
    print(r.status_code)
    ans = r.json()
    print(ans)
    # return {'formatted_address': ans['regeocode']['formatted_address'],
    #         'city': ans['regeocode']['addressComponent']['city'],
    #         'country': ans['regeocode']['addressComponent']['country']}


def gaode_search_for_city(cityname, countryname):
    # ?address = 9, Madison Avenue, 曼哈顿, 纽约, 纽约州, 美国 & country = us & language = zh & key = < ⽤户的key >
    gaode_url = " https://restapi.amap.com/v3/geocode/geo"
    parmas = {'address': cityname, 'key': "f50480ce1dfb3fd6aa8634f067a559c4", 'country': countryname, 'language': "zh"}
    r = requests.get(gaode_url, parmas)
    print(r.url)
    print(r.status_code)
    print(r.json())


def gaode_reverse_geo_code(lon, lat):
    # https://restapi.amap.com/v3/geocode/regeo?output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all
    url = "https://restapi.amap.com/v3/geocode/regeo"
    gaode_key = "86959160eb68570d15ae3236db7aa989"
    parmas = {'location': str(lon) + "," + str(lat), 'key': gaode_key}
    r = requests.get(url, parmas)
    print(r.status_code)
    ans = r.json()
    print(ans)
    return {'formatted_address': ans['regeocode']['formatted_address'],
            'city': ans['regeocode']['addressComponent']['city'],
            'country': ans['regeocode']['addressComponent']['country']}


# gaode_reverse_geo_code(18.5509126, 4.3907153)
# gaode_search_for_city("巴林", "bh")
# pick_point_search_for_city("巴林", None)
# pick_point_reverse_geo_code(26.1551249, 50.5344606)
