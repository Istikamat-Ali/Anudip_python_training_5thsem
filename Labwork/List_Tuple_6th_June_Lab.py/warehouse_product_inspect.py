'''9. Warehouse Product Inspection
Problem Statement
Product IDs and quality status:
products = [
 (101, "Pass"),
 (102, "Fail"),
 (103, "Pass"),
 (104, "Fail"),
 (105, "Pass")
]
Write a program to:
• Display failed product IDs. 
• Count passed and failed products. 
• Calculate pass percentage. 
• Stop checking if 3 failures are found.'''
print("---------------------- Warehouse Product Inspection ----------------------")
# Given list of product IDs and their quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]
# Display failed product IDs
print("Failed Product IDs:")
for product_id, quality_status in products:
    if quality_status == "Fail":
        print(product_id)
print("---------------------------------")
#-----------------------------------------
# Count passed and failed products
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
print("Passed Products Count:", passed_count)
print("Failed Products Count:", failed_count)
print("---------------------------------")
#-----------------------------------------
# Calculate pass percentage
total_products = len(products)
pass_percentage = (passed_count / total_products) * 100
print("Pass Percentage:", pass_percentage)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
failed_count = 0
for _, quality_status in products:
    if quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
print("Failed Products Count:", failed_count)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
print("Passed Products Count:", passed_count)
print("Failed Products Count:", failed_count)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
pass_percentage = (passed_count / total_products) * 100
print("Pass Percentage:", pass_percentage)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
pass_percentage = (passed_count / total_products) * 100
print("Pass Percentage:", pass_percentage)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
pass_percentage = (passed_count / total_products) * 100
print("Pass Percentage:", pass_percentage)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
pass_percentage = (passed_count / total_products) * 100
print("Pass Percentage:", pass_percentage)
print("---------------------------------")
#-----------------------------------------
# Stop checking if 3 failures are found
passed_count = 0
failed_count = 0
for _, quality_status in products:
    if quality_status == "Pass":
        passed_count += 1
    elif quality_status == "Fail":
        failed_count += 1
        if failed_count == 3:
            break
pass_percentage = (passed_count / total_products) * 100
print("Pass Percentage:", pass_percentage)
print("---------------------------------")
#-----------------------------------------