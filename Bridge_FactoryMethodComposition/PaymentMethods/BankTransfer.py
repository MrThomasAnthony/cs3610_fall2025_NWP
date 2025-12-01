from FactoryMethod.PaymentFactory import PaymentImplementor

class BankTransfer(PaymentImplementor):
    def process_payment(self, amount: float):
        print(f"Processing BANK TRANSFER of ${amount:.2f}")

