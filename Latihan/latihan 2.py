#Latihan 2

namaFile = input('Masukkan nama file : ')
while True:
    data = input('Data yang mau ditambahkan : ')
    file = open('dataMhs.txt', 'a')
    file.write(data + '\n')
    file.close()
    lagi = input('Mau lagi (y/n) : ')
    if lagi != 'y':
        break
    elif lagi == 'n':
        break
