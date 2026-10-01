import pandas as pd
import numpy as np

data = {
    "Product": ["Pen", "Book", "Bag", "Pencil"],
    "Sales": [100, 200, 150, 80]
}

df = pd.DataFrame(data)

highest = np.max(df["Sales"])

print("Highest Sales =", highest)