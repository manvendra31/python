try:
    score = int(input("Score: "))
    if score <=100:
        print("Score is valid")
        if score >=90:
            print("Grade A")
        elif score >=80:
            print("Grade B")    
        elif score >=70:
            print("Grade C")  
        elif score >=60:
            print("Grade B")      
        else:
            print("Grade F")    
    else:
        print("Score is invalid")    
except ValueError:
    print("Please give a valid integer")        