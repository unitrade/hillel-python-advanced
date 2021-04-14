import datetime
from math import isinf, isnan


class LessThanZeroException(Exception): pass
class InfiniteException(Exception): pass
class NanException(Exception): pass
class MaxDepositOneTimeException(Exception): pass
class InsufficientFundsException(Exception): pass


class Account:
    MAX_DEPOSIT = 10000  # Maximum transfer amount

    def __init__(self, amount: float, num_tx: int = 10):
        self.__amount = amount
        self.__num_tx = num_tx
        self.__tx = []
        self.__add_tx('Init', self.__amount)

    def get_amount(self):
        return self.__amount

    def get_txs(self):
        return self.__tx[:]

    def deposit(self, amount: float):
        self.__is_deposit_valid(amount)
        self.__add_amount(amount)
        self.__add_tx('Deposit', amount)

    def withdraw(self, amount: float):
        self.__is_withdraw_valid(amount)
        self.__subtract_amount(amount)
        self.__add_tx('Withdraw', amount)

    @staticmethod
    def __is_deposit_valid(amount):
        if amount < 0:
            raise LessThanZeroException('The operation cannot be performed - deposit can not be less than 0')
        if isinf(amount):
            raise InfiniteException('Infinite is not allowed')
        if isnan(amount):
            raise NanException('NaN is not allowed')
        if amount == 0:
            print('No action required - nothing to do!')
        if amount > Account.MAX_DEPOSIT:
            raise MaxDepositOneTimeException('The operation cannot be performed - Max deposit is %s' % Account.MAX_DEPOSIT)

    def __is_withdraw_valid(self, amount):
        if amount < 0:
            raise LessThanZeroException('The operation cannot be performed - withdraw can not be less than 0')
        if isinf(amount):
            raise InfiniteException('Infinite is not allowed')
        if isnan(amount):
            raise NanException('NaN is not allowed')
        if amount == 0:
            print('No action required - nothing to do!')
        if amount > self.__amount:
            raise InsufficientFundsException('The operation cannot be performed - insufficient funds')

    def __add_tx(self, status: str, amount: float):
        log = "{0} | {1} | {2}".format(datetime.datetime.now().isoformat(), status, str(amount))
        if self.__num_tx == 0:
            return self.get_txs()
        if len(self.get_txs()) < self.__num_tx:
            self.__tx.append(log)
        else:
            self.__tx = self.__tx[1:]
            self.__tx.append(log)
        return self.get_txs()

    def __add_amount(self, amount):
        self.__amount += amount

    def __subtract_amount(self, amount):
        self.__amount -= amount


if __name__ == '__main__':
    acc = Account(1000.00)
    assert len(acc.get_txs()) == 1, 'No transactions'

    acc.deposit(500.10)
    acc.withdraw(300)
    acc.deposit(1000)
    acc.deposit(500)
    acc.withdraw(550)
    acc.withdraw(300.50)
    acc.deposit(500)

    for i in acc.get_txs():
        print(i)
    print("acc::::::::::::TOTAL:"" ", acc.get_amount())

    # 2021-04-10T11:31:10.488422 | Init | 1000.0
    # 2021-04-10T11:31:10.488504 | Deposit | 500.1
    # 2021-04-10T11:31:10.488516 | Withdraw | 300
    # 2021-04-10T11:31:10.488523 | Deposit | 1000
    # 2021-04-10T11:31:10.488527 | Deposit | 500
    # 2021-04-10T11:31:10.488533 | Withdraw | 550
    # 2021-04-10T11:31:10.488538 | Withdraw | 300.5
    # 2021-04-10T11:31:10.488543 | Deposit | 500
    # acc::::::::::::TOTAL:  2349.6
