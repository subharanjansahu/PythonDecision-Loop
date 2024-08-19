l = 100
h = 2000
for i in range(l,h+1):
  temp = i
  ln = len(str(temp))
  sum = 0
  while temp > 0:
    di = temp % 10
    sum = sum + di**ln
    temp = temp // 10
  if i == sum:
    print(sum)