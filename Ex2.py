count=0
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        for k in [1,2,3,4]:
            if i!=j and j!=k and i!=k:
                count+=1
                print(f'{i}{j}{k}',end=" ")
print(f'一共有{count}个')
