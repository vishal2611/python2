#1.WAP to sum of the indices of a string : "python"
str1="python"
size=len(str1)
sum=0
for i in range(size):
    sum+=i
print(sum)


#2. WAP to print the factorial from 1 to 8.
fact=1
for i in range(1,9):
    fact*=i
    print(f"Factorial of {i} : {fact}")

#3. WAP to print only prime numbers from 1 to 15

print("Prime numbers between 1 to 15 : ")
for i in range(1,16):
    if i>1:
        for j in range(2,i):
            if (i%j) ==0:
                break
        else:
             print(i)