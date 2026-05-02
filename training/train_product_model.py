import pandas as pd
import pickle

# LOAD DATA
df = pd.read_csv("../data/BDA_SEM-4.csv")

# FEATURE ENGINEERING
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# GROUP BY PRODUCT
df_product = df.groupby('Description').agg({
    'Quantity': 'mean',
    'UnitPrice': 'mean',
    'TotalAmount': 'sum'
}).reset_index()

# SAVE PRODUCT DATA (NO ML NEEDED NOW)
pickle.dump(df_product, open("../models/product_data.pkl", "wb"))

print("✅ Product dataset saved")