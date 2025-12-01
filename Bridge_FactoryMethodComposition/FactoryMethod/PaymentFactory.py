from PaymentMethods.PaymentImplementor import PaymentImplementor
from PaymentMethods.BankTransfer import BankTransfer
from PaymentMethods.Cheque import Cheque
from PaymentMethods.DigitalWallet import DigitalWallet

class PaymentFactory:
    # Factory to create PaymentImplementor instances based on a key/string.
    
    @staticmethod
    def create_payment_method(method_type: str) -> PaymentImplementor:
        methods = {
            "bank": BankTransfer,
            "cheque": Cheque,
            "wallet": DigitalWallet
        }
        
        method_class = methods.get(method_type.lower())
        if method_class:
            return method_class()
        else:
            raise ValueError(f"Unknown payment method: {method_type}")