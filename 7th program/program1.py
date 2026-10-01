import pandas as pd

data = {
    "Product": ["Pen", "Book", "Bag", "Pencil"],
    "Sales": [100, 200, 150, 80]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)