# marks=[10,20,30,40,50,60,70,80,90,100]
# sub_list=marks[:-1]
# print(sub_list)


#wap to swap first and last value of list
# marks=[10,20,30,40,50,60,70,80,90,100]
# print("Before swapping: ",marks)
# temp=marks[0]
# marks[0]=marks[-1]
# marks[-1]=temp
# print("After swapping: " ,marks)

#wap to find the sum of all elements in the list : [10,20,30,40]
# l1=[10,20,30,40]
# s=0
# for i in l1:
#     s+=i
# print("The sum of all elements of list: ",s)


#wap to find the sum of only even elements in the list : [10,3,4,6,22,31,33,55,40]
# l1=[10,3,4,6,22,31,33,55,40]
# s=0
# for i in l1:
#     if i%2==0:
#         s+=i
# print("The sum of only even elements of list: ",s)

#wap to find the sum of only odd elements in the list : [10,3,4,6,22,31,33,55,40]
# l1=[10,3,4,6,22,31,33,55,40]
# s=0
# for i in l1:
#     if i%2!=0:
#         s+=i
# print("The sum of only odd elements of list: ",s)

#wap to find the count of how many int values and how many string values in the list : [70,"aman",50,10,20,"rohan","iq-india"]
l1=[70,"aman",50,10,20,"rohan","iq-india"]
int_count=0
str_count=0
for i in l1:
    if type(i)==int:
        int_count+=1
    elif type(i)==str:
        str_count+=1
print("The count of int values in the list: ",int_count)
print("The count of string values in the list: ",str_count)

