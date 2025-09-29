# This is the bank example

balance=0


def main():
    print("Balance",balance)
    deposit(100)
    withdraw(28)
    print("Balance: ",balance)


def deposit(n):
    balance +=n

def withdraw(n):
    balance -= n

if __name__=="__main__":
    main()


# In the above code we get unboundlocalerror dispite that we already define the balance