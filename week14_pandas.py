import pandas as pd
import numpy as np

#Membuat kategori baru berdasarkan threshold (ambang batas)
d = {'hobi':['jogging', 'mancing', 'renang',
             'mancing', 'mancing', 'baca', 
             'baca', 'mancing', 'fotograsi', 
             'mancing', 'camping']}

df = pd.DataFrame(d)
print(df)

df['hobi'].value_counts()
persentase = df['hobi'].value_counts(normalize=True)
persentase

threshold = 0.1
hobi_lain = persentase[persentase < threshold].index
hobi_lain

df['hobi'] = df['hobi'].replace(hobi_lain, 'lainnya')
df['hobi']
df['hobi'].value_counts(normalize=True)


#Menyimpan Data Frame sebagai file CSV
data = {
    'nama': ['bejo', 'tejo', 'wati', 'tiwi', 'cecep'],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L'],
    'umur': [20, 21, 19, 20, 22]
}
df = pd.DataFrame(data)

df.to_csv('data_peserta.csv')
df = pd.read_csv('data_peserta.csv')
df.to_csv('data_peserta_tanpa_index.csv', index=False)
df = pd.read_csv('data_peserta_tanpa_index.csv')


#Menghitung jumlah baris menurut kriteria tertentu
n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), columns=cols)
df[df['A'] > 5].sum()
df[df['A'] > 5].mean()


data = {
    'nama': ['bejo', 'tejo', 'wati', 'tiwi', 'cecep'],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L'],
    'umur': [20, 21, 19, 20, 22]
}
df = pd.DataFrame(data)

usia = df.pop('umur').to_frame()
print(df)
print(usia)