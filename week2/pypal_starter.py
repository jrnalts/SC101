import pypal


def bank():
    my_account = pypal.Pypal('Andrew', balance=1000, withdraw_limit=700)
    my_account.withdraw(1000)

    my_account.set_withdraw_limit(1100)
    my_account.set_name('andrew')

    my_account.withdraw(500)
    my_account.withdraw(1200)

    my_account.deposit(100)
    my_account.withdraw(600)

    # print(my_account._name)
    # print(my_account._withdraw_limit)
    # print(my_account.__balance)

    remain = my_account.get_balance()
    print(remain)


if __name__ == '__main__':
    bank()
