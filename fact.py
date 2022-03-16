num = input("Enter a number: ")
def recur_fact(n):
if n == 1:
   return n
elif n < 1:
   return ("Factorial doesnt exist")
else:
   return n*recur_fact(n-1)
print (recur_fact(int(num)))
