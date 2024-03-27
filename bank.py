# определите класс "Account", имитирующий банковский счет.  Класс должен включать атрибуты
# для хранения идентификатора владельца, баланса счета и методы для депозита (пополнения) и
# снятия средств, если на счету достаточно средств

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Счет успешно пополнен.  Сумма на счету {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} сом.  Остаток на счете {self.balance}")

    def info(self):
        print(f"Текущий баланс: {self.balance}")

man = Account(32479898, 600)
man.info()
man.withdraw(430)
man.withdraw(350)
man.deposit(23000)



