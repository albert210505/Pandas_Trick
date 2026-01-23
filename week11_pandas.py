import pandas as pd
import numpy as np

#Menerapkan agregasi pada sejumlah kolom dengan agg()
df = pd.read_csv('D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv')
df.groupby('pclass').agg({'pclass':'count', 
                          'age':['mean', 'max'], 
                          'survived': 'mean'})
df.groupby('pclass').agg(n_pass=('pclass', 'count'),
                         avg_age=('age', 'mean'),
                         max_age=('age', 'max'), 
                         survival_rate=('survived', 'mean'))

#Mengurutkan data berdasarkan kolom tertentu
df = pd.read_csv('D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv')
df.sort_values('age').head()
df.sort_values('age', ascending=False).head()
df.sort_values(['survived', 'age']).head()

#Menangani whitespace pada Data Frame
data = {'nim': ['10', '11', '12', '13', '  '],
        'nama': ['adi', '  ', 'tejo', '  ', 'bejo']}

df = pd.DataFrame(data)
df.info()
df = df.replace(r'^\s*$', np.nan, regex=True)
df.info()

#Mengakses sekelompok data dengan get_group()
df = pd.read_csv('D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv')
grouped_df = df.groupby('sex')
grouped_df.get_group('female').head(10)
grouped_df = df.groupby('survived')
grouped_df.get_group(1).head(10)

#Menata ulang penempatan kolom pada Data Frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), 
                  columns=cols)
df[['D', 'C', 'A', 'E', 'B']]
df = df[['D', 'C', 'A', 'E', 'B']]
