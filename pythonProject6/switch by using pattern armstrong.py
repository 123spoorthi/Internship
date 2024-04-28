def armstrong():
    num=int(input("Enter a number: "))
    arms=str(num)
    result=0
    for i in arms:
        result=result+int(i)**len(arms)
        print(result)
        if result==num:
            print("The number is an armstrong number")
        else:
            print("The number is not an armstrong number")
armstrong()

def pattren1():
    n=5
for i in range(1,n+1):
    print(" "*i)sssss
for i in range(1,0,-1):
    print("*"*i)
pattren1()

def pattren2():
    n=5
for i in range(1,n+1):
        print(" "*n-i,"*"*i)
for i in range(n-1,0,-1):
    print("*"*i)
pattren2()

def switch_case():
    n=int(input("Enter a functionname:"))
    switch_data={1:armstrong,
                 2:pattren1,
                 3:pattren2}
    result=switch_data.get(n,default)
    result()
    switch_case()

