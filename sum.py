N=int(input())
K=int(input())
total=0
list=[]
for i in range(0,N):
  number=int(input())
  list.append(number)
for i in range(0,K):
  total=total+list[i]
print(total)
