a,b=input().split()
arr=list(map(int,input().split()[:int(a)]))
op=[]
for i in range(int(b)):
    loc=0
    c,d=input().split()
    for j in range(int(c),int(d)+1):
        loc=loc+arr[j]
    op.append(loc)
for k in range(len(op)):
    print(op[k])