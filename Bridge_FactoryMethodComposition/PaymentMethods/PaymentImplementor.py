from abc import ABC, abstractmethod

class PaymentImplementor(ABC):
    """
    The Implementation Interface.
    Defines how the actual payment processing is performed.
    """
    @abstractmethod
    def process_payment(self, amount: float):
        pass