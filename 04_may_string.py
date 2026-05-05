#string ('', "", ''' ''')  char is not supported in python, string is used for it. 
#string ia series of character, space, symbols.

student_name="Aman Kumar"
student_address="D-1 255/455 NOIDA SEC-15 NEW DELHI 110096"
student_mob="+91 7250871431"
#print(len(student_mob))
student_profile=f"""Hi my name is {student_name} and I am a "DevOps intern" 
and looking for challenging opportunity"""
# print(student_profile)



#operators in python
# 1. Arithmetic operator
# 2. Assignment opr
# 3. Comparison opr
# 4. Logical opr
# 5. Membership opr
# 6. Identity opr
# 7. Bitwise opr

#2. Assignment opr
a=10
#a=a+10  #standard way
a+=10  #shorthand method
#print(a)

#3. Comparison opr/logical (<,>,>=,<=,==,!=)
n1=30
n2=40
#print(n1>n2) 

# 4. Logical opr (and, or,not)
n1=1
n2=3
#res=n1==1 and n2==3 and n1==2 and n2==3
res=not(n1==1 or n2==3 or n1==2 or n2==3)
print(res)