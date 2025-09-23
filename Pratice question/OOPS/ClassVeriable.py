# Here we can can see the class veriable 

class Mobile:
    company_name = "Samsung"   # <-- Class Variable (same for all)

    def __init__(self, model, launch):
        self.model = model     # <-- Instance Variable
        self.launch = launch   # <-- Instance Variable

    def __str__(self):
        return f"{Mobile.company_name} {self.model} launched in {self.launch}"


# Create objects
mobile1 = Mobile("S23", 2024)
mobile2 = Mobile("S24", 2025)

print(mobile1.model)   # Samsung S23 launched in 2024
print(mobile2.model)   # Samsung S24 launched in 2025

# Update instance variable (affects only mobile1)
mobile1.model = "S25"

print(mobile1.model)   # Samsung S25 launched in 2024
print(mobile2.model)   # Samsung S24 launched in 2025


print(mobile1)
print(mobile2)
