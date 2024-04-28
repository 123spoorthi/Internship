name=['nawaz','malli','prathiksha','aftab']
password=[123,1234,12345,1233]
balance=[1000000,2000000,500000,1000]

def withdraw(current):
    amount=int(input("Enter the amount : "))
    if amount<=balance[current]:
        balance[current]-=amount
        print("successfully")
    else:print("Insufficient funds")
def c_balance(current):
    print("balance is ",balance[current])

def default(current):
    print("enter crt option")




u_name=input('Enter your name : ')
for i in range(len(name)):
 if u_name==name[i]:

    u_password=int(input('Enter your password : '))
    if u_password == password[i]:
        while True:
            print('1.withdraw\n2.balance')
            option=int(input('Enter your option : '))
            if option==0:break
            data={1:withdraw,2:c_balance}
            result=data.get(option,default)
            result(i)