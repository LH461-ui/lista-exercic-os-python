# Sistema Escolar Simples

# Pedindo as 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificando a média e exibindo a mensagem
if media < 6:
    print("Reprovado, média menor que 6. Sua média foi:", media)
else:
    print("Você foi aprovado! Sua média foi:", media)