prime=0
composite=0
n=int(input("enter a number: "))
if(n>0):
    for i in range(2,n+1):
        if(i%2!=0):
            prime=prime+1
        else:
            composite=composite+1
print("count of prime numbers",prime)
print("count of composite numbers",composite)
print("0 and 1 is neither prime nor composite")
