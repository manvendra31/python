# Here is the a bank valut of the family example

class Valut:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.knuts=knuts
        self.sickles=sickles

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"    

    def __add__(self,other):
        galleons=self.galleons + other.galleons
        sickles=self.sickles + other.sickles
        knuts=self.knuts + other.knuts
        return Valut(galleons,sickles,knuts)


potter=Valut(100,50,25)
print(potter)        

weasley = Valut(25,50,100)
print(weasley)

nesty = Valut(1,2,3)
print(nesty)

total = potter + weasley   + nesty
print(total)
