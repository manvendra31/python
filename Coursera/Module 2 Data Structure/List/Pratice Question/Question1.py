# 1. Count how many times a number appears in a list 
# nums = [2, 3, 2, 5, 2, 7]
# Count how many times 2 appears
a=[2,3,2,5,2,7,2,2,5,6,9,8,2,6,9,2]

b = print(len(a))
count = 0
for i in a:
    if i==2:
        count = count+1
print(count)