def exibir_tabuleiro(tab):
    print()
    for i in range(3):
        print(" | ".join(tab[i]))
        if i < 2:
            print("--+---+--")
    print()

def verificar_vitoria(tab, jogador):
    # Linhas, colunas e diagonais
    for i in range(3):
        if all([tab[i][j] == jogador for j in range(3)]) or all([tab[j][i] == jogador for j in range(3)]):
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == jogador or tab[0][2] == tab[1][1] == tab[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        try:
            linha = int(input("Escolha a linha (1, 2 ou 3): ")) - 1
            coluna = int(input("Escolha a coluna (1, 2 ou 3): ")) - 1
        except ValueError:
            print("Digite apenas números válidos!")
            continue

        if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
        else:
            print("Posição inválida, tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        elif jogadas == 9:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo_da_velha()