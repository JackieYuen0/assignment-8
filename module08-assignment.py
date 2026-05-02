# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services

services = {"Web Development": 150,
           "Data Analysis": 175,
           "Repairs": 50,
           "Gardening": 90,
           "Database Management": 120,
            "Cleaning": 20}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {"company_name": "ABC Corp",
             "contact_person": "John Smith",
             "email": "john@gmail.com",
             "phone": 4032344103}

customer2 = {"company_name": "BBC Corp",
             "contact_person": "De Zed",
             "email": "De@gmail.com",
             "phone": 7547547542}

customer3 = {"company_name": "CNN Corp",
             "contact_person": "Cras Wed",
             "email": "Cras@gmail.com",
             "phone": 2041234953}

customer4 = {"company_name": "Weawea Corp",
             "contact_person": "bua cem",
             "email": "bua@gmail.com",
             "phone": 5672837485}
# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}

customers = {"C001": customer1,
             "C002": customer2,
             "C003": customer3,
             "C004": customer4}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
print(customers)


# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers.get("C002")
c003_contact = customers.get("C003").get("contact_person")
c999_info = customers.get("C999", "error")
print(c002_info, c003_contact, c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = 1234567890
customers["C002"]["industry"] = "Technology"
print(customers["C001"], customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here

project1 = {"name": "Anac", "service": "Repairs", "hours": 40, "budget": 9000}
project2 = {"name": "jack", "service": "Repairs", "hours": 40, "budget": 2000}
project3 = {"name": "Healing", "service": "Repairs", "hours": 40, "budget": 15555}
project4 = {"name": "Watering", "service": "Gardening", "hours": 40, "budget": 1200}
project5 = {"name": "Culling", "service": "Gardening", "hours": 30, "budget": 10000}
projects = {"C001": [project1, project2],
            "C002": [project3],
            "C003": [project4],
            "C004": [project5]}
projects_list = []
for values in list(projects.values()):
    for project in values:
        projects_list.append(project)

print(projects_list)

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for project in projects_list:
    print(project["hours"] * project["budget"])

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print(customers.keys())
for person in list(customers.values()):
    print(person["company_name"])
print(len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {"Repairs": 0,
                  "Gardening": 0}
for project in projects_list:
    if project["service"] == "Repairs":
        service_counts["Repairs"] += 1
    if project["service"] == "Gardening":
        service_counts["Gardening"] += 1
print(service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
total_hours = 0
total_projects = 0
total_budget = 0
max_budget = 0
min_budget = float('inf')
for things in list(projects.values()):
    for event in things:
        total_hours += event["hours"]
        total_budget += event["budget"]
        total_projects += 1
        if event["budget"] > max_budget:
            max_budget = event["budget"]
        if event["budget"] < min_budget:
            min_budget = event["budget"]


avg_budget = total_budget/total_projects

print(total_hours, total_projects, total_budget, max_budget, min_budget, avg_budget)


# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer in customers:
    print(customers[customer])
    customer_hours = 0
    customer_budget = 0
    for project in projects[customer]:
        customer_hours += project["hours"]
        customer_budget += project["budget"]
    print(customer_hours, customer_budget)

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {key: customers[key] for key in projects.keys()}
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {customer_id: 0 for customer_id in projects.keys()}
for guy in projects:
    for guy_projects in projects[guy]:
        customer_budgets[guy] += guy_projects["budget"]
print(customer_budgets)
# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
tier1 = {service: "Premium" for service, rate in services.items() if rate >= 200}
tier2 = {service: "Standard" for service, rate in services.items() if 200> rate >= 100}
tier3 = {service: "Basic" for service, rate in services.items() if rate < 100}
service_tiers = {**tier1, **tier2, **tier3}
print(service_tiers)
# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
test = {"bazinga": 12}
def validate_customer(customer_dict):
    if customer_dict.get("company_name", False) == False:
        return False
    if customer_dict.get("contact_person", False) == False:
        return False
    if customer_dict.get("email", False) == False:
        return False
    if customer_dict.get("phone", False) == False:
        return False
    return True
print(validate_customer(customer1))
print(validate_customer(customer2))
print(validate_customer(customer3))
print(validate_customer(customer4))


# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):
    new_dictionary = {}
    for pros in projects_dict:
        new_dictionary[pros] = {"total": 0, "average":0, "count":0}
        for tasks in projects_dict[pros]:
            new_dictionary[pros]["total"] += tasks["budget"]
            new_dictionary[pros]["count"] += 1
            new_dictionary[pros]["average"] = new_dictionary[pros]["total"]/new_dictionary[pros]["count"]
    return new_dictionary
print(analyze_customer_budgets(projects))

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here