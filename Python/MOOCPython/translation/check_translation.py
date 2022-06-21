import openpyxl
from xml.dom.expatbuilder import TEXT_NODE
from xml.dom.minidom import parse, Node


def main():
    eng_excel_dir = "D:\\CODE\\workstation\\Document\\9.0\\9.0提翻译\\ENWorldcities.xlsx"
    book = openpyxl.load_workbook(eng_excel_dir)
    sheet = book.worksheets[1]
    city_lst = []
    for row in sheet.rows:
        city_lst.append(row[0].value)
    #
    # for item in city_lst:
    #     print(item)
    print("start check")
    #     <!--add by xiaolei.huang  start-->
    eng_xml_dir = "D:\\CODE\\workstation\\Document\\9.0\\9.0提翻译\\cities.xml"
    write_xml_path = "D:\\CODE\\workstation\\Document\\9.0\\9.0提翻译\\rightENcities.xml"
    dom = parse(write_xml_path)
    element_obj = dom.documentElement

    cities = element_obj.getElementsByTagName('string')
    cnt = int(1)
    print(sheet.rows)
    for city in cities:
        print(sheet[cnt][0].value)
        print(city)
        city.appendChild(dom.createTextNode(sheet[cnt][0].value))
        cnt += 1
        # print()
        # if city.hasChildNodes():
        #     for child in city.childNodes:
        #         remove_all_child(child)
        # print("done")

    with open(write_xml_path, 'w', encoding="utf-8") as f:
        dom.writexml(writer=f, indent='', newl='', addindent='', encoding='utf-8')


def remove_all_child(node):
    if node.hasChildNodes():
        for child in node.childNodes:
            remove_all_child(child)
        return remove_all_child(node)
    else:
        node.parentNode.removeChild(node)
        return


if __name__ == '__main__':
    main()
