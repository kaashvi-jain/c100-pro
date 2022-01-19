class atm (object):
    def __init__(self,cardno,pin,bn):
        self.cardno=cardno
        self.piv=pin
        self.bn=bn
        self.bal=50000
    def checkbal(self):
        print("your balance is : ",self.bal)
    def withdraw(self,amount):
        bal=self.bal-amount
        if bal<0:
            print("you do not have balance")
        else:
            self.bal=bal
            print("your balance is : ",self.bal)   

bank=input("please enter your bank: ")
cardno=input("please enter your card number ")
pin=input("please enter your pin  ")
newuser=atm(cardno,pin,bank)
print("1 check balance")
print("2 cash withdraw")
activity=int(input("please enter your option "))
if activity==1:
    newuser.checkbal()
elif activity==2:
    amount=int(input("please enter the amount "))
    newuser.withdraw(amount)
else:
    print("invaild option")        

