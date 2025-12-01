import xml.etree.ElementTree as ET
from TargetInterface.IFinanceDataProvider import FinancialDataProvider
from Adaptees.CreditAuthorizationService import CreditAuthorizationService

class JSONAdapter(FinancialDataProvider):
    def __init__(self, adaptee: CreditAuthorizationService):
        self.adaptee = adaptee

    def get_financial_data(self) -> str:
        # Get data from json adaptee - already in json format
        return self.adaptee.fetch_credit_history_json()