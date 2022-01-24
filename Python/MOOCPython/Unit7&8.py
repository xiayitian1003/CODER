# d = dict(name='Gumby', age=42, height=1.76)
# print(d.items())

#字典用来kv快速查找，集合用来快速判断包含关系（二者的操作都是常数级，集合的in快于list与数据规模无关）
#集合无序，字典3.5以后有顺序，为元素添加顺序

# import sys
# import os
#     args = sys.argv[0]

with open("SteveJobs.txt", "r", encoding="utf-8") as f:
    read_file = f.readlines()
for i in read_file:
    print(i)




