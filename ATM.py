#program(atm transaction
#first method______!

'''
import time;
class insufficientfundsexception(Exception):
    def __init__(self,msg):
        self.msg=msg

print("atm transaction")
print('*************************************************************************************')
print("enter atm card")
cpin=2020
abal=5000
print("correct pin::")
#print("enter bal::")
time.sleep(1)
epin=int(input("enter the pin"));
time.sleep(1)
try:
    if cpin!=epin:
        raise insufficientfundsexception("you enter wrong pin")
    else:
        wamt=int(input("enter amount"))
        abal=abal-wamt
        print("Balance after Successuful-Transaction : ",abal)
        print("end of the transaction")
        print("take your card....")

except insufficientfundsexception as msg:
    #print("msg")
    print("transaction is invalidpine xception")
    print("you enterd wrong pin")

    
'''
#Second method______!
'''
import time;
class invaildpinexception(Exception):
    def __init__(self,msg):
        self.msg=msg;#main program
print("ATM pin");
print("****************");
cpin=1976
print("correct pin ::")
time.sleep(1)
epin=int(input("enter the pin::"));
time.sleep(1)
try:
    if cpin!=epin:
        raise invaildpinexception(" you have enter wrong pin")
    else:
        cpin=epin
    print("correct pin")
except invaildpinexception as msg:
    print(msg)  
#class insufficientfundsexception(invaildpinexception):
    def __init__(self,msg):
        self.msg=msg
time.sleep(1)
acbal=8000
print("Initial-Balance ::",acbal);
time.sleep(5)
wamt=int(input("Enter Withdraw Amount : "));		#6000
time.sleep(5)
try:
    if wamt>acbal:
        raise insufficientfundsexception("Less Funds in Account...");
    else:
        acbal=acbal-wamt;
        print("Balance after Successuful-Transaction : ",acbal);
except insufficientfundsexception as msg:
    print(msg)
    print("Transaction NOT possible!!!");
time.sleep(5)

print("********************************");
print("Final-Account Balance : ",acbal);
print("End of the ATM Transaction");
'''
        
#######################################################################################################
#third method______!

import time;
'''
print("atm machine")
print("********************well come to telangana gramenna bank*****************")
bal=5000
cpin=2020
print("enter the atm card")
epin=int(input("enter pin number:"))
time.sleep(2)
if(epin==cpin):
    print("1-withdrow")
    print("2- deposit")
    print("3-check balance")
    print("4-change pin")
    c=int(input("choice the transation:"))
    if(c==1):
        w=int(input("enter the amount"));
        bal=bal-w
        print("after your successfull transation",bal)
        print("end of the transaction...")
    elif(c==2):
        d=int(input("enter your deposit amount"))
        bal=bal+d 
        print("after deposit total amount",bal)
        print("end of the transaction...")
    elif(c==3):
        print("your current amount",bal)
        print("end of the transaction...")
    elif(c==4):
        c=int(input("enter the your choice pin :"))
        cpin==c
        print("after your modify pin is ",c)
        print("successfully modifyed")
        print("end of the transaction")
else:
    epin!=cpin
    print("you enter the wrong pin!!!!")
    print()
'''  