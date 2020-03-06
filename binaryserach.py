def binarysearch(arr,n):
    low=0
    high=len(arr)-1
    while low<=high:
        mid = int((low + high) // 2)
        if(n==arr[mid]):
            return mid
        elif(n>arr[mid]):
            low=mid+1
        else:
            high=mid-1
def ar1(a,n):
    print("number is",n)
    print("index at",a)
n=int(input("enter the to be in array"))
arr=list(map(int,input().split()[:n]))
k=int(input("enter the search element"))
binarysearch(arr,k)


