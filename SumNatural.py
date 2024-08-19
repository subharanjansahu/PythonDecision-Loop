# n = 5
# sum = 0
# for i in range(1,n+1):
#   sum +=i
# print(sum)

# use method in an interval
def sum(l,h):
  add = 0
  for i in range(l,h+1):
    add += i
  print("sum between",l,"and",h,"is =",add)
sum(1100,1200)