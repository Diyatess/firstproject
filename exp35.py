# class bank:
#     def __init__(self,name,accnt,acno):
#         self.name=name
#         self.accnt=accnt
#         self.acno=acno
#         self.blnc=0
#     def show(self):
#         print("Name: ",self.name)
#         print("Account Type: ",self.accnt)
#         print("Account No: ",self.acno)
#         print("Balance: ",self.blnc)
#     def dpst(self,d):
#         self.blnc=self.blnc+d
#         return self.blnc
#     def wdrw(self,w):
#         self.blnc=self.blnc-w
#         return self.blnc
# name=input("Enter the name: ")
# accnt=input("Enter the account type: ")
# acno=int(input("Enter the account No:"))
# ba=bank(name,accnt,acno)
# x=ba.show()
#
# while(True):
#     print("Menu")
#     print("1.Deposit")
#     print("2.Withdraw")
#     a=int(input("Enter your choice:"))
#     if a==1:
#         d=int(input("Enter the amount to deposit:"))
#         print("Your total balance amount is ",ba.dpst(d))
#     elif a==2:
#         w=int(input("Enter the amount to withdraw:"))
#         if w>d:
#             print("Insufficient Balance")
#         else:
#             print("Your total balance amount is ",ba.wdrw(w))
#     else:
#         print("Invalid Choice")


class bank:
    def __init__(self,acc,name,acctype):
        self.acc=acc
        self.name=name
        self.acctype=acctype
        self.bal=0
    def showaccdet(self):
        print("Account Number:",self.acc)
        print("Account Holder Name:",self.name)
        print("Account Type:",self.acctype)
        print("Account Balance:",self.bal)

    def deposit(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal
name=input("Enter Name:")
accountnum=int(input("Enter account num:"))
accounttyp=input("Enter account type:")
o=bank(accountnum,name,accounttyp)
o.showaccdet()
while("true"):
    print("MENU")
    print(" 1.Deposit")
    print(" 2.Withdraw")
    choice=int(input("enter youe choice:"))
    if choice==1:
        d1=int(input("Enter the depositing value:"))
        o.deposit(d1)
        print("balance:",o.bal)
    elif choice==2 :
        w1 = int(input("Enter the amount to withdraw:"))
        if w1 > d1:
            print("Insufficient Balance")
        else:
            print("Your total balance amount is ", o.withdraw(w1))

    else:
        print("Invalid choice")

