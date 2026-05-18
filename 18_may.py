#WAP to count total number of vowels in a string using while loop.
str1="rohan"
i=0
count=0
while i<len(str1):
    if str1[i] in "aeiouAEIOU":
        count+=1
    i+=1
print(count)