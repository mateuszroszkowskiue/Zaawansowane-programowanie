class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, adress, plot):
        super().__init__(area, rooms, price, adress)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom: \n"
            f"Powierzchnia: {self.area} m^2 \n"
            f"Liczba pokoi: {self.rooms} \n"
            f"Cena: {self.price} PLN \n"
            f"Adres: {self.address} \n"
            f"Rozmiar działki: {self.plot} m^2"  
        )

class Flat(Property):
    def __init__(self, area, rooms, price, adress, floor):
        super().__init__(area, rooms, price, adress)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie: \n"
            f"Powierzchnia: {self.area} m^2 \n"
            f"Liczba pokoi: {self.rooms} \n"
            f"Cena: {self.price} PLN \n"
            f"Adres: {self.address} \n"
            f"Piętro: {self.floor}"
        ) 

# house1 = House(area=100, rooms=5, price=800000, adress="Warszawska 4", plot=300)
house1 = House(100, 5, 800000, "Warszawska 4", 300)
flat1 = Flat(70, 4, 600000, "Młynarska 15", 14)

print(house1)
print("\n")
print(flat1)