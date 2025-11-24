from typing import Any, Dict
from BuilderInterface.ICustomerBuilder import ICustomerBuilder


class CustomerDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> ICustomerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ICustomerBuilder) -> None:
        self._builder = builder

    def build_customer_profile(self, data: Dict[str, Any]) -> None:
        self.builder.build_first_name(data.get("first_name"))
        self.builder.build_middle_name(data.get("middle_name"))
        self.builder.build_last_name(data.get("last_name"))
        self.builder.build_primary_email(data.get("p_email"))
        self.builder.build_secondary_email(data.get("s_email"))
        self.builder.build_primary_mobile(data.get("p_phone"))
        self.builder.build_secondary_mobile(data.get("s_phone"))