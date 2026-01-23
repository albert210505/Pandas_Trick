import pandas as pd
import numpy as np


# 29 Melakukan random sampling pada Data Frame
d = {
    'col_1': [1, 2, 3, 4, 5],
    'col_2': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(d)
print(df)

print(df.sample(n=4, replace=False, random_state=0))
print(df.sample(n=4, replace=True, random_state=0))


# 30 Akses nilai variabel pada query()
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

print(df.query('A > 5'))

rerata = df['A'].mean()
print(rerata)

print(df.query('A > @rerata'))


# 31 Tipe data ordinal pada Pandas Data Frame
d = {
    'pelanggan': [11, 12, 13, 14],
    'kepuasan': ['baik', 'cukup', 'buruk', 'cukup']
}
df = pd.DataFrame(d)
print(df)

from pandas.api.types import CategoricalDtype

tingkat_kepuasan = CategoricalDtype(
    ['buruk', 'cukup', 'baik', 'Sangat baik'],
    ordered=True
)

df['kepuasan'] = df['kepuasan'].astype(tingkat_kepuasan)
print(df)

df = df.sort_values('kepuasan', ascending=True)
print(df)

print(df[df['kepuasan'] > 'cukup'])


# 33 Plotting pada pandas Data Frame
n_rows = 40
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)
print(df.head())

# Line plot
df.plot(kind='line')
df[['A', 'B']].plot(kind='line')

# Bar plot
df.plot(kind='bar')
df[['A', 'B']].plot(kind='bar')
df[['A', 'B']].head().plot(kind='bar')
df[['A', 'B']].head().plot(kind='barh')

# Area plot
df.plot(kind='area')
df[['A', 'B']].head().plot(kind='area')

# Box plot
df.plot(kind='box')

# Histogram
df.plot(kind='hist')
df[['A', 'B']].plot(kind='hist')

# KDE
df.plot(kind='kde')

# Scatter plot
df.plot(x='A', y='B', kind='scatter')
