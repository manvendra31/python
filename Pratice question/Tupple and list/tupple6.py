'''
Exercise 3: Sum and average of all numbers in a list
Calculate and print the sum and average of all numbers in a list.

Given:

my_list = [10, 20, 30, 40, 50]
Expected Output:

Sum: 150
Average: 30.0
'''

my_list = [10, 20, 30, 40, 50]

for i in my_list:
    b=len(my_list)
    a=i
    i=a+i
print(i)
print(i/b)