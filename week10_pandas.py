import pandas as pd
import numpy as np

# Video 37 Seleksi baris dengan banyak kriteria
df = pd.read_csv('D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv')

df[(df['sex'] == 'female') &
   (df['age'] >= 60) &
   (df['embarked'] == 'S') &
   (df['survived'] == 1)]

kr1 = df['sex'] == 'female'
kr2 = df['age'] >= 60
kr3 = df['embarked'] == 'S'
kr4 = df['survived'] == 1

df[kr1 & kr2 & kr3 & kr4]


# Video 38 Mengenal parameter header dan skiprows
df = pd.read_csv('./data/iris_error.csv')
df.head(8)

df = pd.read_csv('./data/iris_error.csv', header=2, skiprows=[5, 6])
df.head()


# Video 39 Mengacak urutan baris pada DataFrame
n_rows = 6
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 5, size=(n_rows, n_cols)),
    columns=cols
)

df.sample(frac=1.0, random_state=1)
df.sample(frac=1.0, random_state=1).reset_index(drop=True)


# Video 40 Mengakses sekelompok data dengan get_group()
df = pd.read_csv('D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv')

grouped_df = df.groupby('sex')
grouped_df.get_group('female').head(10)

grouped_df = df.groupby('survived')
grouped_df.get_group(1).head(10)