import pandas as pd

data = {
    "Product": ["Pen", "Book", "Bag"],
    "Sales": [100, 200, 150]
}

df = pd.DataFrame(data)

total = df["Sales"].sum()

print("Total Sales =", total)