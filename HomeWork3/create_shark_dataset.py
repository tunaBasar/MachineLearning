import pandas as pd
import numpy as np
import random

num_samples = 300

data = {
    'Tag_ID': [f"SHARK-{random.randint(1000, 9999)}" for _ in range(num_samples)],
    'Species': np.random.choice(['Great White', 'Tiger', 'Hammerhead'], num_samples),
    'Gender': np.random.choice(['Male', 'Female'], num_samples),
    'Length_cm': np.random.uniform(150, 600, num_samples),
    'Fin_Height_cm': np.random.uniform(20, 100, num_samples),
    'Color_Code': np.random.randint(1, 5, num_samples),
    'Age': np.random.randint(5, 60, num_samples).astype(float)
}

df = pd.DataFrame(data)


df['Weight_kg'] = (df['Length_cm'] * 1.8) + (df['Fin_Height_cm'] * 2.5) + (df['Age'] * 1.2) + np.random.normal(0, 30, num_samples)

mask = np.random.choice([True, False], size=num_samples, p=[0.1, 0.9])
df.loc[mask, 'Age'] = np.nan

df.to_csv('data/shark_data.csv', index=False)
print("Dataset oluşturuldu: data/shark_data.csv")
print(df.head())
print("\nEksik Veri Sayısı:\n", df.isnull().sum())