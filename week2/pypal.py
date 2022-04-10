# BANK ACCOUNT CONFIG
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, balance=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._name = name
        self.__balance = balance
        self._withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self._withdraw_limit:
            print('Warning: Exceed Limit')
        elif amount > self.__balance:
            print('Warning: Balance Not Enough')
        else:
            self.__balance -= amount
            print(f'Withdraw Success! {self._name} remains: {self.__balance}')

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposit Success! {self._name} remains: {self.__balance}')

    # setter
    def set_withdraw_limit(self, withdraw_limit):
        self._withdraw_limit = withdraw_limit

    # setter
    def set_name(self, new_name):
        self._name = new_name

    # getter
    def get_balance(self):
        return self.__balance

    @staticmethod
    def bank():
        my_account = Pypal('Andrew', balance=1000, withdraw_limit=700)
        my_account.withdraw(500)
        my_account.withdraw(1000)
        my_account.withdraw(600)


# def bank():
#     my_account = Pypal('Andrew', balance=1000, withdraw_limit=700)
#     my_account.withdraw(500)
#     my_account.withdraw(1000)
#     my_account.withdraw(600)


if __name__ == '__main__':
    print('Welcome to Pypal!')
    Pypal.bank()
