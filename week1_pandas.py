import pandas as pd
import numpy as np

n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)

print("Dataframe awal :")
print(df)

# VIDEO 1: PREFIX & SUFFIX
df_prefix = df.add_prefix('kolom_')
print("DataFrame dengan prefix:")
print(df_prefix)


df_suffix = df.add_suffix('_field')
print("DataFrame dengan suffix:")
print(df_suffix)

# VIDEO 2: SELEKSI BARIS

df_seleksi = df[~df['A'].isin([1, 3])]
print("Seleksi baris")
print(df_seleksi)

# VIDEO 3 : KONVERSI TIPE DATA NUMERIK

data = {
    'col1': ['1', '2', '3', 'teks'],
    'col2': ['1', '2', '3', '4']
}

df_v3 = pd.DataFrame(data)
print(df_v3)
print(df_v3.dtypes)

# astype
df_x = df_v3.astype({'col2': 'int'})
print(df_x)
print(df_x.dtypes)

# to_numeric
df_numeric = df_v3.apply(pd.to_numeric, errors='coerce')
print(df_numeric)
print(df_numeric.dtypes)

# VIDEO 4 : SELEKSI KOLOM BERDASARKAN TIPE DATA

df_v4 = pd.DataFrame(
    np.random.randint(1, 20, size=(5, 2)),
    columns=['bil_pecahan', 'bil_bulat']
)

df_v4['bil_pecahan'] = df_v4['bil_pecahan'].astype(float)
df_v4.index = pd.date_range(start='2024-01-01', periods=5, freq='H')
df_v4 = df_v4.reset_index()
df_v4['teks'] = list('ABCDE')

print(df_v4)
print(df_v4.dtypes)

print(df_v4.select_dtypes(include='number'))
print(df_v4.select_dtypes(include='object'))
print(df_v4.select_dtypes(include='datetime'))
print(df_v4.select_dtypes(include=['number', 'object']))