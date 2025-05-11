# Calculadora de Desconto Simples

# Pede o valor da compra
valor = float(input("Digite o valor da compra: R$"))

# Verifica se tem desconto
if valor > 100:
    valor_final = valor * 0.75  # Aplica 25% de desconto
else:
    valor_final = valor        # Sem desconto

# Mostra o valor final
print("Valor final a pagar: R$", valor_final)