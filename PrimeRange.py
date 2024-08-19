lower = 900
higher = 1000
print("Prime numbers between",lower,"and",higher,"are = ")
for num in range(lower,higher+1):
  for i in range(2,num//2):
    if num % i == 0:
      # print(num,"is non prime")
      break
  else:
    print(num,end=",")