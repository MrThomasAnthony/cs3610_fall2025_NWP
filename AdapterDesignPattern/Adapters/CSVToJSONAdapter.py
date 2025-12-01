import csv
import json
import io
from TargetInterface.IFinanceDataProvider import FinancialDataProvider
from Adaptees.TaxCalculator import TaxCalculator

class CSVToJSONAdapter(FinancialDataProvider):
    def __init__(self, adaptee: TaxCalculator):
        self.adaptee = adaptee

    def get_financial_data(self) -> str:
        # Get data from csv adaptee
        csv_data = self.adaptee.get_tax_history_csv()
        
        # Convert csv to dict/list
        json_list = []
        # Use io.StringIO to treat the string like a file for the CSV reader
        csv_file = io.StringIO(csv_data)
        reader = csv.DictReader(csv_file)
        for row in reader:
            json_list.append(row)
            
        # Return as json String
        return json.dumps(json_list)
