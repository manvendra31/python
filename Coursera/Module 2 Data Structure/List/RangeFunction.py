# Range return the list


friends = ["Ankit","Nitesh","Raghvendra","Aniket"]

print(len(friends))

print(list(range(len(friends))))


# Loop in the list
'''
for friend in friends:
    print("Happy New Year",friend)
'''
for i in range(len(friends)):
    friend=friends[i]    
    print("Happy New Year",friend)