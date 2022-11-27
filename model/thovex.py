from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine
from __init__ import CarFactory


class create_thovex(CarFactory):
    def __init__(self):
        self.engine = capulet_engine.CapuletEngine()
        self.battery = nubbin_battery.NubbinBattery()
    
    def needs_service(self):
        return self.engine.needs_service and self.battery.needs_service()
