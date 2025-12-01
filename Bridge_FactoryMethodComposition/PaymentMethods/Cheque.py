from FactoryMethod.PaymentFactory import PaymentImplementor

class Cheque(PaymentImplementor):
    def process_payment(self, amount: float):
        print(f"Issuing CHEQUE for ${amount:.2f}")
