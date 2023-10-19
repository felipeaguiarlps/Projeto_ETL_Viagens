import pandas as pd

df = pd.read_csv('world-happiness-report-2021.csv')
country_name = df['Country name'].tolist()
print(country_name)

