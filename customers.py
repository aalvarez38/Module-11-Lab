#customers.py
#author: [Abigail Alvarez]
# Module 11 lab: Customer Dictionary & Lookup
#reflection questions:
#1. .get() is usuable without a key but bracket notation it will raise an error without a key.
#2. Excel can crash with large amounts of data. Also, Excel takes so much space up. Compared to python that can handle mass amounts of information and can be automated.
print("--- Excercise 1--- ")
customer = {
    "name": "Alice", #Key : value,
    "name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- Excercise 2 ---")
customer["phone"] = "555-555"
print(customer)
customer["tier"] = "platnium"
print(customer)
del customer["name"]
print(customer)

print(customer.get("ytd_spend",0))

print("--- Excercise 3 ---")
print(customer.get("email","no email on file"))

#try:
    #print(customer.get("email", "no email on file"))

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--- Excercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver":0.05,
    "gold": 0.1,
    "platnium": 0.15,
    }

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0 )
final_price = purchase * (1-discount_rate)
print(f"Tier: {customer["tier"]}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Excercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},

]

print("--- Excercise 7 ---")
catalog = {
        "Widget A": {"price": 9.99, "stock": 150},
        "Gadget C": {"price": 49.99, "stock": 8},
}
for name, details in catalog.items():
    if details["stock"] <20:
        print(f"LOW STOCK: {name} - only {details["stock"]} left")

print("--- Excercise 8 ---")
transations = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transations:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region [region] = sales_by_region.get(region, 0) + amount