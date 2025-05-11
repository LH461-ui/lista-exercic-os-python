if __name__ == "__main__":
    valor = float(input("Digite um número para verificar o intervalo [10, 50]: "))
    if 10 <= valor <= 50:
        print(f"O número {valor} está no intervalo de 10 a 50.")
    else:
        print(f"O número {valor} NÃO está no intervalo de 10 a 50.")