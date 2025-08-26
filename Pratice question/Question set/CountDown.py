#Countdown the second

a = int(input("Enter the number:\n"))
i=a
if a>=60:
    print("Enter the value less then one minutes")
else:    
    while i>=0:
        print(f"Time remaining: {i} second")
        i=i-1
