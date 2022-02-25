from xml.dom.expatbuilder import TEXT_NODE
from xml.dom.minidom import parse, Node
import openpyxl

# from xyt_excel import get_excel_city_set, get_translate_city_list

chinese_dir = "D:\\CODE\\workstation\\Document\\9.0\\cities.xml"


def get_xml_list_by_root(dir):
    dom = parse(dir)
    element_obj = dom.documentElement
    return element_obj


def get_index_type_child_node(parent_node, node_type, index):
    child_list = parent_node.childNodes
    serial_num = 0
    for child in child_list:
        if child.nodeType == node_type:
            serial_num += 1
            if serial_num == index:
                return child


def find_excel_differences():
    # dir = "D:\\CODE\\workstation\\TranssionDeskClock\\TranssionDeskClock9.0\\res\\values-zh-rCN\\cities.xml"
    element_obj = get_xml_list_by_root(chinese_dir)
    cities = element_obj.getElementsByTagName('string')
    cnt = int(0)
    city_set = set()
    for city in cities:
        cnt += 1
        city_name = get_index_type_child_node(city, TEXT_NODE, 2).data
        if city_name in city_set:
            print(city_name)
        else:
            city_set.add(city_name)
    excel_set = get_excel_city_set()

    print(city_set - excel_set)
    print(city_set.difference(excel_set))


def gen_index_city_dict(xml_dir, order):
    element_obj = get_xml_list_by_root(xml_dir)

    cities = element_obj.getElementsByTagName('string')
    city_index_dict = {}
    if order == "city-index":
        for city in cities:
            city_name = get_index_type_child_node(city, TEXT_NODE, 2).data
            city_index_dict[city_name] = city.getAttribute("name")
            # print(city.getAttribute("name"))
    elif order == "index-city":
        for city in cities:
            city_name = get_index_type_child_node(city, TEXT_NODE, 2).data
            city_index_dict[city.getAttribute("name")] = city_name
    print(len(city_index_dict))
    return city_index_dict


# def insert_after(node):
#     if node.nextSibling is None:

# def connect_string_geoinfo(xml_node, geo_info):
#     # 遍历xml字符串，检索excel中对应条目。
#     #     传入字符串信息，返回excel中的经纬国家信息
#     #     元素节点，文本节点插入，字符串拼接

def is_timezone_node(node):
    ans = False
    if node.nodeType == Node.ELEMENT_NODE:
        if node.getAttribute("id") is not None:
            if node.getAttribute("id").upper() == "TIMEZONE":
                ans = True
    return ans


def add_geo_node(dom, city, country_node, lat_lon_node):
    spearator_node = dom.createTextNode("|")
    for child in city.childNodes:
        if is_timezone_node(child):
            next = child.nextSibling
            if next is not None:
                city.insertBefore(spearator_node, next)
                city.insertBefore(country_node, next)
                city.insertBefore(lat_lon_node, next)
            else:
                city.appendChild(spearator_node)
                city.appendChild(country_node)
                city.appendChild(lat_lon_node)


def add_country_geo_info(dom, city, country, lat, lon):
    lat_lon = "|" + str(lat) + "|" + str(lon)
    country_text, lat_lon_text = dom.createTextNode(country), dom.createTextNode(lat_lon)
    country_node, lat_lon_node = dom.createElement("xliff:g"), dom.createElement("xliff:g")
    country_node.setAttribute("id", "country")
    lat_lon_node.setAttribute("id", "lat_lon")
    country_node.appendChild(country_text)
    lat_lon_node.appendChild(lat_lon_text)
    # print(country_node.tagName, country_node.prefix, country_node.localName)
    add_geo_node(dom, city, country_node, lat_lon_node)


def print_city_node_info(city):
    print(city)
    for child in city.childNodes:
        print(child, end=": ")
        if child.childNodes is not None:
            for i in child.childNodes:
                print(i, end="  ")
        print("next child")
    print("next city")


def is_separator_node(node):
    ans = False
    if node.nodeType == Node.ELEMENT_NODE:
        if node.getAttribute("id") is not None:
            if node.getAttribute("id").upper() == "SEPARATOR":
                ans = True
    return ans


def get_city_excel(data):
    excel_dir = "D:\\CODE\\workstation\\Document\\9.0\\字符串拼接\\365-cities-v1.0.xlsx"
    book = openpyxl.load_workbook(excel_dir)
    info_sheet = book.worksheets[0]
    for row in info_sheet.rows:
        if row[0].value == data:
            if row[1].value is not None:
                return {'country': row[1].value, 'lat': row[3].value, 'lon': row[4].value}
            else:
                return {'country': "", 'lat': row[3].value, 'lon': row[4].value}


def main():
    folder_path = "D:\\CODE\\workstation\\Document\\9.0\\字符串拼接\\"
    test_xml, correct_cities = "XML-string-connect.xml", "cities.xml"
    city_xml_dir, write_xml_path = folder_path + correct_cities, folder_path + "new-XML-string-connect.xml"
    dom = parse(city_xml_dir)
    file_object = dom.documentElement
    cities = file_object.getElementsByTagName('string')
    for city in cities:
        for child in city.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                if child.getAttribute("id").upper() == "SEPARATOR":
                    print(child.nextSibling.data, end=" ")
                    geo_info = get_city_excel(child.nextSibling.data)
                    print(geo_info['country'], geo_info['lat'], geo_info['lon'])
                    add_country_geo_info(dom, city, geo_info['country'], geo_info['lat'], geo_info['lon'])
        # country, lat, lon = "中国", "1.111", "4.222"

    # for city in file_object.getElementsByTagName('string'):
    #     print_city_node_info(city)

    with open(write_xml_path, 'w', encoding="utf-8") as f:
        dom.writexml(writer=f, indent='', newl='', addindent='', encoding='utf-8')
    # print(child.nodeName, child.prefix, child.localName)
    # if child.nodeType == Node.ELEMENT_NODE:
    #     print(child, child.tagName, end="|")
    # print()
    # excel_dir = ""

    # gen_index_city_dict()
    # element_obj = get_xml_list_by_root(chinese_dir)
    # xliff_g_list = element_obj.getElementsByTagName('xliff:g')
    # print(xliff_g_list)
    # for xliff_g in xliff_g_list:
    #     print(xliff_g, xliff_g.nextSibling, xliff_g.parentNode, xliff_g.childNodes)
    # for city in cities:
    #     print(city.namespaceURI)
    # print(city.attributes.values())
    # print(city.childNodes[2])
    # print(city.childNodes[1].prefix, city.childNodes[1].localName, city.childNodes[1].nodeName)
    # print(city.nodeValue, city.nodeName, city.localName)


if __name__ == '__main__':
    main()
