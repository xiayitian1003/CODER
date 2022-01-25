import openpyxl

Path = "D:\\CODE\\workstation\\Document\\NewestTimeZone.xlsx"
book = openpyxl.load_workbook(Path)
sheet = book.worksheets[0]
print(sheet.title)
print(sheet.min_row, sheet.max_row)
print(sheet.min_column, sheet.max_column)
for row in sheet.rows:
    print("%s\t%s\t%s" % (row[0].value, row[1].value, row[2].value))
