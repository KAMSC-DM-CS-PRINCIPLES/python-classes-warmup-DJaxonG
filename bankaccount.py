# TODO create class BankAccount
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, dep):
        if(dep > 0):
            self.balance += dep
        return self.balance
    
    def withdraw(self, wit):
        if(self.balance >= wit):
            self.balance -= wit
        return self.balance
    
    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    # create BankAccount below this
    pass