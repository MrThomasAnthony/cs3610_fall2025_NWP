from AbstractionHierarchy.Employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, payment_implementor, monthly_salary):
        super().__init__(payment_implementor)
        self.monthly_salary = monthly_salary

    def calculate_salary(self) -> float:
        return self.monthly_salary