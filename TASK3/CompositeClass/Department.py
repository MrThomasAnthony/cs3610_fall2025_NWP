from typing import List
from ComponentInterface.IOrganizationComponent import IOrganizationComponent

class Department(IOrganizationComponent):
    # Represents a department that can hold employees or sub departments

    def __init__(self, name: str):
        self.name = name
        # A list to hold children components
        self._subordinates: List[IOrganizationComponent] = []

    def add(self, component: IOrganizationComponent):
        self._subordinates.append(component)

    def remove(self, component: IOrganizationComponent):
        self._subordinates.remove(component)

    def get_total_salary(self) -> float:
        # Sum of this department's direct overhead plus the salaries of all children
        
        total = 0.0
        for child in self._subordinates:
            total += child.get_total_salary()
        return total

    def do_operation(self, task: str) -> str:
        
        results = [f"🏢 Department [{self.name}] received task: '{task}'"]
        for child in self._subordinates:
            results.append(child.do_operation(task))
        return "\n".join(results)
