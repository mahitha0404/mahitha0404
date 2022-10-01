age=int(input("Enter your age: "))
if(age>18):
    print("You are eligible for vote")
else:
    x=18-age
    print("You are allowed to vote after %d years"%x)
