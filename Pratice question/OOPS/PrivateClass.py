class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private
        self.__model = model  # private

    # Getter method
    def get_brand(self):
        return self.__brand

    # Setter method
    def set_brand(self, brand):
        self.__brand = brand

car1 = Car("Toyota", "Corolla")
# print(car1.__brand)  # ❌ This will give an error

print(car1.get_brand())  # ✅ Access via getter
car1.set_brand("Honda")
print(car1.get_brand())
