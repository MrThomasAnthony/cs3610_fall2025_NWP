from abc import ABC, abstractmethod
from Product.Customer import Customer

class ICustomerBuilder(ABC):
    @property
    @abstractmethod
    def customer(self) -> Customer:
        pass

    @abstractmethod
    def build_first_name(self, first_name: str) -> None: pass

    @abstractmethod
    def build_middle_name(self, middle_name: str) -> None: pass

    @abstractmethod
    def build_last_name(self, last_name: str) -> None: pass

    @abstractmethod
    def build_primary_email(self, email: str) -> None: pass

    @abstractmethod
    def build_secondary_email(self, email: str) -> None: pass

    @abstractmethod
    def build_primary_mobile(self, number: str) -> None: pass

    @abstractmethod
    def build_secondary_mobile(self, number: str) -> None: pass