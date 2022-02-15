import requests


def search_for_city(cityname, countryname):
    forward_city_url = "https://api.pickpoint.io/v1/forward/"
    parmas = {'key': "4dhMZBJzyxPyEck7wJey", 'city': cityname}
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
        # city_bounding = list(map(float, ans_dic['boundingbox']))
        # print("%.6f, %.6f" % (city_bounding[0], city_bounding[2]))
        # print("%.6f, %.6f" % (city_bounding[1], city_bounding[3]))
        # print((city_bounding[0] + city_bounding[1]) / 2, (city_bounding[2] + city_bounding[3]) / 2)


search_for_city("巴林", None)
