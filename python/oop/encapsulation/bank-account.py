class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print('Withdrawal successful.')
        else:
            print('Insufficient balance!')


account = BankAccount('1234567', 1000)
print(account._balance)

"""To achieve stronger encapsulation and prevent direct access to _balance, you can use a double underscore (__) 
prefix for the variable name. This performs name mangling, which makes it harder to access the variable from outside 
the class. However, even with name mangling, it's still possible to access the variable with a modified name if desired.


Remember, encapsulation in Python relies more on conventions and developer discipline rather than strict enforcement.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    # Rest of the methods...


account = BankAccount("123456789", 1000)
print(account.get_balance())
print(account._BankAccount__balance)  # Name mangling, but not recommended
