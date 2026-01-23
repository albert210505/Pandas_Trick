import pandas as pd
import numpy as np

#Seleksi kolom menggunakan f-string
df = pd.read_csv('./data/Iris.csv')
df.head()

df['SepalWidthCm'].to_frame().head()
part = 'Sepal'

df[f'{part}WidthCm'].to_frame().head()
df[['PetalWidthCm', 'PetalLengthCm']].head()
part = 'Petal'

df[[f'{part}WidthCm', f'{part}LengthCm']].head()


#Membuat kolom baru dengan looping dan f-string
d = {'penjual':['bejo', 'tejo', 'wati', 'bejo', 'cecep', 'tejo', 'wati', 'bejo'], 
     'barang':['monitor', 'monitor', 'keyboard', 'mouse', 'keyboard', 'monitor', 'laptop', 'monitor']}

df = pd.DataFrame(d)
print(df)

d = {'penjual':['bejo', 'tejo', 'wati', 'bejo', 'cecep', 'tejo', 'wati', 'bejo'], 
     'barang':['monitor', 'monitor', 'keyboard', 'mouse', 'keyboard', 'monitor', 'laptop', 'monitor']}

df = pd.DataFrame(d)
print(df)


#Seleksi baris dengan between()
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), columns=cols)

df[df['A'].between(2, 5)]
## DEPRICATED ##
# df[df['A'].between(2, 5, inclusive=False)]
df[df['A'].between(2, 5, inclusive='left')]
df[df['A'].between(2, 5, inclusive='right')]
df[df['A'].between(2, 5, inclusive='both')]
df[df['A'].between(2, 5, inclusive='neither')]

#Tranformasi kolom menjadi baris dengan melt()
d = {
    'kode_area': [123, 456, 789, 321],
    'pabrik': [4, 2, 5, 0],
    'gudang': [2, 4, 7, 3],
    'toko': [64, 32, 15, 24]
}

df = pd.DataFrame(d)

df = df.melt(id_vars='kode_area',
             var_name='jenis_bangunan',
             value_name='jumlah')
