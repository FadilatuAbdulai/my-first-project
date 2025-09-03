# Assignment 1: Smartphone Class with Inheritance and Encapsulation

class Device:   # Parent class
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):   # Child class (inherits from Device)
    def _init_(self, brand, model, storage, battery):
        super()._init_(brand, model)   # Call parent constructor
        self.__storage = storage         # Encapsulation: private attribute
        self.battery = battery
    
    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo 📸"
    
    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model} ☎"
    
    def get_storage(self):       # Encapsulated getter
        return f"Storage: {self.__storage}GB"
    
    def upgrade_storage(self, extra):
        self.__storage += extra
        return f"Upgraded storage to {self.__storage}GB"


# Create objects
phone1 = Smartphone("Samsung", "S24 Ultra", 256, "5000mAh")
phone2 = Smartphone("iPhone", "15 Pro", 128, "4200mAh")

print(phone1.info())
print(phone1.take_photo())
print(phone1.get_storage())
print(phone1.upgrade_storage(128))
print(phone2.call("‪+233599353050‬"))