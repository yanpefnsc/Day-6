# Loop principal — permite repetir operações até o usuário digitar 'sair'
while True:
    # pergunta se quer sair ou continuar
    sair = input("Digite 'sair' para encerrar ou Enter para continuar: ")
    if sair == "sair":
        break
    
    # lê os dois números do usuário
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))
    # lê a operação desejada (normaliza para minúsculas)
    escolha = input("Escolha a operação (soma, subtracao, multiplicacao ou divisao): ").lower()

    # função que realiza a operação escolhida
    def calcular(n1, n2, operacao):  # operacao poderia ter qualquer nome
        if operacao == "soma":  # se o usuário escolheu soma
            return n1 + n2
        elif operacao == "subtracao":  # se escolheu subtração
            return n1 - n2
        elif operacao == "multiplicacao":  # se escolheu multiplicação
            return n1 * n2
        elif operacao == "divisao":  # se escolheu divisão
            if n2 != 0:  # evita divisão por zero
                return n1 / n2
            else:
                return "Erro: Divisão por zero!"
        else:
            return "Operação inválida"  # caso o usuário digite algo desconhecido

    # chama a função e mostra o resultado
    resultado = calcular(n1, n2, escolha)
    print(f"O resultado da {escolha} é: {resultado}")
