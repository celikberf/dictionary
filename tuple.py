list = [1,2,3]
tuple = (1 , 'iki' , 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ['ali' , 'veli']
tuple = ('ayse' , 'fatma' , 'ayse')
names = ('demet' , 'mehmet' , 'ayse') + tuple

list[0] = 'ahmet'
#tuple[0] = 'deniz' # hata alırız. herhangi bir elemanını değiştiremeyiz. Sabit kalıyo. Tek bir eleman üzerinde değişiklk yapamayız
print(tuple.count('ayse')) # kac tane ayse var .
print(tuple.index('ayse')) # ilk kaç numaralı indexte ayse var

print(list)
print(tuple)
print(names)