from BuilderInterface.ICustomerBuilder import ICustomerBuilder
from Product.Customer import Customer

class MobileAppBuilder(ICustomerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._customer = Customer()

    @property
    def customer(self) -> Customer:
        product = self._customer
        self.reset()
        return product

    def build_first_name(self, first_name: str) -> None:
        self._customer.first_name = first_name

    # Mobile App, no middle name
    def build_middle_name(self, middle_name: str) -> None:
        pass 

    def build_last_name(self, last_name: str) -> None:
        self._customer.last_name = last_name

    def build_primary_email(self, email: str) -> None:
        self._customer.primary_email = email

    # Mobile App, no secondary email
    def build_secondary_email(self, email: str) -> None:
        pass

    def build_primary_mobile(self, number: str) -> None:
        self._customer.primary_mobile = number

    # Mobile App, no secondary mobile
    def build_secondary_mobile(self, number: str) -> None:
        pass