#value types => string, number

x = 5 
y = 25

x = y 

y = 10

print(x,y)  # burda x değişmedi

#reference type

a = ['apple', 'banana']
b = ['apple', 'banana']

a = b 

b[0] = 'grape' #burada a'da değişti

print(a,b)