import pandas as pd
import numpy as np

df = pd.read_excel("SaleData.xlsx")
print(pd.pivot_table(df, index=["Region", "Manager"]))
