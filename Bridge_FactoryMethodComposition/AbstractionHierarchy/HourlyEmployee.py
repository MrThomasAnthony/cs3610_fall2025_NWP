from AbstractionHierarchy.Employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, payment_implementor, rate, hours):
        super().__init__(payment_implementor)
        self.rate = rate
        self.hours = hours

    def calculate_salary(self) -> float:
        return self.rate * self.hours