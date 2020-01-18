import pandas as pd
import os

file_path = 'dataset/titanic_train.csv'
df = pd.read_csv(file_path)
print(df.head())