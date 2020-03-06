def selectionsort(arr):
    for i in range(len(arr)-1):
        minval=min(arr[i:])             
        minind=arr.index(minval,i)
        if arr[i]!=arr[minind]:
            arr[i],arr[minind]=arr[minind],arr[i]
    print(arr)


n=int(input("enter the number"))
arr=list(map(int,input().split()[:n]))
selectionsort(arr)
