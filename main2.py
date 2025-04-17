def add(x,y):
    return x+y

def subract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("please select an operation")
print("a addition")
print("b subraction")
print("c multiplication")
print("d division")

choice=input("enter your choice")

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

if choice=="a":
    print("addition" ,add(num1,num2))
elif choice=="b":
    print("subraction" ,subract(num1,num2))
elif choice=="c":
    print("multiplication" ,multiply(num1,num2))
elif choice=="d":
    print("division" ,divide(num1,num2))
else :
    print("invalid option")