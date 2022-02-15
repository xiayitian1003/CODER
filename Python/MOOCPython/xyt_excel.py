import openpyxl
from xythttprequest import search_for_city

Path = "D:\\CODE\\workstation\\Document\\NewestTimeZone.xlsx"
book = openpyxl.load_workbook(Path)
sheet = book.worksheets[0]
print(sheet.title)
print(sheet.min_row, sheet.max_row)
print(sheet.min_column, sheet.max_column)
cnt = int(0)
for row in sheet.rows:
        cnt += 1
        print("Start search %s in %d times" % (row[0].value, cnt))
        ans = search_for_city(row[0].value, row[1].value)
        if ans is not None:
            print("%d times finish, ans of %s is %.3f, %.3f" % (cnt, row[0].value, ans['lat'], ans['lon']))
        else:
            print("%d times finish, ans of %s is None" % (cnt, row[0].value))
            # if row[1].value is None:
            #     print("%3d %10s %10s %10s" % (cnt, row[0].value, row[1].value, row[2].value))