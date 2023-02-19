class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.hunger = 0
        self.energy = 100

    def meow(self):
        print("Meow!")

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.energy = 100

    def play(self):
        if self.energy >= 20:
            print(f"{self.name} is playing with a ball of yarn!")
            self.energy -= 20
            self.hunger += 10
        else:
            print(f"{self.name} is too tired to play")

    def feed(self):
        if self.hunger > 0:
            print(f"{self.name} is eating some delicious food!")
            self.hunger = 0
            self.energy += 10
        else:
            print(f"{self.name} is not hungry right now")
