from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine
from __init__ import CarFactory


class create_glissade(CarFactory):
    def __init__(self):
        self.engine = willoughby_engine.WilloughbyEngine()
        self.battery = spindler_battery.SpindlerBattery()
    
    def needs_service(self):
        return self.engine.needs_service and self.battery.needs_service()
