from main import Shop

my_shop = Shop()

# Test 1: Check default inventory
assert "chips" in my_shop.inventory, "Test 1 Failed: chips not found"
print("Test 1: Passed")

# Test 2: Check default stock
assert my_shop.inventory["chips"].quantity == 20, "Test 2 Failed: wrong stock"
print("Test 2: Passed")

# Test 3: Check total earnings
assert my_shop.total_earnings == 0.0, "Test 3 Failed: earnings should be 0"
print("Test 3: Passed")

# Test 4: Check coupon codes
assert "save10" in my_shop.coupons, "Test 4 Failed: save10 coupon not found"
print("Test 4: Passed")

# Test 5: Check second coupon
assert "welcome20" in my_shop.coupons, "Test 5 Failed: welcome20 coupon not found"
print("Test 5: Passed")

# Test 6: Check Product object
assert my_shop.inventory["chips"].name == "chips", "Test 6 Failed: wrong product name"
print("Test 6: Passed")

# Test 7: Check product price
assert my_shop.inventory["chips"].price == 20.0, "Test 7 Failed: wrong product price"
print("Test 7: Passed")

# Test 8: Check database version
assert my_shop.database_version == 2, "Test 8 Failed: wrong database version"
print("Test 8: Passed")

# Test 9: Check all default products
assert len(my_shop.inventory) == 8, "Test 9 Failed: wrong number of products"
print("Test 9: Passed")

# Test 10: Check initial inventory quantity
assert my_shop.inventory["juice"].quantity == 10, "Test 10 Failed: wrong juice quantity"
print("Test 10: Passed")

print("\nAll 10 tests passed successfully!")
