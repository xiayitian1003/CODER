from PythonXml import gen_index_city_dict
from xyt_excel import get_translate_city_list

chinese_dir = "D:\\CODE\\workstation\\Document\\9.0\\cities.txt"
eng_dir = "D:\\CODE\\workstation\\Document\\9.0\\eng_cities.xml"


def translated_city_list():
    translate_list = tuple(get_translate_city_list())
    print(translate_list)
    xml_index_city_dict = gen_index_city_dict(chinese_dir, "city-index")
    print(xml_index_city_dict)
    eng_city_dict = gen_index_city_dict(eng_dir, "index-city")
    ans_list = []
    for city_to_compare in translate_list:
        index = xml_index_city_dict[city_to_compare]
        eng_translation = eng_city_dict[index]
        ans_list.append(eng_translation)
    return ans_list


def main():
    print(translated_city_list())


if __name__ == '__main__':
    main()
