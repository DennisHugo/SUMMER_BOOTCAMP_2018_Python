
f = open("input.txt", "r")

for line in f.readlines():
    print(line)

#print(f.read())
f.close()

f1 = open("input1.txt", "r")

#print(f1.readline())   #Lee solo la primera linea
print(f1.read())        #Lee todo el archivo txt
#print(f1.readlines())  #Lee todo pero lo guarda en un diccionario

f1.close()
