# Day-6

"""
Now the code includes a summary of what it does. Right below, you will find the description of each part of the code. The full explanation in English is in the first part, and the description in Portuguese is in the second.

Agora o código possui um resumo do que ele faz. Logo abaixo, você encontrará a descrição de cada parte do código. A explicação completa em inglês está na primeira parte, e a descrição em português está na segunda.

"""

1. Main loop — allows repeating operations until the user types 'exit'
while True:


Explanation: The while True creates an infinite loop. This means that the code inside the loop will continue to execute until a stopping condition is met (in this case, when the user types "exit").

2. Ask if the user wants to exit or continue
    sair = input("Digite 'sair' para encerrar ou Enter para continuar: ")


Explanation: The input() function displays a message asking the user to type something. The user’s input is stored in the variable sair. This line is asking the user if they want to continue or exit the program.

3. Checks if the user typed 'exit'
    if sair == "sair":
        break


Explanation: The code checks if the value of the variable sair is equal to the string "exit". If it is, the break command is executed, which stops the while loop and ends the program.

4. Reads the two numbers from the user
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))


Explanation: These two lines prompt the user to enter two numbers. The input() function reads the value as a string, and the float() function converts this string into a floating-point number (decimal number). The values are stored in the variables n1 and n2.

5. Reads the desired operation from the user and normalizes it to lowercase
    escolha = input("Escolha a operação (soma, subtracao, multiplicacao ou divisao): ").lower()


Explanation: The input() function asks the user to choose an operation (addition, subtraction, multiplication, or division). The .lower() method converts the user's input to lowercase, ensuring that the comparison is case-insensitive (for example, the user can type "SUM" or "sum", and both will be interpreted the same).

6. Defines the calculation function
    def calcular(n1, n2, operacao):


Explanation: This line defines a function called calcular (meaning "calculate" in Portuguese), which takes three parameters: n1, n2 (the two numbers provided by the user), and operacao (the operation chosen, such as sum, subtraction, etc.).

7. Performs the addition operation
        if operacao == "soma":
            return n1 + n2


Explanation: Inside the calcular function, the code first checks if the operation chosen was "soma" (sum). If it is, it returns the result of adding n1 and n2.

8. Performs the subtraction operation
        elif operacao == "subtracao":
            return n1 - n2


Explanation: If the chosen operation was "subtracao" (subtraction), the function returns the result of subtracting n2 from n1.

9. Performs the multiplication operation
        elif operacao == "multiplicacao":
            return n1 * n2


Explanation: If the operation chosen was "multiplicacao" (multiplication), the function returns the product of n1 and n2.

10. Performs the division operation
        elif operacao == "divisao":
            if n2 != 0:
                return n1 / n2
            else:
                return "Erro: Divisão por zero!"


Explanation: If the chosen operation was "divisao" (division), the function checks if n2 (the divisor) is not equal to zero. If it isn’t zero, it returns the result of dividing n1 by n2. If n2 is zero, it returns the error message "Error: Division by zero!" to avoid an invalid division.

11. Handles invalid operations
        else:
            return "Operação inválida"


Explanation: If the user enters an operation that isn’t recognized (i.e., something other than "soma", "subtracao", "multiplicacao", or "divisao"), the function returns the message "Invalid operation", indicating the operation entered is not valid.

12. Calls the function and displays the result
    resultado = calcular(n1, n2, escolha)
    print(f"O resultado da {escolha} é: {resultado}")


Explanation: The function calcular() is called with the values n1, n2, and the chosen operation escolha. The result returned by the function is stored in the variable resultado. Then, the print() function displays the result, showing the type of operation performed and its result.

Summary of what the code does:

The program enters a loop that continues until the user types "exit".

If the user chooses to continue, they enter two numbers and choose a mathematical operation.

The program performs the operation and displays the result.

If the user types "exit", the program ends.

This code allows the user to perform multiple calculations (addition, subtraction, multiplication, or division) interactively until they decide to exit the program.



