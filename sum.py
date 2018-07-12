N=int(input())
K=int(input())
total=0
list=[]
if(N>0 and K>0):
   for i in range(0,N):
      number=int(input())
      list.append(number)
   for i in range(0,K):
      total=total+list[i]
   print(total)
else:
  print("invalid")
