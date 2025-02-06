# Calculadora com While.

# Inicia um loop infinito para manter a calculadora em execução.
while True:
    # Solicita ao usuário o primeiro número.
    numero_1 = input('Digite um número: ')

    # Solicita ao usuário o segundo número.
    numero_2 = input('Digite outro número: ')

    # Solicita ao usuário o operador desejado (+, -, / ou *).
    operador = input('Digite o operador (+-/*): ')

    # Inicializa a variável que indica se os números são válidos.
    numeros_validos = None

    # Inicializa as variáveis numéricas (poderia ser opcional, mas aqui está para clareza).
    num_1 = 0
    num_2 = 0

    try:
        # Tenta converter as entradas para float
        num_1 = float(numero_1)
        num_2 = float(numero_2)

        # Se a conversão for bem-sucedida, define que os números são válidos.
        numeros_validos = True

    except:
        # Se ocorrer erro na conversão, mantém numeros_validos como None.
        numeros_validos = None

    # Verifica se os números não são válidos.
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        # Retorna ao início do loop para nova tentativa.
        continue

    # Define uma string com os operadores permitidos.
    operadores_permitidos = '+-/*'

    # Verifica se o usuário digitou mais de um caractere para o operador.
    if len(operador) > 1:
        print('Digite apenas um operador')
        # Retorna ao início do loop para nova tentativa.
        continue
    
    # Verifica se o operador digitado está na lista de operadores permitidos.
    if operador not in operadores_permitidos:
        print('Operador inválido, digite outro.')
        # Retorna ao início do loop para nova tentativa.
        continue

    # Informa ao usuário que a operação será realizada.
    print('Realizando sua conta. Confira o resultado abaixo.')

    # Verifica qual operação deve ser realizada e imprime o resultado.
    if operador == '+':
        print(f'{num_1} + {num_2} = ', num_1 + num_2)
    
    elif operador == '-':
        print(f'{num_1} - {num_2} = ', num_1 - num_2)
    
    elif operador == '*':
        print(f'{num_1} * {num_2} = ', num_1 * num_2)
    
    elif operador == '/':
        print(f'{num_1} / {num_2} = ', num_1 / num_2)
    
    else:
        # Caso nenhum dos operadores anteriores corresponda (situação improvável), informa erro.
        print('Algo deu errado !')
        continue

    # Pergunta ao usuário se deseja sair, converte a resposta para minúsculas e verifica se inicia com 's'.
    sair = input('Deseja sair: [S]im ou [N]ão ').lower().startswith('s')

    # Se a resposta for afirmativa, encerra o loop e finaliza o programa.
    if sair is True:
        print('Até mais!')
        break