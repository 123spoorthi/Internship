def binary_search(arr, target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid] == target:
        elif arr[mid]<target:
        else:right=mid-1
    return-1
numbers=[1,2,3,4,5,6,7,8,9,10]
