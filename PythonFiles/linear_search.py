def lin_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[1,2,3,4,5,5,6]
x=5
res=lin_search(arr,x)
print("element is found at:",str(res))
