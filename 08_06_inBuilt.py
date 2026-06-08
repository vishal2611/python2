# In-built methods.
# append() method is used to add an element at the end of the list.

# emp_name=["aman", "shivam"]
# new_emp="kamal"
# emp_name.append(new_emp)
# print(emp_name)

# for i in range(1,11):
#     name=input(f"Enter employee name {i}: ")
#     emp_name.append(name)
# print(emp_name)


#nested list
# emp_name=["aman", "shivam"]
# print(emp_name)
# emp_name.append(["nam1","nam2","nam3"])
# print(emp_name)

#extend() method is used to add multiple elements at the end of the list.
# emp_name=["aman", "shivam"] 
# print(emp_name)
# emp_name.extend(["nam1","nam2","nam3"])
# print(emp_name)

# insert() method is used to add an element at a specific index in the list.
# emp_name=["aman", "shivam"]
# print(emp_name)
# emp_name.insert(1, "Iq-India")
# print(emp_name)

# pop() method is used to remove an element from the list based on index and it returns the removed element.
#by default it deletes & returns the last element of the list.
# my_list=[10,20,30,40,50]
# print(my_list)
# removed_element=my_list.pop(2)
# print("Removed element: ",removed_element)
# print("List after removal: ",my_list)

# remove() method is used to remove an element from the list based on value and it does not return anything.
# my_list=[10,20,30,40,50]
# print(my_list)
# my_list.remove(30)
# print("List after removal: ",my_list)


# clear() method is used to remove all elements from the list.
# my_list=[10,20,30,40,50]
# print(my_list)
# my_list.clear()
# print("List after clearing: ",my_list)

#reverse() method is used to reverse the order of elements in the list.
# my_list=[10,20,30,40,50]
# print(my_list)
# my_list.reverse()
# print("List after reversing: ",my_list)

#sort() method is used to sort the elements of the list in ascending order by default.
# my_list=[50,20,40,100,500,600,10,30]
# print(my_list)
# my_list.sort()
# print("List after sorting: ",my_list)
# my_list.sort(reverse=True)
# print("List after sorting in descending order: ",my_list)

#count() method is used to count the number of occurrences of a specific element in the list.
# my_list=[10,20,30,40,50,10,20,10]
# print(my_list)
# count=my_list.count(10)
# print("Number of occurrences of 10: ",count)

#universal functions
# sum() function is used to find the sum of all elements in the list.
#min() function is used to find the minimum element in the list.
# max() function is used to find the maximum element in the list.


my_list=[10,20,30,40,50]
print("Sum of all elements: ",sum(my_list))
print("Minimum element: ",min(my_list))
print("Maximum element: ",max(my_list))