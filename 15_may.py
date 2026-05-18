#wap to print the total of even numbers from 1 to 15.
# strt=1
# end=15
# sum=0
# while strt<=end:
#     if strt%2==0:
#         sum+=strt
#         print(sum)
#     strt+=1

#WAP to check the given string by user is pallindrom or not.
# str1=input("Enter the string : ")
# copy_t=str1
# rev=""
# i=len(str1) -1

# while i>=0:
#     rev+=str1[i]
#     i-=1
# if copy_t==rev:
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")


#wap tp reverse the digit : 1234
num=1234
rev=0

while num!=0:
    dig=num%10
    rev=rev*10+dig
    num//=10
print(rev)