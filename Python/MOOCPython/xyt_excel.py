import openpyxl
from xythttprequest import pick_point_search_for_city, pick_point_reverse_geo_code
from xythttprequest import gaode_reverse_geo_code
from xythttprequest import gaode_search_for_city
from decimal import Decimal

# Path = "D:\\CODE\\workstation\\Document\\NewestTimeZone.xlsx"
# Path = "D:\\CODE\\workstation\\Document\\9.0\\TimeZone-Version-2.0.xlsx"
# Path = "D:\\CODE\\workstation\\Document\\9.0\\v2.0NotFound.xlsx"
# Path = "D:\\CODE\\workstation\\Document\\9.0\\TimeZone-Version-2.0-Reverse.xlsx"


# print(write_sheet.title)
# print(write_sheet.min_row, write_sheet.max_row)
# print(write_sheet.min_column, write_sheet.max_column)


def round_3_float(decimal_num):
    decimal_num = str(decimal_num)
    return Decimal(decimal_num).quantize(Decimal('0.000'))


def get_cell_value(cell):
    return cell.value


# def search_all_city():
#     sheet = book.worksheets[0]
#     print(sheet.title)
#     print(sheet.min_row, sheet.max_row)
#     print(sheet.min_column, sheet.max_column)
#     unfinished_city_sheet = book.create_sheet()
#     cnt = int(0)
#     for row in sheet.rows:
#         cnt += 1
#         print("Start search %s in %d times" % (row[0].value, cnt))
#         city_info = (row[0].value, row[1].value)
#         ans = pick_point_search_for_city(row[0].value, row[1].value)
#         ans_row = city_info
#         if ans is not None:
#             print("%d times finish, ans of %s is %.3f, %.3f" % (cnt, row[0].value, ans['lat'], ans['lon']))
#             ans_row += (round_3_float(ans['lat']), round_3_float(ans['lon']), "", ans['display_name'])
#             write_sheet.append(ans_row)
#         else:
#             print("%d times finish, ans of %s is None" % (cnt, row[0].value))
#             ans_none_type = "city&country"
#             ans = pick_point_search_for_city(row[0].value, None)
#             unfinished_ans = (cnt,) + city_info
#             if ans is not None:
#                 print("%3d %10s %10s %10s" % (cnt, row[0].value, row[1].value, row[2].value))
#                 ans_row += (ans['lat'], ans['lon'], ans_none_type, ans['display_name'])
#                 unfinished_ans += (ans['lat'], ans['lon'], ans_none_type, ans['display_name'])
#             else:
#                 print("city")
#                 ans_lat, ans_lon = "none", "none"
#                 ans_none_type = "city"
#                 ans_row += (ans_lat, ans_lon, ans_none_type, "none name")
#                 unfinished_ans += (ans_lat, ans_lon, ans_none_type, "none name")
#
#             write_sheet.append(ans_row)
#             unfinished_city_sheet.append(unfinished_ans)
#         book.save(filename=Path)
#
#
# def search_by_reverse():
#     sheet = book.worksheets[0]
#     print(sheet.title)
#     print(sheet.min_row, sheet.max_row)
#     print(sheet.min_column, sheet.max_column)
#     cnt = int(163)
#     for row in sheet[164: 365]:
#         cnt += 1
#         print("Start search %s in %d times" % (row[0].value, cnt))
#         print("coordinate is -- lat: %s, lon: %s" % (row[2].value, row[3].value))
#
#         # print(row, row[0].col_idx, row[0].column, row[0].column_letter, row[0].coordinate, row[0].row)
#         ans = pick_point_reverse_geo_code(row[2].value, row[3].value)
#         print(ans)
#
#         ans_row = (cnt,)
#         ans_row = ans_row + tuple(map(get_cell_value, row[0: 4]))
#         print(ans_row)
#         plan_to_add = [ans['city'], ans['country'], ans['country_code']]
#         print(type([ans['city'], ans['country'], ans['country_code']]))
#         for item in plan_to_add:
#             if item is not None and len(item) > 0:
#                 ans_row += (item,)
#         ans_row += (row[5].value,)
#
#         write_sheet.append(ans_row)
#         book.save(filename=Path)


def get_final_wrong_list():
    final_wrong_path = "D:\\CODE\\workstation\\Document\\9.0\\FinalWrongTimeZone.xlsx"
    book = openpyxl.load_workbook(final_wrong_path)

    sheet = book.worksheets[0]
    final_wrong_sheet = book.create_sheet()

    cnt = int(0)
    num = cnt
    for row in sheet.rows:
        cnt += 1
        print(cnt)
        if str(row[5].value) == "1":
            num += 1
            ans_row = tuple(map(get_cell_value, row))
            final_wrong_sheet.append(ans_row)
    print(num)
    book.save(filename=final_wrong_path)


get_final_wrong_list()
# search_by_reverse()
# search_all_city()
