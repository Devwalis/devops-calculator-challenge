def calcular_media():
    numeros = []
    print("\nDigite os números para calcular a média.")
    print("Pressione Enter sem digitar nada para finalizar.\n")

    while True:
        entrada = input(f"Digite o {len(numeros) + 1}º número (ou Enter para finalizar): ")

        if entrada == "":
            break

        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Valor inválido! Digite apenas números.")

    if not numeros:
        return "Nenhum número foi informado."

    media = sum(numeros) / len(numeros)
    return f"Média: {media:.2f} (baseada em {len(numeros)} números)"
