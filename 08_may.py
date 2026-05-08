#Loops in python
#1. for loop : range based
#2. while loop : condition based

#for loop , if _ is found in for loop it means _ is just to run the loop or to complete the syntax
#range(start:0,stop-1, step), and it always works with integer value
# for i in range(5):
#     print(i)

# for i in range(1,15,2):
#     print(i,end=" ")
#     print("Python",end=" ") #end=" " is used to change the vertical to horizintal

# for i in range(1,20):
#     if i==10:
#         break  # it breaks the loop
#     print(i)

# for i in range(1,20):
#     if i==10:
#         continue  # it skips the number in  the loop
#     print(i)

# for i in range(1,20):
#     if i%2!=0:
#         print(f"Odd: {i}")  
#     else:
#         print(f"Even: {i}")

# s=0
# for i in range(1,5):
#     s+=i
# print(s)

#reverse for loop
for i in range(10,0,-1):
    print(i, end=" ")
