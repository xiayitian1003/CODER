from xml.dom.expatbuilder import TEXT_NODE
from xml.dom.minidom import parse, Node
import openpyxl

folder_path = "D:\\CODE\\workstation\\Document\\9.0\\9.0提翻译\\"


def main():
    cities_file, excel_file = folder_path + "城市字符串提翻译.txt", folder_path + "translation.xlsx"
    book = openpyxl.load_workbook(excel_file)
    sheet = book.worksheets[0]
    with open(cities_file, 'r', encoding="utf-8") as f:
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            # print line,                 # 在 Python 2中，后面跟 ',' 将忽略换行符
            print(line.rstrip())  # 在 Python 3中使用
            sheet.append((line.rstrip(),))
            line = f.readline()
    book.save(filename=excel_file)


if __name__ == '__main__':
    main()
