from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tireWearArray):
        self.tireWearArray = tireWearArray

    def needs_service(self):
        wearSum = 0.0
        for x in range(4):
            wearSum = wearSum + self.tireWearArray[x]
        return wearSum >= 3




