def printinfo(arg1,*vartuple):
    print("输出：")
    print (arg1)
    for var in vartuple:
        print(var)
    return;

printinfo(15);
printinfo(75,65,55);

