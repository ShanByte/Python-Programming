quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))
tax_percent= float(input("Enter the tax percent: "))

total = quantity * price
discount = total *(discount_percent/100)
after_discount = total - discount
tax = total * (tax_percent/100)
bill = after_discount + tax
print("Total = ",total)
print("Discount = ",discount)
print("After Discount = ",after_discount)
print("Tax = ",tax)
print("Bill = ",bill)
