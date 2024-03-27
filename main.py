class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} is eating")
        self.power += 1

    def hit(self):
        print(f"{self.name} is hits")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} is walking")

    def info(self):
        print(f"Warrior's name - {self.name}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Power: {self.power}")
        print(f"Endurance: {self.endurance}")
