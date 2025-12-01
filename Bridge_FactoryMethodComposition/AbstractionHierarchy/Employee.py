from abc import ABC, abstractmethod
from FactoryMethod.PaymentFactory import PaymentImplementor

class Employee(ABC):
    
    def __init__(self, payment_implementor: PaymentImplementor):
        self.payment_implementor = payment_implementor

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def payout_salary(self):
        amount = self.calculate_salary()
        print(f"Paying {self.__class__.__name__}...", end=" ")
        self.payment_implementor.process_payment(amount)