#Função
from funcao import celsius_para_fahrenheit
from funcao import fahrenheit_para_celsius

while True:
    #Apresentação

    print('\n------------- Conversor --------------\n')

    #Entrada

    print('1. Celsius para Fahrenheit')
    print('2. Fahrenheit para Celsius')
    print('3. Sair \n')

    opcao = int(input('Escolha uma opção: '))
    
    #Processamento - Saida
    if opcao == 1:
        
        celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = c_f(celsius)
        print(f"{celsius}ºC é igual a {fahrenheit}ºF")

    elif opcao == 2:
        
        fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        celsius = f_c(fahrenheit)
        print(f'{fahrenheit}ºF é igual a {celsius}ºC')
        
    elif opcao == 3:
        
        print('Tchauuu')
        
        break
    
    else:
        
        print('\n Opção Invalida,Tente novamente!')