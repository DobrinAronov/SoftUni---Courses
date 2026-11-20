from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str | None = None
        self.ram: int | None = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def available_processor(self) -> dict[str, int]:
        pass

    @property
    @abstractmethod
    def max_ram(self) -> int:
        pass

    @property
    def valid_ram(self):
        return tuple(2 ** power for power in range(1, int(log2(self.max_ram)) + 1))

    def configure_computer(self, processor: str, ram: int) -> str:
        if processor not in self.available_processor:
            raise ValueError(f"{processor} is not compatible with"
                             f" {self.__str__()} {self.manufacturer} {self.model}!")

        if ram not in self.valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with"
                             f" {self.__str__()} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        processor_price = self.available_processor[processor]
        ram_price = int(log2(ram) * 100)
        self.price = processor_price + ram_price

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
