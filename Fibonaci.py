# n1 = 0
# n2 = 1
# term = 10
# i = 0
# while i < term:
#   print(n1,end=",")
#   nth = n1+n2
#   n1 = n2
#   n2 = nth
#   i+=1

def fibo():
  n1,n2 = 0,1
  term = int(input("Enter number of terms = "))
  i = 0
  while i < term:
    print(n1,end=",")
    nth = n1+n2
    n1 = n2
    n2 = nth
    i+=1
fibo()