def bin2decItera(n):
    decimal=0
    cont=0
    while n!=0:
        resto=n%10
        decimal=decimal + resto*2**cont
        n=n//10 
        cont=cont+1 
    return decimal
    

def bin2decRecur(num):
  if not (num // 10): 
    return (num)
  else:
    return (num % 10 + bin2decRecur(num // 10) * 2)
    
    
def dec2binItera(n):
    binario=0
    cont=0
    while n!=0:
        resto=n%2
        binario=binario + resto*10**cont
        n=n//2 
        cont=cont+1 
    return binario

def dec2binRecur(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * dec2binRecur(int(n / 2)))
        
def main():
    
    numero = int(input('Digite um numero decimal para realizar as conversões para binario : '))
    
    print("Conversao para binario iterativo: ", dec2binItera(numero))   
    print("Conversao para binario recursivo: ", dec2binRecur(numero)) 
    
    numerobin = int(input('Digite um numero binario para realizar as conversões para decimal : '))
    
    print("Conversao para decimal iterativo: ", bin2decItera(numerobin))
    print("Conversão para decimal recursivo: ", bin2decRecur(numerobin))

main()
