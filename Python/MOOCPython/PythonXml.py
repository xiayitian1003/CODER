from xml.dom.expatbuilder import TEXT_NODE
from xml.dom.minidom import parse

# from xyt_excel import get_excel_city_set, get_translate_city_list

chinese_dir = "D:\\CODE\\workstation\\Document\\9.0\\cities.txt"


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

# def is_timezone_node(node):
#     ans = False
#     if node.hasAttributes("id") and (node.getAttribute("id") == "TIMEZONE"):
#         node.parentNode.appChild()


def main():
    city_xml_dir = "D:\\CODE\\workstation\\Document\\9.0\\字符串拼接\\XML-string-connect.xml"
    file_object = get_xml_list_by_root(city_xml_dir)
    cities = file_object.getElementsByTagName('string')
    for city in cities:
        # print(city.nodeValue)
        for child in city.childNodes:
            # print(type(child.attributes))
            print(child, end="")
        print()
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
