# def buscar( letra):
#     lista = ['hola', 'soy', 'juan']
#     if letra in lista:
#         return (f" {letra} Letter has been found")
#     return ('letter wasnt found')



# def main():
    
#     letra = (input('Please enter the number of the letter you want to search: '))
#     buscar(letra)
#     print(buscar(letra))

# main()
def search(lista, letter,index):
    if lista[index] ==letter:
         return letter
    else:
        if lista[index] ==letter:
         return letter

        if:
            len(lista) -1 == index
            if lista[index] ==letter
                return None
    return search(list, letter, index+1)

def main():
    lista =["a", 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j']
    letter = input('Please enter the letter you wish to find: ')
    search(lista, letter, 0)

main()