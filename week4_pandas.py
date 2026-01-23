import pandas as pd
import numpy as np

# Video 13 Konversi nilai numerik ke dalam sejumlah kategori
n_rows = 10
n_cols = 1
cols = ('Usia',)

df = pd.DataFrame(
    np.random.randint(1, 99, size=(n_rows, n_cols)),
    columns=cols
)
print(df)
print()

df['Kelompok_usia'] = pd.cut(
    df['Usia'],
    bins=[0, 18, 65, 99],
    labels=['anak', 'dewasa', 'manula']
)
print(df)
print()


# Video 14 Menggunakan merge dua data frame
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)
print(df.head())
print()

df1 = df.copy(deep=True)
df1 = df1.drop([1, 4])
print(df1)
print()

df2 = df.copy(deep=True)
df2 = df2.drop([0, 3])
print(df2)
print()

# Menggabungkan dua data frame
df_inner = pd.merge(df1, df2, how='inner')
print(df_inner)
print()

df_outer = pd.merge(df1, df2, how='outer')
print(df_outer)
print()


# Video 15 Memecahkan nilai string dari suatu kolom ke dalam beberapa kolom baru
data = {
    'nama': ['Didi Kempot', 'Glen Fredly', 'Mbah Surip'],
    'Tempat_kelahiran': [
        'Surakarta, Jawa Tengah',
        'Jakarta, DKI Jakarta',
        'Mojokerto, Jawa Timur'
    ]
}

df = pd.DataFrame(data)
print(df)
print()

# Memecah nama depan dan nama belakang
df[['nama_depan', 'nama_belakang']] = df['nama'].str.split(' ', expand=True)
print(df)
print()

# Memecah nama Kota dan propinsi
df[['Kota', 'Propinsi']] = df['Tempat_kelahiran'].str.split(', ', expand=True)
print(df)
print()


# Video 16 Menata ulang data frame dengan multiple indexes menggunakan unstack()
df = pd.read_csv('./data/titanicfull.csv')
print(df.head())
print()

# Data Frame dengan multiple indexes dari hasil groupping
grouped = df.groupby(['sex', 'pclass'])['survived'].mean()
print(grouped)
print()

# Menata ulang data frame dengan multiple indexes
df_unstack = grouped.unstack()
print(df_unstack)