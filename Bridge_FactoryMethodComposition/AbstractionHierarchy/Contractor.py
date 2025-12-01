from AbstractionHierarchy.Employee import Employee

class Contractor(Employee):
    def __init__(self, payment_implementor, project_fee):
        super().__init__(payment_implementor)
        self.project_fee = project_fee

    def calculate_salary(self) -> float:
        return self.project_fee