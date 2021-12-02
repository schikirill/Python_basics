import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        for col in range(len(TrafficLight.__color)):
            if col == 0:
                print(TrafficLight.__color[col])
                time.sleep(7)
            if col == 1:
                print(TrafficLight.__color[col])
                time.sleep(2)
            if col == 2:
                print(TrafficLight.__color[col])
                time.sleep(5)
        print("\nDone")


crossroad = TrafficLight()
crossroad.running()
