class TrafficLight:
    def __init__(self):
        self.color = "red"
        self.time = 10

    def change_color(self):
        if self.color == "red":
            self.color = "green"
        else:
            self.color = "red"

class Car:
    def __init__(self, speed):
        self.speed = speed
        self.traffic_light = TrafficLight()

    def check_traffic_light(self):
        if self.traffic_light.color == "green":
            print("Світло зелене. Можна їхати.")
        else:
            print("Світло червоне. Зупиніться і дочекайтеся зеленого світла.")