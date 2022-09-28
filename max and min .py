num=int(input("Enter the number of numbers "))
arr=[]
for i in range (num):
    a=int(input("Enter the Number: "))
    arr.append(a)
temp=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
rarr=arr[::-1]
M=int(input("M= "))
N=int(input("N= "))
print("%d max number is %d"%(M,rarr[M-1]) )
print("%d min number is %d"%(N,arr[N-1]))
Sum=rarr[M-1]+arr[N-1]
Difference=rarr[M-1]-arr[N-1]
print('sum= ',Sum)
