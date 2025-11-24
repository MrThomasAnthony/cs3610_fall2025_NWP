class Customer:
    def __init__(self) -> None:
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.primary_email = None
        self.secondary_email = None
        self.primary_mobile = None
        self.secondary_mobile = None

    def __str__(self) -> str:
        return (f"Customer Details:\n"
                f"  Name: {self.first_name} {self.middle_name if self.middle_name else ''} {self.last_name}\n"
                f"  Emails: Primary({self.primary_email}), Secondary({self.secondary_email})\n"
                f"  Phones: Primary({self.primary_mobile}), Secondary({self.secondary_mobile})")