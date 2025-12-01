import json

class CreditAuthorizationService:
    def fetch_credit_history_json(self):
        # Already returns json, but method name is incompatible
        data = [
            {"id": 500, "amount": 10000, "status": "approved"},
            {"id": 501, "amount": 500, "status": "pending"}
        ]
        return json.dumps(data)