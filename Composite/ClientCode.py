from CompositeClass.Department import Department
from LeafClass.Employee import Employee

if __name__ == "__main__":
    # 1. Create Leaf nodes (Individual Employees)
    dev1 = Employee("Alice", "Backend Dev", 80000)
    dev2 = Employee("Bob", "Frontend Dev", 75000)
    designer = Employee("Charlie", "UI/UX", 70000)
    manager = Employee("Diana", "General Manager", 120000)

    # 2. Create Composite nodes (Departments/Teams)
    dev_team = Department("Development Team")
    design_team = Department("Design Team")
    head_office = Department("Head Office")

    # 3. Build the Tree Structure
    # Add employees to specific teams
    dev_team.add(dev1)
    dev_team.add(dev2)
    design_team.add(designer)

    # Add teams and the manager to the Head Office
    head_office.add(manager)
    head_office.add(dev_team)
    head_office.add(design_team)

    # 4. Perform Uniform Operations
    print("--- Salary Calculation ---")
    # We can ask for the salary of a single dev
    print(f"{dev1.name}'s Salary: ${dev1.get_total_salary()}")
    # Or the salary of the entire organization using the same method
    print(f"Total Company Salary Budget: ${head_office.get_total_salary()}")

    print("\n--- Task Assignment ---")
    # We can assign a task to the whole structure at once
    # The Head Office delegates to Teams, Teams delegate to Employees
    print(head_office.do_operation("Q3 Product Launch"))