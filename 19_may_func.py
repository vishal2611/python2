#what is function in python
#function is a block of code which only runs when it is called
#you can pass data, known as parameters, into a function.
#Every function has their own purpose.
#Function is a block of instructions(code) which execute inside its own block.
#Function is a reusable block of code which performs a specific task.(DRY-Don't Repeat Yourself )
#Syntax of function
#def function_name(parameters):

# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)


# add() #function call


#functions are divided into four types
#1. Take nothing and return nothing
#2. Take something and return nothing
#3. Take nothing and return something
#4. Take something and return something

#Parameters (para) & arguments (arg)
#Parameters are the variables which are defined in the function definition.
#Arguments are the values which are passed to the function when it is called.



# def table(n):
#     for i in range(1, 11):
#         print(n, 'x', i, '=', n*i)

# table(5)
# print("-"*20)
# table(7)
# print("-"*20)
# table(17)

def add(a, b):
    c = a + b
    print("Addition:", c)


def sub(a,b):
    c=a-b
    print("Subtraction:", c)


def product(a,b):
    c=a*b
    print("Product:", c)


def div(a,b):
    c=a/b
    print("Division:", c)
while True:
    option=input("Enter the option (+, -, *, /): ")
    if option == "0":
        print("Exiting the program.")
        break
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    
    if option=="+":
        add(num1,num2)
    elif option=="-":
        sub(num1,num2)
    elif option=="*":
        product(num1,num2)
    elif option=="/":
        div(num1,num2)
    else:
        print("Invalid option")