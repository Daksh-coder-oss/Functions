def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("A. add\n","B.subtract\n","C.multiply\n","D.divide")
functions=input("What do you wanna do in the calculator,pick an option")
a=int(input("Please enter the value of a"))
b=int(input("Please enter the value of b"))
if functions=="A" or functions=="a":
    print(add(a,b))
elif functions=="B" or functions=="b":
    print(subtract(a,b))
elif functions=="C" or functions=="c":
    print(multiply(a,b))
elif functions=="D" or functions=="d":
    print(divide(a,b))
else:
    print("The given input is invalid")
    



