num =int(input("Enter a number:"))
factorial = 1
if num<0:
    print("Factorial does not exist for negative numbers")
elif num ==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("enter a number:"))

print_factors(num)
