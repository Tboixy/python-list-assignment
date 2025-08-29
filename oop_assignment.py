# ===============================
# Assignment 1: Design Your Own Class
# ===============================

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def call(self, number):
        return f"📞 Calling {number} from {self.model}..."

    def charge(self, hours):
        self.battery_life += hours
        return f"🔋 {self.model} charged for {hours} hours. Battery life is now {self.battery_life}h."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery_life}h battery)"


# Child class (Inheritance Example)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    def play_game(self, game):
        return f"🎮 Playing {game} on {self.model} with {self.gpu} GPU."

    # Polymorphism: overriding __str__
    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition, {self.storage}GB, GPU: {self.gpu})"


# ===============================
# Activity 2: Polymorphism Challenge
# ===============================

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


# ===============================
# Main Program
# ===============================

if __name__ == "__main__":
    # Test Smartphone
    phone1 = Smartphone("Samsung", "Galaxy S24", 256, 20)
    print(phone1)
    print(phone1.call("+254712345678"))
    print(phone1.charge(2))

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 18, "Adreno 740")
    print(gaming_phone)
    print(gaming_phone.play_game("Call of Duty Mobile"))

    # Test Vehicles
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
