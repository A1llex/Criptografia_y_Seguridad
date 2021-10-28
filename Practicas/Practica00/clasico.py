#yo

import random
alfabeto = 'ABCDEFGHIJKLMNOPQRSTuVWXYZ'

#Algoritomo para llaves
def KeyGen():
    return random.randint(0,26)

#algoritmo de cifrado
def Enc(llave,mensaje):
    cifrado =''
    for letra in mensaje :
        indice_letra_cifrado = (alfabeto.index(letra)+llave) %27
        cifrado+= alfabeto[indice_letra_cifrado]
    return cifrado

#algorimo para decifrado
def Dec(llave,cifrado):
    return Enc(-llave,cifrado)

llave = KeyGen()
mensaje = 'HOLAMUNDO'
mensaje = input("Entra tu mensaje: ") 
print(f'llave:{llave}')
mensaje2 = Enc(llave,mensaje)
print(f'mensaje cifrado :{mensaje2}')
print(f'mensaje decifrado :{Dec(llave,mensaje2)}')

bytes