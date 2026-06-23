print('Calculadora de Terminal\n')
print('1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão')

try:
    operacao = int(input('\nEscolha de 1 a 4 qual operação quer realizar: '))
    if operacao > 4:
        print('\nErro: Nenhuma das opções válidas foram digitadas.')

    primeiro_numero = int(input('\nDigite o primeiro número: '))
    segundo_numero = int(input('Digite o segundo número: '))

    if operacao == 1:
        print('\nVocê escolheu a opção de Somar')
        somar = primeiro_numero + segundo_numero
        print(f'A soma de {primeiro_numero} + {segundo_numero} é igual a {somar}')
    elif operacao == 2:
        print('\nVocê escolheu a opção de Subtrair')
        subtrair = primeiro_numero - segundo_numero
        print(f'A subtração de {primeiro_numero} - {segundo_numero} é igual a {subtrair}')
    elif operacao == 3:
        print('\nVocê escolheu a opção de Multiplicar')
        multiplicar = primeiro_numero * segundo_numero
        print(f'A multiplicação de {primeiro_numero} * {segundo_numero} é igual a {multiplicar}')
    elif operacao == 4:
        print('\nVocê escolheu a opção de Dividir')
        divisao = primeiro_numero / segundo_numero
        print(f'A divisão de {primeiro_numero} / {segundo_numero} é igual a {divisao}')

except ValueError:
    print('\nErro: Não é permitido letras ou simbolos. Escolha um número de 1 a 4.')
    


