import openpyxl
from xythttprequest import pick_point_search_for_city
from xythttprequest import gaode_search_for_city

Path = "D:\\CODE\\workstation\\Document\\NewestTimeZone.xlsx"
book = openpyxl.load_workbook(Path)
sheet = book.worksheets[0]
write_sheet = book.worksheets[1]
print(sheet.title)
print(write_sheet.title)
print(sheet.min_row, sheet.max_row)
print(sheet.min_column, sheet.max_column)
print(write_sheet.min_row, write_sheet.max_row)
print(write_sheet.min_column, write_sheet.max_column)
cnt = int(0)
for row in sheet.rows:
    cnt += 1
    print("Start search %s in %d times" % (row[0].value, cnt))
    ans = pick_point_search_for_city(row[0].value, row[1].value)
    if ans is not None:
        print("%d times finish, ans of %s is %.3f, %.3f" % (cnt, row[0].value, ans['lat'], ans['lon']))
        ans_row = (row[0].value, row[1].value, ans['lat'], ans['lon'])
        write_sheet.append(ans_row)
    else:
        print("%d times finish, ans of %s is None" % (cnt, row[0].value))
        ans_none_type = "answer in city&country not found"
        if pick_point_search_for_city(row[0].value, None) is None:
            ans_lat, ans_lon = "none", "none"
            ans_none_type = "answer in only city not found"
            ans_row = (row[0].value, row[1].value, ans_lat, ans_lon, ans['display_name'], ans_none_type)
        else:
            print("%3d %10s %10s %10s" % (cnt, row[0].value, row[1].value, row[2].value))
            ans_row = (row[0].value, row[1].value, ans['lat'], ans['lon'], ans['display_name'], ans_none_type)
            write_sheet.append(ans_row)
    book.save(filename="D:\\CODE\\workstation\\Document\\NewestTimeZone.xlsx")
