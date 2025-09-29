# Here is the a bank valut of the family example

class Valut:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.knuts=knuts
        self.sickles=sickles

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"    


potter=Valut(100,50,25)
print(potter)        

weasley = Valut(25,50,100)
print(weasley)


galleons = potter.galleons + weasley.galleons

sickles = potter.sickles + weasley.sickles

knuts = potter.knuts + weasley.knuts

print(galleons,sickles,knuts)


# The above method is the too long to add the above two object sum now we can do anothor method by OperatorOverloading

