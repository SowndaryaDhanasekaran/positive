n=int(input())
k=int(input())
list=[]
sum=0
for i in range(0,n):
    number=int(input())
    list.append(number)
for i in range(0,k):
    sum=sum+list[i]

print(sum)
