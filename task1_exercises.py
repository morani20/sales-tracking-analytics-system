# ==============================================================================
# Part 1: Variables & Data Types
# ==============================================================================

# 1. Product details definition and formatted printing
product_name = "Laptop"
price = 1200.50
quantity = 8

print(f"Product: {product_name} | Price: ${price:.2f} | Quantity in Stock: {quantity}")

# 2. Dynamic revenue calculator based on user input
user_product = input("Enter product name: ")
user_price = float(input("Enter product price: "))
user_qty = int(input("Enter quantity sold: "))

total_revenue = user_price * user_qty
print(f"Total Revenue for {user_product}: ${total_revenue:.2f}")

# 3. String-to-integer conversion and type checking
numeric_text = "150"
print("Before conversion:", numeric_text, "Type:", type(numeric_text))

converted_number = int(numeric_text)
print("After conversion:", converted_number, "Type:", type(converted_number))


# ==============================================================================
# Part 2: Conditionals
# ==============================================================================

# 1. Monthly sales performance evaluation
monthly_sales = 3500

if monthly_sales < 1000:
    performance = "ضعيف"
elif monthly_sales <= 5000:
    performance = "متوسط"
else:
    performance = "ممتاز"

print(f"Sales: {monthly_sales} -> Performance: {performance}")

# 2. Inventory level evaluation
stock_quantity = 5

if stock_quantity == 0:
    stock_status = "نفذ المخزون"
elif stock_quantity < 10:
    stock_status = "كمية منخفضة"
else:
    stock_status = "متوفر"

print(f"Stock Level: {stock_quantity} -> Status: {stock_status}")

# 3. Finding peak sales value without built-in max() function
sales_m1 = 1200
sales_m2 = 1800
sales_m3 = 1500

highest_sales = sales_m1
if sales_m2 > highest_sales:
    highest_sales = sales_m2
if sales_m3 > highest_sales:
    highest_sales = sales_m3

print(f"Highest sales record among the three months is: {highest_sales}")


# ==============================================================================
# Part 3: Loops
# ==============================================================================

# 1. Printing a 12-month sequential sales report
months_data = [400, 700, 500, 800, 1100, 950, 1200, 1300, 1050, 1400, 1600, 1500]
print("--- Monthly Sales Report ---")
for index, sales in enumerate(months_data, start=1):
    print(f"Month {index}: ${sales}")

# 2. Summing up sales that strictly exceed a threshold
sample_sales_list = [1500, 2500, 1800, 3100, 2000, 4200]
filtered_sum = 0
for sales in sample_sales_list:
    if sales > 2000:
        filtered_sum += sales

print(f"Sum of sales strictly above 2000: ${filtered_sum}")

# 3. Standard FizzBuzz implementation (1 to 50)
print("--- FizzBuzz Execution ---")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 4. Number guessing game for a target sales goal
target_goal = 7000
print("--- Sales Goal Guessing Game ---")
while True:
    try:
        guess = int(input("Guess the sales target (e.g. 7000): "))
        if guess > target_goal:
            print("أعلى من الهدف! حاول مجدداً.")
        elif guess < target_goal:
            print("أقل من الهدف! حاول مجدداً.")
        else:
            print("ممتاز! تخمين صحيح، لقد وصلت للهدف المطلوب.")
            break
    except ValueError:
        print("الرجاء إدخال رقم صحيح فقط.")


# ==============================================================================
# Part 4: Functions
# ==============================================================================

def calculate_revenue(price, quantity):
    """Calculates total revenue."""
    return price * quantity

def apply_discount(price, discount_percent=10):
    """Applies a percentage discount to a given price."""
    return price * (1 - discount_percent / 100)

def classify_performance(sales_value):
    """Classifies sales performance based on predefined thresholds."""
    if sales_value < 1000:
        return "ضعيف"
    elif sales_value <= 5000:
        return "متوسط"
    else:
        return "ممتاز"

def average(numbers_list):
    """Calculates the arithmetic mean of a numbers list."""
    if not numbers_list:
        return 0
    return sum(numbers_list) / len(numbers_list)


# ==============================================================================
# Part 5: Data Structures
# ==============================================================================

# 1. Processing and sorting a monthly sales list
monthly_records = [1200, 950, 1800, 1500, 2100, 1300]
print(f"Original Records: {monthly_records}")
print(f"Highest Monthly Sale: {max(monthly_records)}")
print(f"Lowest Monthly Sale: {min(monthly_records)}")
monthly_records.sort()
print(f"Sorted Records (Ascending): {monthly_records}")

# 2. Key-value dictionary tracking and picking the top performer
products_catalog = {
    "Keyboard": 450,
    "Monitor": 1200,
    "Headphones": 350
}
top_product = max(products_catalog, key=products_catalog.get)
print(f"Top Selling Product: {top_product} with sales of ${products_catalog[top_product]}")

# 3. Filtering unique cities using a set structure
customer_cities = ["Gaza", "Ramallah", "Gaza", "Nablus", "Ramallah", "Hebron"]
unique_cities = set(customer_cities)
print(f"Unique Customer Cities: {unique_cities}")