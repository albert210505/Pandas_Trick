import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size =(n_rows, n_cols)),
                  columns = cols)

# video 5 : Membalik urutan baris dan kolom pada Data Frame
print(df)
print('\nmembalik urutan kolom\n')
print(df.loc[:, ::-1])
print('\nMembalik urutan baris\n')
print(df.loc[::-1])
print('\nmembalik urutan baris dan mengembalikan index\n')
print(df.loc[::-1].reset_index(drop = True))

# video 6 : Mengganti nama kolom pada Data Frame
print('\nMengganti nama (label) untuk sebuah kolom pada Data Frame\n')
print(df.rename(columns={'C':'Hobi', 'B':'Alamat', 'A':'Nama','D':'Kota', 'E':'Negara'}))

# video 7 : Menghapus (drop) missing values (NaN)
df2 = pd.DataFrame(
    np.random.randn(5, 4),
    columns=list('ABCD')
)
df2.iloc[1, 2] = np.nan
df2.iloc[3, 0] = np.nan
df2 = df2.reset_index().rename(columns={'index': 'Z'})
print(df2.head())
df2_backup = df2.copy(deep=True)

print('\nMenghapus (drop) setiap kolom yang mengandung missing values\n')
df2 = df2.dropna(axis='columns')
print(df2.head())

print('\nMenghapus (drop) setiap baris yang mengandung missing values')
df2 = df2_backup.copy(deep=True)
df2 = df.dropna(axis='rows')
print(df2.head())

print('\nPersentase missing values untuk tiap kolom')
df2 = df2_backup.copy(deep=True)
print(df2.isna().mean())

print('\nMenghapus (drop) setiap kolom yang mengandung missing values berdasarkan threshold')
treshold = len(df2) * 0.9
df2 = df2.dropna(thresh=treshold, axis='columns')
print(df2.head())

# viddeo 8 : Memeriksa kesamaan antar dua buah kolom (series) pada Data Frame
data = {'A': [15, 15, 18, np.nan, 12],
        'B':[15, 15, 18, np.nan, 12]}
df3 = pd.DataFrame(data)
print(df3)

print('\nMengenal pandas series')
print(df3['A'])
print(type(df3['A']))
print(type(df3))

print('\nMemeriksa kesamaan dengan operator ==')
print(df3['A']==df3['B'])
print('\nMemeriksa kesamaan dengan method equals')
print(df3['A'].equals(df3['B']))

print('\nMemeriksa kesamaan antar dua data frame')
df3a = df3.copy(deep = True)
df3.equals(df3a)
print(df3 == df3a)