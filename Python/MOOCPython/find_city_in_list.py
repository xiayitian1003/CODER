import openpyxl

city_file_path = "D:\\CODE\\workstation\\Document\\9.0\\cities.txt"
excel_path = "D:\\CODE\\workstation\\Document\\9.0\\find-city.xlsx"
book = openpyxl.load_workbook(excel_path)
sheet = book.worksheets[0]
write_sheet = book.create_sheet()

with open(city_file_path, encoding='utf-8') as f:
    whole_file = f.read()
    cnt = int(0)
    write_sheet.append(("ANS", "ANS"))
    for row in sheet.rows:
        cnt += 1
        city_info = (cnt, row[0].value, row[1].value)
        if (">" + str(row[0].value) + "<") not in whole_file:
            ans_row = city_info + ("name not found",)
            write_sheet.append(ans_row)
        book.save(filename=excel_path)
