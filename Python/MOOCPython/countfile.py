import sys
import re


def countfile(filename, words):
    try:
        f = open(filename, "r", encoding="utf-8")
    except Exception as e:
        print(e)
        return 0
    txt = f.read()
    f.close()
    splitChars = set([])
    for c in txt:
        if not ("a" <= c <= "z" or "A" <= c <= "Z"):
            splitChars.add(c)
    splitStr = ""
    for c in splitChars:
        if c in {'.', '?', '!', '"', "'", '(', ')', '|', '*', '$', '\\', '[', ']', '^', '{', '}'}:
            splitStr += "\\" + c + "|"
        else:
            splitStr += c + "|"
    splitStr += " "
    print(splitStr)
    # print(txt)
    lst = re.split(splitStr, txt)
    # print(lst)
    for x in lst:
        if x == "":
            continue
        lx = x.lower()
        if lx in words:
            words[lx] += 1
        else:
            words[lx] = 1
    return 1


result = {}
if countfile(sys.argv[1], result) == 0:
    exit()
lst = list(result.items())
lst.sort(key=lambda x: -x[1])
with open("statistics.txt", "w", encoding="utf-8") as ans:
    for i in lst:
        ans.write("%s\t%d\n" % (i[0], i[1]))
