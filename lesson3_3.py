def interest(money,rate,years):
    for i in range(years):
        money=money*(1+rate)
    return money

money = 10000
rate = 0.055
years=5
sum=interest(money,rate,years)
print(sum)
lx=sum-money
print(lx)