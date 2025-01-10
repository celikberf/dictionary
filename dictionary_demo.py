"""
ogrenciler = {
    '120' : {
        'ad' : 'Ali'
        'soyad' : 'Yılmaz'
        'telefon' : '598 998 98 98'
    }, 

    '125' : {
        'ad' : 'Can'
        'soyad' : 'Korkmaz'
        'telefon' : '589 889 89 89'
    }, 
    '128' : {
        'ad' : 'Volkan'
        'soyad' : 'Yükselen'
        'telefon' : '577 777 77 77'
    }, 
}

1- Bilgileri verilen öğrencilerin kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz. 

"""

ogrenciler = {}

number = input('Lütfen öğrenci numarasını giriniz : ')
name = input('Lütfen öğrenci adını giriniz : ')
surname = input('Lütfen öğrenci soyadını giriniz : ')
phone = input('Lütfen öğrenciye ait telefon numarasını giriniz : ')

# ogrenciler[number] = {
#     'ad' : name,
#     'soyad' : surname,
#     'telefon' : phone
# }

ogrenciler.update({
    number: {
        'ad' : name,
     'soyad' : surname,
        'telefon' : phone
    }
})

number = input('Lütfen öğrenci numarasını giriniz : ')
name = input('Lütfen öğrenci adını giriniz : ')
surname = input('Lütfen öğrenci soyadını giriniz : ')
phone = input('Lütfen öğrenciye ait telefon numarasını giriniz : ')

ogrenciler.update({
    number: {
        'ad' : name,
     'soyad' : surname,
        'telefon' : phone
    }
})

number = input('Lütfen öğrenci numarasını giriniz : ')
name = input('Lütfen öğrenci adını giriniz : ')
surname = input('Lütfen öğrenci soyadını giriniz : ')
phone = input('Lütfen öğrenciye ait telefon numarasını giriniz : ')

ogrenciler.update({
    number: {
        'ad' : name,
     'soyad' : surname,
        'telefon' : phone
    }
})

print(ogrenciler)

print('*'*50)

ogrNo = input('öğrenci no : ')
ogrenci = ogrenciler[number]
print(f"Aradığınız{ogrNo} nolu öğrencinin adı : {ogrenci['ad']} soyadı : {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")