import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [50, 100, 70, 40]

plt.bar(products, sales)
plt.title("Product Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Number Sold")
plt.savefig("product_sales.png")