import pandas as pd
import numpy as np


# 33 Menampilkan nilai kumulatif
d = {
    'pemain': ['Budi', 'Joni', 'Iwan', 'Budi', 'Iwan', 'Asep', 'Joni'],
    'goal': [2, 1, 3, 1, 1, 2, 2]
}
df = pd.DataFrame(d)
print(df)

print(df['goal'].cumsum().to_frame())

df['jumlah_goal_kumulatif'] = df['goal'].cumsum()
df['jumlah_goal_kumulatif_tiap_pemain'] = df.groupby('pemain')['goal'].cumsum()
df['cummax'] = df['goal'].cummax()
df['cummin'] = df['goal'].cummin()
df['cumprod'] = df['goal'].cumprod()
print(df)


# 34 Mapping pada Data Frame dengan applymap()
df = pd.DataFrame({
    'Jenis_kelamin': ['Pria', 'Wanita', 'lelaki', 'perempuan'],
    'usia': [23, 21, 24, 22],
    'shift': ['pagi', 'siang', 'malam', 'siang']
})
print(df)

df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
print(df)

mapping = {
    'pria': 'L',
    'lelaki': 'L',
    'wanita': 'P',
    'perempuan': 'P',
    'pagi': 1,
    'siang': 2,
    'malam': 3
}

df[['Jenis_kelamin', 'shift']] = df[['Jenis_kelamin', 'shift']].applymap(mapping.get)
print(df)


# 35 Memadukan fungsi agregasi dengan transform()
d = {
    'no_nota': [1, 1, 1, 2, 2, 3, 4, 5],
    'kopi': ['latte', 'cappucino', 'latte', 'espresso', 'cappuccino', 'latte', 'espresso', 'latte'],
    'harga': [50, 60, 80, 150, 120, 60, 100, 40]
}
df = pd.DataFrame(d)
print(df)

print(df.groupby('no_nota')['harga'].sum().to_frame())
df['total_harga'] = df.groupby('no_nota')['harga'].transform('sum')
print(df)

print(df.groupby('kopi')['harga'].sum().to_frame())
df['total_omset'] = df.groupby('kopi')['harga'].transform('sum')
print(df)


# 36 Menyatukan kolom dengan str.cat()
data = {
    'nama': ['Bayu', 'indra', 'devi', 'agni'],
    'Jenis_kelamin': ['L', 'L', 'P', 'L'],
    'usia': [23, 21, 22, 25]
}
df = pd.DataFrame(data)
print(df)

print(df['nama'].str.cat(df['Jenis_kelamin'], sep=',').to_frame())
df['nama_jk'] = df['nama'].str.cat(df['Jenis_kelamin'], sep=',')
print(df)

print(df['nama'].str.cat(df['usia'].astype(str), sep='-').to_frame())
df['nama_usia'] = df['nama'].str.cat(df['usia'].astype(str), sep='-')
print(df)
