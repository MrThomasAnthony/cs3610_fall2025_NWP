from abc import ABC, abstractmethod
from typing import List

# 1. The Component Interface
class IOrganizationComponent(ABC):
    # The common interface for both Employees and Departments.

    @abstractmethod
    def get_total_salary(self) -> float:
        pass

    @abstractmethod
    def do_operation(self, task: str) -> str:
        pass

    def add(self, component: 'IOrganizationComponent'):
        pass

    def remove(self, component: 'IOrganizationComponent'):
        pass

