class Car:
    def __init__(self, max_speed, speed_unit):
        self.first = max_speed
        self.second = speed_unit
        print(f"Car with the maximum speed of {self.first} {self.second}")
    pass


class Boat:
    def __init__(self, max_speed):
        self.first = max_speed
        print(f"Boat with the maximum speed of {self.first} knots")
    pass


q = int(input())
queries = []
for _ in range(q):
    args = input().split()
    vehicle_type, params = args[0], args[1:]
    if vehicle_type == "car":
        max_speed, speed_unit = int(params[0]), params[1]
        vehicle = Car(max_speed, speed_unit)
    elif vehicle_type == "boat":
        max_speed = int(params[0])
        vehicle = Boat(max_speed)
    else:
        raise ValueError("invalid vehicle type")
