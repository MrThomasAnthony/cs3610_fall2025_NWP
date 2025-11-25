from Director.CustomerDirector import CustomerDirector
from ConcreteBuilders.WebAppBuilder import WebAppBuilder
from ConcreteBuilders.MobileAppBuilder import MobileAppBuilder
from Product.Customer import Customer

def main():
    form_data = {
        "first_name": "John",
        "middle_name": "Quincy",
        "last_name": "Adams",
        "p_email": "john.adams@example.com",
        "s_email": "john.private@example.com",
        "p_phone": "+1-555-0100",
        "s_phone": "+1-555-0200"
    }

    director = CustomerDirector()

    print("--- Scenario 1: Customer registered via Web App ---")
    web_builder = WebAppBuilder()
    director.builder = web_builder
    
    director.build_customer_profile(form_data)
    
    web_customer = web_builder.customer
    print(web_customer)

    print("\n--- Scenario 2: Customer registered via Mobile App ---")
    mobile_builder = MobileAppBuilder()
    director.builder = mobile_builder
    
    director.build_customer_profile(form_data)
    
    mobile_customer = mobile_builder.customer
    print(mobile_customer)
    
if __name__ == "__main__":
    main()