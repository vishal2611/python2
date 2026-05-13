# name="python"                 #traversing ofstring using range()
# size=len(name)
# for i in range(size):         # i is a helping variable in loop
#     print(name[i],end="")    #we can print indexing as well in this way. (using range())

# name="python"
# for i in name:          # only string will get printed. (without using range)
#     print(i,end="")

# var1="DevOps Engineer"
# for i in var1:
#     if i=="e":
#         continue
#     print(i,end="")

#WAP to count all the vowels from given string: "This is a Devops batch."
# var1="this is devops batch"
# count=0
# c_count=0
# for i in var1:
#     if i in "aeiou":
#         count+=1 
#     elif i==" ":
#         continue
#     else:
#         c_count+=1
# print(count)
# print(c_count)


#WAP to print your name in reverse format
name="Vishal"
reverse=" "
for i in name:
    reverse=i+reverse
print(reverse)


