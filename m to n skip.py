M=int(input("Enter the starting number of range:"))
N=int(input("Enter the ending number of range:"))
k=int(input("Enter the numbers to be skipped in range:"))
for i in range(M,N+1,k+1):
    print(i)
