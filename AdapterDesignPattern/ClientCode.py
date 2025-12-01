from ForcastingModule.ForcastingModule import ForecastingFinanceModule
from Adapters.CSVToJSONAdapter import CSVToJSONAdapter
from Adapters.XMLToJSONAdapter import XMLToJSONAdapter
from Adapters.JSONAdapter import JSONAdapter
from Adaptees.TaxCalculator import TaxCalculator
from Adaptees.AccountingModule import AccountingModule
from Adaptees.CreditAuthorizationService import CreditAuthorizationService

# Example Usage
if __name__ == "__main__":
    # Initialize the various financial systems - adaptees
    tax_system = TaxCalculator()
    acc_system = AccountingModule()
    credit_system = CreditAuthorizationService()

    # Initialize the Forecasting Module - client
    forecasting_app = ForecastingFinanceModule()

    # use adapters to integrate different systems
    
    # Adapter for CSV
    tax_adapter = CSVToJSONAdapter(tax_system)
    forecasting_app.integrate_and_process(tax_adapter)

    # Adapter for XML
    acc_adapter = XMLToJSONAdapter(acc_system)
    forecasting_app.integrate_and_process(acc_adapter)

    # Adapter for JSON
    credit_adapter = JSONAdapter(credit_system)
    forecasting_app.integrate_and_process(credit_adapter)