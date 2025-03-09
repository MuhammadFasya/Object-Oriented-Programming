class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate  # Harga sewa per hari

    def calculate_rental(self, days):
        return self.rental_rate * days  # Harga total berdasarkan jumlah hari

    def show_details(self):
        return f"Vehicle: {self.brand} {self.model}, Rate: ${self.rental_rate}/day"


class Car(Vehicle):
    def __init__(self, brand, model, rental_rate, trunk_capacity):
        super().__init__(brand, model, rental_rate)
        self.trunk_capacity = trunk_capacity  # Kapasitas bagasi

    def open_trunk(self):
        return f"Opening trunk with capacity: {self.trunk_capacity} liters"


class Bike(Vehicle):
    def __init__(self, brand, model, rental_rate, engine_cc):
        super().__init__(brand, model, rental_rate)
        self.engine_cc = engine_cc  # Kapasitas mesin dalam cc

    def kickstart(self):
        return f"Kickstarting the {self.brand} {self.model} with {self.engine_cc}cc engine"


class LuxuryFeatures:
    def enable_gps(self):
        return "GPS enabled"

    def enable_heated_seats(self):
        return "Heated seats enabled"


class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, rental_rate, trunk_capacity, luxury_fee=50):
        super().__init__(brand, model, rental_rate, trunk_capacity)
        self.luxury_fee = luxury_fee  # Biaya tambahan untuk fitur mewah

    def calculate_rental(self, days):
        return super().calculate_rental(days) + (self.luxury_fee * days)  # Harga rental dengan biaya tambahan

    def show_details(self):
        return super().show_details() + f", Luxury Fee: ${self.luxury_fee}/day"


# Simulasi Penyewaan Kendaraan
vehicles = [
    Car("Toyota", "Camry", 40, 500),
    Bike("Honda", "CBR", 20, 150),
    LuxuryCar("BMW", "Series 7", 100, 600)
]

print("\nAvailable Vehicles:")
for v in vehicles:
    print(v.show_details())

# Contoh penyewaan kendaraan
days = 3
print("\nRental Costs for 3 Days:")
for v in vehicles:
    print(f"{v.brand} {v.model}: ${v.calculate_rental(days)}")

# Contoh penggunaan fitur unik
print("\nFeature Demonstrations:")
print(vehicles[0].open_trunk())  # Car feature
print(vehicles[1].kickstart())   # Bike feature
print(vehicles[2].enable_gps())  # LuxuryCar feature
print(vehicles[2].enable_heated_seats())  # LuxuryCar feature
