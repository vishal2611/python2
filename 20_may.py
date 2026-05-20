#WAF to check number pass by argument is odd or even
# def check(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "odd"
# res=check(4)
# print(res)

#waf to check which number is greater among two numbers by user input
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# res=greater(a,b)
# print("Greater number is:", res)

#waf to check character pass by user is vowel or consonant
# def check_char(a):
#     if a in "aeiouAEIOU":
#         print("vowel")
#     else:
#         print("consonant")
# char=input("Enter a character: ")
# check_char(char)


#waf to check a number is completely divisible by 2 & 3
# def check_num(num):
#     if num % 2 == 0 and num % 3 == 0:
#         return "YES NUMBER IS COMPLETELY DIVIDED"
#     else:
#         return "No, NUMBER IS NOT COMPLETELY DIVIDED"
# number = int(input("Enter a number: "))
# result = check_num(number)
# print(result)

#WAF to return the length of a string passed by user without using len() function
def check_len(a):
    count=0
    for i in a:
        count+=1
    return count
str1=input("Enter a string: ")
res=check_len(str1)
print("Length of the string is:", res)
