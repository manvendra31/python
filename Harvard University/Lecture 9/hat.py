import random

class Hat:
    def __init__(self):
        self.house=["Basti","Sant Kabir Nagar","Gorakhpur","Lucknow"]

    def sort(self,name):
        print(name, "is in", random.choice(self.house)) 


hat = Hat()

hat.sort("Harry")