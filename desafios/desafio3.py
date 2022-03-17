"""
CPF = 168.995.350-09
------------------------------------------------
0 * 10 = 10           #    0 * 11 = 11 <-
4 * 9  = 54           #    4 * 10 = 60
1 * 8  = 64           #    1 *  9 = 72
6 * 7  = 63           #    6 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
9 * 5  = 25           #    9 *  6 = 30
9 * 4  = 12           #    9 *  5 = 15
9 * 3  = 15           #    1 *  4 = 20
1 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         236          #             266
11 - (236 % 11) = 11  #     11 - (266 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Loop infinito
while True:
    # cpf = '04169991079'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
