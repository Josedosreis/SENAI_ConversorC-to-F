# Conversor de Temperatura !

# Apresentação

print('\n >>> Em qual escala está a temperatura que voce quer converter?')
print('\n\t >>> Digite C para Celsius, F para Fahrenheit e K para Kelvin ! \n')

grau = input('>>>> Digite : ')
print('\n >> Qual é o valor da temperatura na escala que você quer converter?')

# escolha = float(input('------- : '))

temperatura = float(input(''))
print('\n >> Em qual escala está a temperatura para qual você quer converter?')

# escolha = input('------- : ')

conversao = input()

#(°F − 32) × 5/9 )

if (grau == "f" and  conversao == "c"):
    print('\n >>>> A tempera em Celsius é:',  (temperatura - 32) * 5 / 9, "C")

if (grau == "c" and  conversao == "f"):
    print('\n >>>> A temperatura em Fahrenheit é:',  9 * temperatura / 5 + 32, "F")


