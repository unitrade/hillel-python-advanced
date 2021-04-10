import datetime


class Account:
    """

    Class Account that represent a bank work flow

    ...

    Args:
    -----
        amount: float
            The initial amount, which may be negative
        num_tx: int
            The number of successful transactions which saved in log
            N=0 that means log off
            default=10

    Attributes:
    -----------
    __amount: float
        The  amount of account
    __num_tx: int
        The number of successful transactions
    __tx: list
        The list that stores the transaction log.
    __add_tx('str', self.__amount):
        method that add successful transaction to log
        'str' name of tx


    Methods:
    --------
    get_amount(self)
        A method that returns the current state of the account
    get_txs(self)
        A method that returns the current state of the account
    deposit(self, amount: float)
        A method of crediting the account
    withdraw(self, amount: float)
        A method of withdrawal
    __is_deposit_valid(amount)
        A private static method that check for deposit is valid
    __is_withdraw_valid(self, amount)
        A private method that check for withdraw is valid
    __add_tx(self, status: str, amount: float)
        A private method that writes logs
        Count of logs depends on num_tx variable
    __add_amount(self, amount)
        A method that increases the amount
    __subtract_amount(self, amount)
        A method that reduces the amount

    """

    MAX_DEPOSIT = 10000  # Maximum transfer amount

    def __init__(self, amount: float, num_tx: int = 10):
        self.__amount = amount
        self.__num_tx = num_tx
        self.__tx = []
        self.__add_tx('Init', self.__amount)

    def get_amount(self):
        """

        A method that returns the current state of the account

        Return:
            amount

        """
        return self.__amount

    def get_txs(self):
        """

        A method that returns successful transactions

        Return:
            transactions

        """
        return self.__tx[:]

    def deposit(self, amount: float):
        """

        A method of crediting the account

        Returns:
            False if amount is not valid

        """
        is_amount_valid, err = self.__is_deposit_valid(amount)
        if not is_amount_valid:
            return is_amount_valid, err
        self.__add_amount(amount)
        self.__add_tx('Deposit', amount)

    def withdraw(self, amount: float):
        """

        A method of withdrawal

        Returns:
            False if amount is not valid

        """
        is_amount_valid, err = self.__is_withdraw_valid(amount)
        if is_amount_valid is not True:
            return is_amount_valid, err
        self.__subtract_amount(amount)
        self.__add_tx('Withdraw', amount)

    @staticmethod
    def __is_deposit_valid(amount):
        """

        A private static method that check for deposit is valid
        Returns:
            False if amount < 0, amount == 0 and amount > MAX_DEPOSIT
            True in other cases

        """
        if amount < 0:
            return False, 'The operation cannot be performed - deposit can not be less than 0'
        if amount == 0:
            return False, 'No action required'
        if amount > Account.MAX_DEPOSIT:
            return False, 'The operation cannot be performed - Max deposit is %s' % Account.MAX_DEPOSIT
        return True, ''

    def __is_withdraw_valid(self, amount):
        """

        A private method that check for withdraw is valid

        Returns:
            False if amount < 0, amount == 0 and amount > MAX_DEPOSIT
            True in other cases

        """
        if amount < 0:
            return False, 'The operation cannot be performed - withdraw can not be less than 0'
        if amount == 0:
            return False, 'No action required'
        if amount > self.__amount:
            return False, 'The operation cannot be performed - insufficient funds'
        return True, ''

    def __add_tx(self, status: str, amount: float):
        """

        A private method that writes logs
        Count of logs depends on num_tx variable

        Return:
            transactions

        """
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
        """A method that increases the amount"""
        self.__amount += amount

    def __subtract_amount(self, amount):
        """A method that reduces the amount"""
        self.__amount -= amount


if __name__ == '__main__':
    acc = Account(1000.00)
    assert len(acc.get_txs()) == 1, 'No transactions'

    result, err = acc.withdraw(5000)
    assert result is False and err == 'The operation cannot be performed - insufficient funds'

    acc.__setattr__("amount", 10)  # Check for manual set
    assert acc.get_amount() == 1000, "Can not be set manual"

    result, err = acc.deposit(10000.01)
    assert result is False and err == 'The operation cannot be performed - Max deposit is 10000'

    result, err = acc.deposit(-10)
    assert result is False and err == 'The operation cannot be performed - deposit can not be less than 0'

    result, err = acc.deposit(0)
    assert result is False and err == 'No action required'

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
