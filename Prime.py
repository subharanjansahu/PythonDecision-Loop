num = 21
for i in range(2,num//2):
  if num%i == 0:
    print(num,"is non prime")
    print(i,"times",num//i,"is",num)
    break
  else:
    print(num,"is prime")