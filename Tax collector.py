print("Welcome to the Friendly Tax Calculator")
user_income = float(input("Enter your total income in birr:"))

def calculate_tax(income):
    tax = 0
    
    if income <= 2000:
        tax = 0
    elif income <= 4000:
        tax = (income - 2000) * 0.15
    elif income <= 7000:
        tax = (4000 - 2000) * 0.15 + (income - 4000) * 0.20
    elif income <= 10000:
        tax = (4000 - 2000) * 0.15 + (7000 - 4000) * 0.20 + (income - 7000) * 0.25
    elif income <= 14000:
        tax = (4000 - 2000) * 0.15 + (7000 - 4000) * 0.20 + (10000 - 7000) * 0.25 + (income - 10000) * 0.30
    else:  # income > 14000
        tax = (4000 - 2000) * 0.15 + (7000 - 4000) * 0.20 + (10000 - 7000) * 0.25 + (14000 - 10000) * 0.30 + (income - 14000) * 0.35
    
    net_income = income - tax
    return tax, net_income=


total_tax, net = calculate_tax(user_income)

print(f" Total Tax: {total_tax}birr")
print(f" Net Income After Tax: {net}birr")
