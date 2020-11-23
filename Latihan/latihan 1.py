#Latihan 1

namaFile = input('Masukkan nama file : ')
print('Isi file ', namaFile, 'adalah : ')
file = open('anyfiles.txt', 'r')
print(file.read())
