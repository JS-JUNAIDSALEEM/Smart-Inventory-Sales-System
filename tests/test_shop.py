
from main import Shop

my_shop = Shop()

# Test 1: Check default inventory
print("Test 1:", "Passed" if "chips" in my_shop.inventory else "Failed")

# Test 2: Check default stock
print("Test 2:", "Passed" if my_shop.inventory["chips"].quantity == 20 else "Failed")

# Test 3: Check total earnings
print("Test 3:", "Passed" if my_shop.total_earnings == 0.0 else "Failed")

# Test 4: Check coupon codes
print("Test 4:", "Passed" if "save10" in my_shop.coupons else "Failed")

# Test 5: Check second coupon
print("Test 5:", "Passed" if "welcome20" in my_shop.coupons else "Failed")

# Test 6: Check Product object
print("Test 6:", "Passed" if my_shop.inventory["chips"].name == "chips" else "Failed")

# Test 7: Check product price
print("Test 7:", "Passed" if my_shop.inventory["chips"].price == 20.0 else "Failed")

# Test 8: Check database version
print("Test 8:", "Passed" if my_shop.database_version == 2 else "Failed")

# Test 9: Check all default products
print("Test 9:", "Passed" if len(my_shop.inventory) == 8 else "Failed")

# Test 10: Check initial inventory quantity
print("Test 10:", "Passed" if my_shop.inventory["juice"].quantity == 10 else "Failed")
