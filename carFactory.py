from abc import ABC, abstractmethod
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoPrimeTire
from car import Car

class CarFactory:
    """Factory that creates a combination of engine, battery and tire"""

    def create_calliope(sensor_array, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTire(sensor_array)
        car = Car(engine, battery,tire)
        return car

    def create_glissade(sensor_array, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTire(sensor_array)
        car = Car(engine, battery,tire)
        return car

    def create_palindrome(sensor_array, current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTire(sensor_array)
        car = Car(engine, battery,tire)
        return car

    def create_rorschach(sensor_array, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tire = OctoPrimeTire(sensor_array)
        car = Car(engine, battery,tire)
        return car

    def create_Thovex(sensor_array, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tire = OctoPrimeTire(sensor_array)
        car = Car(engine, battery,tire)
        return car
