from ComponentInterface.IOrganizationComponent import IOrganizationComponent

class Employee(IOrganizationComponent):
    # Represents an individual employee

    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_total_salary(self) -> float:
        return self.salary

    def do_operation(self, task: str) -> str:
        return f"  - Employee {self.name} ({self.position}) is working on: {task}"

    def add(self, component: 'IOrganizationComponent'):
        print("Cannot add to an individual employee.")

    def remove(self, component: 'IOrganizationComponent'):
        print("Cannot remove from an individual employee.")
