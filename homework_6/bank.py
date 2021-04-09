import datetime


class Account:
    MAX_DEPOSIT = 10000

    def __init__(self, amount: float, num_tx: int = 10):
        self.__amount = amount
        self.__num_tx = num_tx
        self.__tx = []
        self.__add_tx('Init', self.__amount)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        pass

    def deposit(self, amount):
        is_amount_valid, err = self.__is_deposit_valid(amount)
        if not is_amount_valid:
            return is_amount_valid, err
        self.__add_amount(amount)
        self.__add_tx('Deposit', amount)

    def get_txs(self) -> list:
        return self.__tx[:]

    def __add_amount(self, amount):
        self.__amount += amount

    @staticmethod
    def __is_deposit_valid(amount):
        if amount < 0:
            return False, 'The operation cannot be performed - deposit can not be less than 0'
        if amount == 0:
            return False, 'No action required'
        if amount > Account.MAX_DEPOSIT:
            return False, 'The operation cannot be performed - Max deposit is %s' % Account.MAX_DEPOSIT
        return True, ''

    def __add_tx(self, status, amount):
        log = "{0} | {1} | {2}".format(datetime.datetime.now().isoformat(), status, str(amount))
        if self.__num_tx == 0:
            return self.get_txs()
        if len(self.get_txs()) < self.__num_tx:
            self.__tx.append(log)
        else:
            self.__tx = self.__tx[1:]
            self.__tx.append(log)
        return self.get_txs()


if __name__ == '__main__':
    acc = Account(-1000.00)

    acc.amount = 10000  # Check for manual set
    assert acc.amount == 1000, "Can not be set manual"

    print(acc.amount)
    acc.deposit(500)
    acc.deposit(1000)
    acc.deposit(500)
    acc.deposit(2000)
    acc.deposit(10000)
    acc.deposit(500)
    print("acc: ", acc.amount)
    for i in acc.get_txs():
        print(i)
