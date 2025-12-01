from abc import ABC, abstractmethod

class FinancialDataProvider(ABC):
    
    @abstractmethod
    def get_financial_data(self) -> str:
        pass