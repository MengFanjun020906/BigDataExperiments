class Fruit:
    def __init__(self, fruit_name, fruit_price):
        self.fruit_name = fruit_name
        self.fruit_price = fruit_price
        self.number_sell = 0

    def describe_fruit(self):
        print("水果名: ", self.fruit_name)
        print("价格: ", self.fruit_price)

    def number_fruit(self):
        print("仓库的水果很充足")

    def set_number_sell(self, num):
        self.number_sell = num

# 创建一个fruit实例
fruit = Fruit("苹果", 3.99)

# 调用fruit的方法
fruit.describe_fruit()
fruit.number_fruit()

# 添加一个number_sell属性并打印它
print("水果卖了: ", fruit.number_sell)

# 修改number_sell属性的值并再次打印它
fruit.number_sell = 10
print("水果卖了: ", fruit.number_sell)

# 调用set_number_sell方法并打印
fruit.set_number_sell(5)
print("每次出售限量: ", fruit.number_sell)
