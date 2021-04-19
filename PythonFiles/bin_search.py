"""THis is binary search algorithm using recursion"""
"""defining a function for bin_search"""
def binary_search(arr,low,high,x):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        print("element is not present")
        return -1
arr=[1,2,3,4,5]
x=1
result=binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print("element is found at:"+str(result))
else:
    print("element not found")
