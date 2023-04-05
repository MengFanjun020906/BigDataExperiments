class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_cat = Cat("tommy", 3)
print("My cat's name is " + my_cat.name.title())
print("My cat is " + str(my_cat.age) + " years old")


