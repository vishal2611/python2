#waf to check how many vowels in gien string
# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in s:
#         if char in vowels:
#             count+=1        
#     return count
# res=count_vowels("vIshal")
# print(res)


# Local Variable vs global variable
# def msg():
#     global name  # here we are declaring name as global variable so that it can be accessed outside the function
#     name="vishal"
#     print(name) #here we can print name variable beacuse it's already on local scope of the function
# msg()
# print(name) # here we can access name variable because we declared it as global variable inside the function

#waf to count char "p" in python programming and return total occurences
# def count_p(s):
#     count=0
#     for char in s:
#         if char=="p" or char=="P":
#             count+=1
#     return count

# res=count_p("Python programming")
# print(res)

# def count_char(dest,find):
#     count=0
#     for i in dest:
#         if i==find:
#             count+=1
#     return count
# dest="Python programming"
# find="p"
# res=count_char(dest,find)
# print(res)



# def count_p(s):
#     count=0
#     for char in s:
#         if char=="m" or char=="M":
#             count+=1
#     return count

# res=count_p("Python programming")
# print(res)

#waf to returnsum of string indexes
def sum_indexes(s):
    sum=0
    for i in range(len(s)):
        sum+=i
    return sum
res=sum_indexes("python")
print(res)