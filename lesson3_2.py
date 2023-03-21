
py={"赵一","钱二","孙三","李四","周五","吴六"}
c={"王二","郑一","张三","李四","周五","吴六"}
print("选择python的同学有",py)
print("选择c的同学有",c)
print("选择python和c语言的同学有：",py|c)
print("只选择py不选c的同学",py-c)
print("只选择c不选择py的有",c-py)
py.add("冯七")
py.add("陈八")
print("选择python的同学有",py)