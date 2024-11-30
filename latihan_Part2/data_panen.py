data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#membuat percabangan
for id_lokasi, info in data_panen.items():
    hasil_padi = info['hasil_panen']['padi']
    hasil_jagung = info['hasil_panen']['jagung']
    if hasil_padi > 1300 or hasil_jagung > 800:
        print(f"lokasi {id_lokasi}, memerlukan perhatian khusus")
    else:
        print(f"lokasi {id_lokasi} dalam kondisi baik")

#menampilkan jumlah padi dan kedelai sesuai lokasi
hasil_padi = {}
hasil_kedelai = {}
for lokasi, data in data_panen.items():
    hasil_padi[lokasi] = data['hasil_panen']['padi']
    hasil_kedelai[lokasi] = data['hasil_panen']['kedelai']
print(f"Hasil panen padi setiap lokasi:", hasil_padi)
print(f"Hasil panen kedelai setiap lokasi:", hasil_kedelai)
    
#Menampilkan jumlah padi dan kedelai
hasil_padi = []
hasil_kedelai = []
for lokasi, data in data_panen.items():
    hasil_padi.append(data['hasil_panen']['padi'])
    hasil_kedelai.append(data['hasil_panen']['kedelai'])
print("Hasil Keseluruhan Padi:", hasil_padi)
print("Hasil Keseluruhan Kedelai:", hasil_kedelai)



#menampilkan lokasi3
print(data_panen['lokasi3']['nama_lokasi'])

#menampilkan hasil panen jagung lokasi2
print(data_panen['lokasi2']['hasil_panen']['jagung'])

#menampilkan semua lokasi
for id_lokasi, info in data_panen.items():
    print(f"\nID Lokasi: {id_lokasi}")
    print(f"Nama Lokasi: {info['nama_lokasi']}")  
    for hasil,hasil_panen in info["hasil_panen"].items():
       print(f"Nilai {hasil.capitalize()}: {hasil_panen}")

       #baris baru
       print("Hello Word")
       
       #Line Agar Di konflik
       print("Abdurrahman Aufar")