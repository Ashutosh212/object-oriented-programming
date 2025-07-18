class Account:
    def __init__(self):
        self._balance = 0  # visual clue this _balance is private, do not touch

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


if __name__=="__main__":
    account = Account()
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")