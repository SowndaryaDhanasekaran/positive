number=input()
num=number.split()
num1=int(num[0])
num2=int(num[1])
num3=int(num[2])
if((num1>=num2) and (num1>=num3)):
  print(num1)
elif((num2>=num1) and (num2>=num3)):
  print(num2)
else:
  print(num3)
