def dec2bin(n):
    lista_binarios = []
    divisao = n
    if divisao < 0 :
        print(dec2bin(int(input("Insira um valor maior que 0 "))))
        exit()

    while divisao > 0:
        resto = divisao % 2
        divisao = divisao // 2
        lista_binarios.append(str(resto))
    while len(lista_binarios) < 4:
        lista_binarios.append('0')

    lista_binarios = lista_binarios[::-1]            

    return ''.join(lista_binarios)

def Main():
    numero = int(input("Digite o numero decimal : "))  
    print(dec2bin(numero))
    

Main()