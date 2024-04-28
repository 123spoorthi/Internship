def armstrong_by_lambda():
    num=int(input("Enter a number:"))
    arms=str(num)
    result=list(map(lambda a:int(a)**len(arms),arms))
    final=0
    for i in result:final=final+i
    print(final)
armstrong_by_lambda()
