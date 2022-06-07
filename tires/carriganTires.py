from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tireWearArray):
        self.tireWearArray = tireWearArray

    def needs_service(self):
        for x in range(4):
            if self.tireWearArray[x] >= 0.9:
                return True
        return False
