# radio_OOP_model.py

# This file contains the model of an Object Oriented example program, of a radio network.

# Import root abstract class.
from abc import ABC, abstractmethod


class subscriber(ABC):
    def __init__(self, key: int = 0, manufacturer: str = "NA", model: str = "NA", serial: int = 0):
        self.__mykey = key
        self.__mymanufacturer = manufacturer
        self.__mymodel = model
        self.__myserial = serial

    # Get subscriber Key
    @property
    def key(self) -> int:
        return self.__mykey

    # Set subscriber Key
    @key.setter
    def key(self, key: int) -> int:
        self.__mykey = key
        return self.__mykey
    
    # Get subscriberManufacturer
    @property
    def manufacturer(self) -> str:
        return self.__mymanufacturer
    
    # Get subscriberModel
    @property
    def model(self) -> str:
        return self.__mymodel
    
    # Get subscriber Serial Number
    @property
    def serial(self) -> int:
        return self.__myserial

class mobile(subscriber):
    def __init__(self, key, manufacturer, model, serial):
        super().__init__(key, manufacturer, model, serial)
        self.__mytype: str = "mobile"

    @property
    def type(self) -> str:
        return self.__mytype 

class portable(subscriber):
    pass

class basestation(ABC):
    pass

class controller(ABC):
    pass



# Testing
DMR1 = mobile(1234, "Tait Communications", "DMR1000", 5001)
assert DMR1.key == 1234
assert DMR1.manufacturer == "Tait Communications"
assert DMR1.model == "DMR1000"
assert DMR1.serial == 5001
assert DMR1.type == "mobile"


print(DMR1.key)
print(DMR1.manufacturer)
print(DMR1.model)
print(DMR1.serial)
print(DMR1.type)
