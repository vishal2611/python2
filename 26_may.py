#List
#Listis a data structure in Python that is mutable, ordered, and allows duplicate elements. 
# It is defined using square brackets [] and can contain elements of different data types.
#List can be heterogeneous, meaning it can contain elements of different data types, such as integers, strings, and even other lists.
#List can be homogeneous, meaning it can contain elements of the same data type, such as all integers or all strings.
#List is mutable, which means you can modify its elements after it has been created.
#List is ordered, which means that the elements in a list have a specific order and can be accessed using their index.
#List allows duplicate elements, which means that you can have multiple occurrences of the same element in a list.
#List can be nested, which means that you can have lists within lists, creating a hierarchical structure.
#total index = length of list - 1

marks_10th=[20,55,60,76,50,60,"hello",5.5]
print("Before update: ",marks_10th)
marks_10th[0]=200
print("After update: ",marks_10th)