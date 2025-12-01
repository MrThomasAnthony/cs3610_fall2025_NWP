class AccountingModule:
    def get_ledger_xml(self):
        # Simulating xml return data
        return """
        <ledger>
            <entry>
                <id>101</id>
                <amount>1200.50</amount>
                <type>asset</type>
            </entry>
            <entry>
                <id>102</id>
                <amount>300.00</amount>
                <type>liability</type>
            </entry>
        </ledger>
        """