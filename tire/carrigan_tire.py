from tire.tire import Tire

class CarriganTire(Tire):

    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self) -> bool:
        for i in self.sensor_array:
            if i >= 0.9:
                return True
        return False