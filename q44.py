# Given a list of strings representing product names and their prices, extract and print only those products whose prices are above 20. Use the walrus operator to do the comparison and assignment in a single step.

products = ["apple:10", "banana:5", "mango:25", "date:30", "fig:15"]
for product in products:
    new_list = product.split(":")
    if (price := int(new_list[1])) > 20:
        print(product)
