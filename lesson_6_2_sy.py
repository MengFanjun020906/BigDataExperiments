class BankAccount:
    def __init__(self, account_name, balance, interest_rate):
        self.account_name = account_name
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("error")

    def annual_interest(self):
        return self.balance * self.interest_rate

# 创建银行帐户
my_account = BankAccount('888666', 35000, 0.03)

# 存入5000
my_account.deposit(5000)

# 取出12000
my_account.withdraw(12000)

# 打印账户信息，余额，年利率和年息
print('账户名:', my_account.account_name)
print('余额:', my_account.balance)
print('年利率:', my_account.interest_rate)
print('年息:', my_account.annual_interest())
