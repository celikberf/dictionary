# key - value (anahtar - değer)

# 06 => ankara 81 => düzce
#sıralaırn birbirine uygun olması gerekiyor.

# sehirler = ['ankara' , 'düzce']
# plakalar = [6 , 81]

# print(plakalar[sehirler.index('ankara')])
# print(plakalar[sehirler.index('düzce')]) 

# # print(plakalar['ankara']) =>6
# # print(plakalar['düzce']) => 81

# plakalar = {'ankara' : 6 , 'düzce' : 81 } # ankara indexini 6'ya , düzceyi 81'e atadık.

# print(plakalar['ankara'])
# print(plakalar['düzce'])

# plakalar['istanbul'] = 34 # istanbul ' u ekledik
# plakalar['ankara'] = 'new value' # ankara burda "new value" oldu. 

# print(plakalar)

users = {
    'berfincelik' : {
        'age' : 26 , 
        'roles' : ['user'],
        'email' : 'berfin@gmail.com',
        'address' : 'ankara',
        'phone' : '23123123'
    },
    'gulercelik' : {
        'age' : 50 , 
        'roles' : ['admin' , 'user'],
        'email' : 'guler@gmail.com',
        'address' : 'ankara',
        'phone' : '848488484'
    }
}

print(users['gulercelik']['roles'])
print(users['berfincelik']['roles'][0])