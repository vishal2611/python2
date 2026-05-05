# 5. Membership opr

str1="This is python for devops"  #find command or membership opr doesn't work for numbers
find="this" #case sensitive
find2="This"
#print(find2 in str1)

num1="4567"
#print("4" in num1)
#print("4" not in num1)

email="iqindia123@gmail.com"
find="@gmail.com"
# if find in email:
#     print("This is a valid google mail id")
# else:
#     print("Invalid email")

#age comparison
aman_age=20
abhishek_age=30
# if aman_age>abhishek_age:
#     print("Yes, aman's age is more than abhishek")
# else:
#     print("No, aman's age is not more than abhishek")

#user is eligible for voting.
min_age=18
nationality="IN"
user_age=int(input("Enter your age: "))
user_id=input("Enter your Identity (ex. IN): ")
if user_age>=min_age and user_id==nationality:
    print("User is eligible")
else:
    print("User is not eligible")