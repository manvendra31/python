# We return one tuple
'''
def main():
    student=get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name=input("Name:- ")
    house=input("House:- ")
    return (name, house)

if  __name__=="__main__":
    main()
'''

# So, the main question is that why we used this so answer is that is no one is can the structure 
# like manvendra is from jaipur but actually manvendra is from bodwal so overcome the this type issue we can used 
# the class no one can changed the structure now we see how we code

def main():
    student=get_student()
    if student[0]=="Ramu":
        student[1]="Jaipur"    # 
    print(f"{student[0]} from {student[1]}")

def get_student():
    name=input("Name:- ")
    house=input("House:- ")
   # return (name, house)   # Here if we run the code and assign ramu otherthen jaipur if throw an error
    return[name, house]   # Now it can automatically correct that ramu is from jaipur


if  __name__=="__main__":
    main()