from operadores import operacoes

def menu_calculadora():
    print("""
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█""")  
    print('\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print('\n+. Soma\n-. Subtração\n*. Multiplicação\n/. Divisão\n0. Para fechar a calculadora.')
def calcula_operacoes():
    while True:
        try: 
            operador = input('\nQual operação deseja realizar? (+, -, *, / ou 0 para sair): ')

            if operador == '0':
                print('\nObrigado por usar a calculadora')
                break

            primeiro_numero = int(input('\nDigite o primeiro número: '))
            segundo_numero = int(input('Digite o segundo número: '))
            
            # Pega a chave do dicionário operacoes e seu valor através da variável operador.
            funcao_operacao = operacoes.get(operador)
            resultado = funcao_operacao(primeiro_numero, segundo_numero)

            print(f'O resultado da operação é: {resultado}')

        except ValueError: 
            print('Erro: Digite apenas as operações possíveis.')
            continue
        except TypeError:
            print('Erro: Escolha uma das opções válida (+, -, *, / ou 0 para sair).')
      
menu_calculadora()
calcula_operacoes()