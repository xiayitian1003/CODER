import openpyxl
from xythttprequest import pick_point_search_for_city
from xythttprequest import gaode_search_for_city

Path = "D:\\CODE\\workstation\\Document\\NewestTimeZone.xlsx"
book = openpyxl.load_workbook(Path)

sheet = book.worksheets[0]
write_sheet = book.create_sheet()
unfinished_city_sheet = book.create_sheet()
write_sheet.title = "answer_sheet"
unfinished_city_sheet.title = "unfinished"

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
        ans_row = (row[0].value, row[1].value, ans['lat'], ans['lon'], "", ans['display_name'])
        write_sheet.append(ans_row)
    else:
        print("%d times finish, ans of %s is None" % (cnt, row[0].value))
        ans_none_type = "city&country"
        ans = pick_point_search_for_city(row[0].value, None)
        if ans is None:
            print("city")
            ans_lat, ans_lon = "none", "none"
            ans_none_type = "city"
            ans_row = (row[0].value, row[1].value, ans_lat, ans_lon, ans_none_type, "none name")
            unfinished_ans = (cnt, row[0].value, row[1].value, ans_lat, ans_lon, ans_none_type, "none name")
        else:
            print("%3d %10s %10s %10s" % (cnt, row[0].value, row[1].value, row[2].value))
            ans_row = (row[0].value, row[1].value, ans['lat'], ans['lon'], ans_none_type, ans['display_name'])
            unfinished_ans = (
                cnt, row[0].value, row[1].value, ans['lat'], ans['lon'], ans_none_type, ans['display_name'])
        write_sheet.append(ans_row)
        unfinished_city_sheet.append(unfinished_ans)
    book.save(filename=Path)
