class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def __str__(self):
        return f"{self.owner}: ${self._balance}"

acct = BankAccount("Alice", 1000)
acct.deposit(500)
print(acct)

# Expected Output:
# Alice: $1500