"""

1. Loop principal — permite repetir operações até o usuário digitar 'sair'
while True:


Explicação: O while True cria um loop infinito. Ele vai continuar executando até que uma condição de parada seja atendida, o que ocorre quando o usuário digita "sair".

2. Pergunta se o usuário deseja sair ou continuar
    sair = input("Digite 'sair' para encerrar ou Enter para continuar: ")


Explicação: A função input() exibe uma mensagem para o usuário e espera que ele digite algo. O que o usuário digitar é armazenado na variável sair. O objetivo dessa linha é perguntar ao usuário se ele deseja sair ou continuar.

3. Verifica se o usuário digitou 'sair'
    if sair == "sair":
        break


Explicação: Aqui, o código verifica se o valor da variável sair é igual à string "sair". Se for, o comando break é executado, que sai do loop while, encerrando a execução do programa.

4. Lê os dois números do usuário
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))


Explicação: As duas linhas acima solicitam que o usuário insira dois números. A função input() lê o que o usuário digitar como uma string, e a função float() converte essa string em um número decimal (número de ponto flutuante). Esses valores são atribuídos às variáveis n1 e n2.

5. Lê a operação desejada do usuário e normaliza para minúsculas
    escolha = input("Escolha a operação (soma, subtracao, multiplicacao ou divisao): ").lower()


Explicação: A função input() solicita que o usuário escolha uma operação entre soma, subtração, multiplicação ou divisão. O método .lower() converte o que o usuário digitar para letras minúsculas, garantindo que a comparação posterior seja feita de forma insensível a maiúsculas/minúsculas (ou seja, o usuário pode digitar tanto "SOMA" quanto "soma").

6. Definição da função de cálculo
    def calcular(n1, n2, operacao):


Explicação: Aqui começa a definição de uma função chamada calcular. Ela recebe três parâmetros: n1, n2 (os números inseridos pelo usuário) e operacao (a operação escolhida pelo usuário).

7. Realiza a operação com base na escolha do usuário
        if operacao == "soma":
            return n1 + n2


Explicação: A função calcular começa verificando se a operação escolhida foi "soma". Se for, ela retorna a soma dos dois números n1 e n2.

8. Verifica se a operação é subtração
        elif operacao == "subtracao":
            return n1 - n2


Explicação: Se a operação escolhida for "subtracao", a função retorna a subtração de n2 de n1.

9. Verifica se a operação é multiplicação
        elif operacao == "multiplicacao":
            return n1 * n2


Explicação: Se a operação escolhida for "multiplicacao", a função retorna o produto de n1 e n2.

10. Verifica se a operação é divisão
        elif operacao == "divisao":
            if n2 != 0:
                return n1 / n2
            else:
                return "Erro: Divisão por zero!"


Explicação: Se a operação escolhida for "divisao", o código verifica se o divisor (n2) é diferente de zero. Se for, ele retorna o resultado da divisão n1 / n2. Caso contrário, retorna a mensagem de erro "Erro: Divisão por zero!", para evitar uma divisão inválida.

11. Caso a operação seja inválida
        else:
            return "Operação inválida"


Explicação: Caso o usuário digite uma operação que não seja "soma", "subtracao", "multiplicacao" ou "divisao", a função retorna a mensagem "Operação inválida", informando que a entrada não é reconhecida.

12. Chama a função de cálculo e exibe o resultado
    resultado = calcular(n1, n2, escolha)
    print(f"O resultado da {escolha} é: {resultado}")


Explicação: A função calcular() é chamada com os valores n1, n2 e a operação escolha fornecida pelo usuário. O resultado retornado pela função é armazenado na variável resultado. Em seguida, a função print() exibe o resultado na tela, mostrando o tipo de operação que foi realizada e o resultado.

Resumo do que o código faz:

O programa entra em um loop infinito, perguntando ao usuário se deseja continuar ou sair.

"""


Se o usuário optar por continuar, ele digita dois números e escolhe uma operação matemática.

O programa executa a operação e exibe o resultado.

Se o usuário digitar "sair", o loop é interrompido e o programa é finalizado.
