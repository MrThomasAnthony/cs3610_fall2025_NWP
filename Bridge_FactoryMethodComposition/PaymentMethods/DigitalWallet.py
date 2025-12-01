from FactoryMethod.PaymentFactory import PaymentImplementor

class DigitalWallet(PaymentImplementor):
    def process_payment(self, amount: float):
        print(f"Transferring ${amount:.2f} to DIGITAL WALLET")