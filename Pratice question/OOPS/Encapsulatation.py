'''
💡 Theory

Encapsulation = wrapping variables (data) and methods (functions) inside a class so we can control access to them.

Think of it like a bank locker 🔒:

You can’t directly touch the money (private variable).

You must use deposit() / withdraw() methods to interact safely.

🔑 Access Modifiers in Python

Python doesn’t enforce strict access rules like Java or C++, but we use naming conventions:

Public variables/methods (default, no underscore)
→ Accessible from anywhere.

Protected variables/methods (_var)
→ Convention: internal use only (but still accessible).

Private variables/methods (__var)
→ Name mangled → can’t be accessed directly.

'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner             # Public variable
        self._account_type = "Saving"  # Protected variable
        self.__balance = balance       # Private variable

    # Public method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New Balance = {self.__balance}")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, New Balance = {self.__balance}")
        else:
            print("Insufficient balance!")

    # Getter method for balance
    def get_balance(self):
        return self.__balance


# Create account
acc = BankAccount("Manvendra", 1000)

# Public access
print(acc.owner)          # ✅ Allowed

# Protected access (not recommended but possible)
print(acc._account_type)  # ✅ Works, but "for internal use"

# Private access
#print(acc.__balance)    # ❌ ERROR: Attribute not found

# Access via method
print(acc.get_balance())  # ✅ Correct way
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(5000)
