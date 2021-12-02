class Road:
    def __init__(self, length_m, width_m, road_thikness_cm):
        self._length_m = length_m
        self._width_m = width_m
        self.one_cm_kg = 25
        self.road_thikness_cm = road_thikness_cm

    def road_mass(self):
        return print(self._length_m * self._width_m * self.one_cm_kg * self.road_thikness_cm / 1000)


m = Road(5000, 20, 5)
m.road_mass()
