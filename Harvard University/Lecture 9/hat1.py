import random

class Hat:

    house=["Basti","Sant Kabir Nagar","Gorakhpur","Lucknow"]

    @classmethod

    def sort(cls,name):
        print(name, "is in", random.choice(cls.house)) 


Hat.sort("Harry")