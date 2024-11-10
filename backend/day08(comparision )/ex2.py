
class BankAccount:


    account_counter=1000



    def __init__(self, owner ,balance=0, branch_name="sbi",branch_name1='HDFC'):

        self.owner =owner
        self.balance =balance
        self.Branch_name =branch_name
        self.Branch_name1 =branch_name1


        self.Account_number = BankAccount.account_counter
        BankAccount.account_counter +=10



    def deposit(self, amount):
            if amount >0:
                self.balance +=amount
                print(f"We have a successful done Amount will be Deposit:${self.balance} ")
            else:
                print(f"there is the deposit amount but pls waiting........ ")
    #         With draw option ...................
    def withdraw(self, amount):
        if amount >self.balance:
            print("account balance zero.... ")
        elif amount < 0:
            print("Withdraw amount will be done process....")
        else:
            self.balance +=amount
            print(f"We have successful done Withdraw. pls check new :{self.balance} ")
    def check_balance(self):
        print(f"Account Balance:{self.balance}")


    def account_info(self):
        print(f"Account Holder name:{self.owner}")
        print(f"Account number:{self.Account_number}")
        print(f"Account Holder Balance:{self.balance}")
        print(f"Account Holder Branch_name:{self.Branch_name}")
        print(f"Account holder Branch_name1:{self.Branch_name1}")



Account1= BankAccount("vijay",100,"Bangalore")
Account2= BankAccount("Upendra",500,'Hyderabad')
Account3= BankAccount('kumarreddy',1000,"New york",'kodipalli')



print("\n---Some information about account1 -----")
Account1.account_info()
print("\n---Some information about account2 -----")

Account2.account_info()
print("\n---Some information about account3 -----")
Account3.account_info()

print("\n------the details of  Transactions for Account 1 ---")
Account1.deposit(20000)
Account1.withdraw(200)
Account1.check_balance()


print("\n------the details of  Transactions for Account 2---")
Account2.deposit(200)
Account2.withdraw(500)
Account2.check_balance()
print("\n------the details of  Transactions for Account 3 ---")

Account3.deposit(10000)
Account3.withdraw(700)
Account3.check_balance()


