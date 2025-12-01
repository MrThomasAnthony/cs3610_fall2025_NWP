import json
from TargetInterface.IFinanceDataProvider import FinancialDataProvider    

class ForecastingFinanceModule:
    
    def integrate_and_process(self, source: FinancialDataProvider):
        raw_json = source.get_financial_data()
        
        # Parse JSON
        data = json.loads(raw_json)
        
        print(f"Processing Data from {source.__class__.__name__}")
        print(f"Raw JSON received: {raw_json}")
        print(f"Parsed Python Obj: {data}")
        print("Forecast calculation complete.\n")