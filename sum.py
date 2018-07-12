N=int(input())
K=int(input())
numbers=input()
x=numbers.split()
total=0
if(K>0 and N>0):
    for i in range(0,K):
        total=total+int(x[i])

    print(total)
else:
    print("invalid")
