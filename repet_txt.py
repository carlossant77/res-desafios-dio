def repetir_texto():
    texto = str(input("Insira o texto que será repetido: "))
    repet = int(input("Insira o número de vezes que será repetido: "))
    
    count = 0
    
    while count < repet:
        print(texto, "\n")
        count += 1
        
repetir_texto()