l=[2,7,6,3,8,1]
n=len(l)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if l[min]>l[j]:
            min=j
            l[i],l[min]=l[min],l[i]
print(l)