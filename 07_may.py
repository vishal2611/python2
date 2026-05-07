# #nested if else
# name=input("Enter your name: ")
# if name:
#     print(f"Yes name {name} is provided")
#     addr=input("Enter your address:")
#     if addr:
#         print("Address is : ", addr)
#     else:
#         print("Address is not provided")


# else:
#     print("Name is not provided")


# n1=int(input("Enter the number: "))
# if n1%2==0:
#     print(f"Number {n1} is even ")
# else:
#     print(f"Number {n1} is odd")

student_n=input("Enter student name: ")
roll=int(input("Enter your roll number: "))
pre=int(input("Enter your pre marks: "))
if pre>=400:
    print("You are pass in pre and eligible for mains.")
    mains=int(input("Enter your mains marks: "))
    if mains >= 600:
        print("You are pass in Mains and eligible for Interview")
        inter=int(input("Enter your Interview marks: "))
        if inter>=700:
            print(f"You are selected as an IAS Mr.{student_n}")
        else:
            print("Better Luck Next time, you failed")
    else:
        print("Fail in Mains")
else:
    print("Better luck next time, pre failed ❌")