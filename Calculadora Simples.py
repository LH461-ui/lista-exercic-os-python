
print("Calculadora Simples")
print("Selecione OPERAÇÃO")
print("1- SOMA")
print("2- SUBTRAÇÃO")
print("3- MULTIPLICAÇÃO")
print("4- DIVISÃO")
print("5- POTÊNCIAÇÃO")
print("6- SAIR")

escolha = input("Digite a operação desejada: ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Por favor, digite números válidos")
    exit

if escolha == 1:
    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
elif escolha == 2:
    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
elif escolha == '3':
    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
elif escolha == '4':
    if num2 == 0:
        print("Error: Divisão por zero não é permitida")
    else:
        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
elif escolha == '5':
    print(f"Resultado: {num1} ** {num2} = {num1 ** num2}")
else:
    print("Opção inválida")
if __name__ == "__main__":
    exit
    