#1. creation of list
#2. Updation of list
#3. Indexing
#4. slicing
#5. Traversing
#6.In-builtmethods
#7.Test
#8. Assignments

#slicing
# marks=[10,20,30,40,50,60,70,80]  #[start-0:stop-1:step-1]

# # sublist=marks[0:6]
# # sublist=marks[0:8:2] # skips 1 element and takes 1 element
# sublist=marks[::-1] # reverse the list
# print(sublist)

#Traversing
# marks=[10,11,20,21,30,31,40,41,50,51,60,61,70,80]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print("The element is even: ",marks[i])
#     else :
#         print("The element is odd: ",marks[i])

marks=[10,11,20,21,30,31,40,41,50,51,60,61,70,80]
total=0
for i in marks:
    total=total+i
print("The total is: ",total)