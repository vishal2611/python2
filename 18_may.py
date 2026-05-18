#WAP to count total number of vowels in a string using while loop.
# str1="rohan"
# i=0
# count=0
# while i<len(str1):
#     if str1[i] in "aeiouAEIOU":
#         count+=1
#     i+=1
# print(count)

#wap tp print formatted table of a number givern by user.
num1=int(input("Enter a number: "))
i=1
while i<=10:
    print(f"{num1} x {i} = {num1*i}")
    i+=1