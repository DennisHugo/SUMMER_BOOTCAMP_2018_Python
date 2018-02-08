zoo = ['lion', "elephant", 'monkey']
holas = ['h','o','l','a']

if __name__ == "__main__":
    f = open("output.txt", 'a')

    for i in zoo:
        print(f.write(i))
    for j in holas:
        print(f.write(j))   #Escribe hola al final de la oracion del archivo output.txt

    f.close()
