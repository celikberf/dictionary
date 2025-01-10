fruits = {'orange', 'apple', 'banana'}

print(fruits) # diğerlerinden farkı indexlenemez. [0] gibi

for x in fruits : 

    print(x) #index numaraları yok listeyi sıralayamayız. Bu şekilde içindeeki elemanlara ulaşabilir.

fruits.add('cherry') #cherry ekledik.
fruits.update(['mango', 'grape']) # bir liste gönderebiliriz.Liste içine karısmıs bir sekilde gönderilir.
#Aynı elemanı (apple) bir daha eklemeye kalkarsak eklenmez. 1 eleman 1 kere olur bu listede
fruits.remove('mango') # mangoyu sildik.
fruits.discard('apple') # discard ile de elemanı silebiliriz. Apple silindi . 
fruits.pop() # normalde pop ile son elemanı silerdik fakat burda hangsını sileceğini bilemeyiz. Random eleman siler.
fruits.clear() #tüm elemanları sildik. 

print(fruits) 

myList = [1,2,5,4,4,2,1]
print(set(myList)) # set'lediğimiz zaman tekrar eden eleman olmaz . Çıktısı : {1, 2, 4, 5} olur.
