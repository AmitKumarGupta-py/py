from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self._status = 'off'

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device: {self._name}, Status: {self._status}"


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("SmartLight")
        self._brightness = 0

    def turn_on(self):
        self._status = 'on'
        return "Smart light is now on."

    def turn_off(self):
        self._status = 'off'
        return "Smart light is now off."

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self._brightness = level
            return f"Brightness set to {level}%."
        else:
            return "Invalid brightness level. Please enter a value between 0 and 100."


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("SmartThermostat")
        self._temperature = 0

    def turn_on(self):
        self._status = 'on'
        return "Smart thermostat is ON"

    def turn_off(self):
        self._status = 'off'
        return "Smart thermostat is OFF"

    def set_temperature(self, temp):
        self._temperature = temp
        return f"Temperature set to {temp}°C."



light = SmartLight()
print(light.device_info())
print(light.turn_on())
print(light.set_brightness(70))
print(light.device_info())
print(light.turn_off())
print(light.device_info())

thermostat = SmartThermostat()
print(thermostat.device_info())
print(thermostat.turn_on())
print(thermostat.set_temperature(22))
print(thermostat.device_info())
print(thermostat.turn_off())
print(thermostat.device_info())
