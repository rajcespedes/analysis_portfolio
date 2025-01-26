import pandas as pd

data = pd.read_csv('./dodgers_salaries_test.csv')

print(data[' BB'])

data.drop(columns=' BB',axis=0, inplace=True)

print(data.info())

correlation = data.corr()

print(data.corr())

correlation.to_csv('corr_mat.csv')

