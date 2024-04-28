rows=int(input("Enter the pyramid pattren Rows"))
print("pyramid star pattren")
for i in range(0,rows):
    for j in range(0,rows-i-1):
        print(end = ' ')
    for k in range(0,i+1):
        print('*',end = ' ')
    print()

