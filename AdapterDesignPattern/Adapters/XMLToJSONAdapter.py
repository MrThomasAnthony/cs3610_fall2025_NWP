import json
import xml.etree.ElementTree as ET
from TargetInterface.IFinanceDataProvider import FinancialDataProvider
from Adaptees.AccountingModule import AccountingModule

class XMLToJSONAdapter(FinancialDataProvider):
    def __init__(self, adaptee: AccountingModule):
        self.adaptee = adaptee

    def get_financial_data(self) -> str:
        # Get data from XML adaptee
        xml_data = self.adaptee.get_ledger_xml()
        
        # Convert XML to dict/list
        root = ET.fromstring(xml_data)
        json_list = []
        for entry in root.findall('entry'):
            record = {
                "id": entry.find('id').text,
                "amount": entry.find('amount').text,
                "type": entry.find('type').text
            }
            json_list.append(record)
            
        # Return as json String
        return json.dumps(json_list)