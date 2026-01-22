import pandas as pd
import numpy as np


# Video 9 Membagi Data Frame menjadi dua secara acak

# Persiapan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                  columns = cols)
print(df)
print(df.shape)

# Membagi Data Frane menjadi dua secara acak
# berdasarkan proporsi tertentu

proporsi = 0.7
df_1 = df.sample(frac=proporsi)
df_2 = df.drop(df_1.index)

print(f'\ndf_1 shape: {df_1.shape}')
print(f'\ndf_2 shape: {df_2.shape}\n')

print(df_1)
print()
print(df_2)
print()


# Video 10 Mengganti nama kolom pada Data Frame berdasarkan pola

# Persiapan Data Frame
df = pd.read_csv('./data/titanicfull.csv')
df.columns = ['Pclass', 'Survival status', 'full name', 'Sex', 'Age',
              'Sib_SP', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
df_backup = df.copy(deep=True)
print(df.head())

# Menggunakan lowercase untuk nama kolom dan mengganti spasi dengan _

df.columns = df.columns.str.replace(' ', '_').str.lower()
print(df.head())

# Memangkas kelebihan spasi pada nama kolom
df = df_backup.copy(deep=True)
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
print(df.head())


# Video 11 Seleksi kolom dan baris pada Data Frame menggunakan loc

# persiaoan Data Frame
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                  columns = cols)
print(df)
print()

# Seleksi kolom dan baris menggunakan loc
print(df.loc[[0,3,4], ['B','E']])
print()

# Seleksi baris dengan kondisi
print(df.loc[df['B']>10, ['B','D','E']])
print()

# Slicing data frame dengan loc
print(df.loc[0:4, 'B':'D'])
print()


# video 12 Membentuk kolom bertipe datetime dari beberapa
#          kolom lain pada Pandas Data Frame

# Persiapan Data Frame
data = {'day':[1, 2, 10, 25, 12],
        'month':[1, 2, 4, 5, 6],
        'year':[2000, 2001, 2010, 2015, 2020]}

df = pd.DataFrame(data)
print(df)
print()

# Membentuk kolom bertipe datetime
df['penanggalan'] = pd.to_datetime(df[['day', 'month', 'year']])
print(df)
print()
print(df.dtypes)
print()