import pandas as pd
import numpy as np

data = {
    "Product": ["Pen", "Book", "Bag", "Pencil"],
    "Sales": [100, 200, 150, 80]
}

df = pd.DataFrame(data)

print(df)
print("Total:", df["Sales"].sum())
print("Average:", np.mean(df["Sales"]))
print("Maximum:", np.max(df["Sales"]))
print("Minimum:", np.min(df["Sales"]))