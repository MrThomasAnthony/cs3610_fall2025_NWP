from FactoryMethod.PaymentFactory import PaymentFactory
from AbstractionHierarchy.HourlyEmployee import HourlyEmployee
from AbstractionHierarchy.SalariedEmployee import SalariedEmployee
from AbstractionHierarchy.Contractor import Contractor


if __name__ == "__main__":
    # Use Factory to create payment methods
    try:
        bank_method = PaymentFactory.create_payment_method("bank")
        wallet_method = PaymentFactory.create_payment_method("wallet")
        cheque_method = PaymentFactory.create_payment_method("cheque")
    except ValueError as e:
        print(e)
        exit()

    # Create Employees bridging to Payment Methods
    
    # Hourly Employee paid via Wallet
    worker1 = HourlyEmployee(wallet_method, rate=20, hours=160)
    
    # Salaried Employee paid via Bank Transfer
    worker2 = SalariedEmployee(bank_method, monthly_salary=5000)
    
    # Contractor paid via Cheque
    worker3 = Contractor(cheque_method, project_fee=3500)
    
    # Changing a payment method dynamically
    # say worker 1 wants to switch to Cheque
    print("\n--- Processing Payroll ---")
    worker1.payout_salary()
    worker2.payout_salary()
    worker3.payout_salary()
    
    print("\n--- Switching Worker 1 to Cheque ---")
    worker1.payment_implementor = cheque_method
    worker1.payout_salary()