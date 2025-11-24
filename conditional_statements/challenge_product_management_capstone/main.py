# Input variables
product_type = "Perishable"
days_until_expiration = 8
stock_level = 50 
if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    elif (days_until_expiration >=4 and days_until_expiration <=6) and stock_level >50:
        print("20% discount applied")
    elif days_until_expiration >=7 and stock_level <= 50:
        print("10% discount applied")
else:
    print("No discount available for non-perishable items.")