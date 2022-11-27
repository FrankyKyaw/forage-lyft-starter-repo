from battery.battery import Battery
from datetime import datetime
from utils import add_years_to_date

class NubbinBattery(Battery):

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self) -> bool:
        service_threshold_date = add_years_to_date(self.last_service_date, 4)
        return service_threshold_date < self.current_date