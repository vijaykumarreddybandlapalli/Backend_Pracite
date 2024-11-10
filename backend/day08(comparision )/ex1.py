
class BankAccount:
    # Class variable
    account_counter = 1056503


    def __init__(self, owner, balance=0, branch_name="SBI"):

        self.owner = owner
        self.balance = balance
        self.branch_name= branch_name

        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 10


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance}")

    # Method to check balance
    def check_balance(self):
        print(f"Account Balance: ${self.balance}")

    # Method to display account details
    def account_info(self):
        print(f"Account Holder: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Branch Name: {self.branch_name}")
        print(f"Balance: ${self.balance}")




account1 = BankAccount("Vijay", 500, "Anathapur")
account2 = BankAccount("Jeevan", 1000, "Kadiri")
account3 = BankAccount( "Pradeep",2000,"Thirupathi" )


print("\n--- Information About  Account 1 Info ---")
account1.account_info()

print("\n---Information About  Account 2 Info ---")
account2.account_info()


print("\n---------Information about account 3Info----")
account3.account_info()

print("\n---  the details of Transactions for Account 1 ---")
account1.deposit(300)
account1.withdraw(200)
account1.check_balance()

print("\n------the details of  Transactions for Account 2 ---")
account2.withdraw(1500)
account2.deposit(500)
account2.check_balance()

print("\n------the details of  Transactions for Account 3 ---")
account3.withdraw(1500)
account3.deposit(500)
account3.check_balance()
































































































