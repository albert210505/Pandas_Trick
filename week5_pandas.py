import pandas as pd
import numpy as np


# Video 17 Resampling pada data deret waktu (time series data)
n_rows = 365 * 24
n_cols = 2
cols = ['col1', 'col2']

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)

df.index = pd.date_range(start='2023-01-01', periods=n_rows, freq='H')
print(df.head())

resample_monthly = df.resample('M')['col1'].sum().to_frame()
print(resample_monthly)

# Video 18 Membentuk dummmy Data Frame
df_dummy = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'Col2': [5, 6, 7, 8]
})
print(df_dummy)

n_rows = 5
n_cols = 3
arr = np.random.randint(1, 20, size=(n_rows, n_cols))
print(arr)

df_arr = pd.DataFrame(arr, columns=tuple('ABC'))
print(df_arr)

print(pd.DataFrame(np.random.randn(5, 4)).head())

# Video 19 Formating tampilan Data Frame
n_rows = 5
n_cols = 2
cols = ['omset', 'operasional']

df = pd.DataFrame(
    np.random.randint(1, 20, size=(n_rows, n_cols)),
    columns=cols
)
print(df)

df['omset'] = df['omset'] * 100_000
df['operasional'] = df['operasional'] * 10_000
print(df)

df.index = pd.date_range(start='2023-01-01', periods=n_rows, freq='D')
df = df.reset_index()
df = df.rename(columns={'index': 'tanggal'})
print(df)

# Video 20 Menggabungkan (merge) dua Data frame secara berdampingan
d1 = {'col1': [1, 2, 3],
      'col2': [10, 20, 30]}
df1 = pd.DataFrame(d1)
print(df1)

d2 = {'col1': [4, 5, 6],
      'col2': [40, 50, 60]}
df2 = pd.DataFrame(d2)
print(df2)

df = pd.merge(df1, df2, left_index=True, right_index=True)
print(df)
