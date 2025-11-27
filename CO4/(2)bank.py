class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance: ₹", self.balance)


acc1 = BankAccount(12345, "Rahul", "Savings", 5000)

acc1.display()
while(1):
    a=int(input("\n 1.deposit\n 2.withdra\n 3.display status\n 4.quit\n enter your choice:"))
    if a==1:
        depo= int(input("enter the amount to be deposited:"))
        acc1.deposit(depo)
    elif a==2:
        withdraw =int(input("enter the amount to be withdraw:"))
        acc1.withdraw(withdraw)
    elif a==3:
        acc1.display()
    elif a==4:
        break
    else:
        print("enter a valid option!!")

