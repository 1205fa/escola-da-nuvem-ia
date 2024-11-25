import random 

def main():
    valor = [random.randint(1,10000) for _ in range(100)]

    maior = (max(valor))
    posicao = valor.index(maior) + 1

    resultado = {
        "Número": valor,
        "Maior Valor": maior,
        "Posição": posicao
    }

    print("\n Número gerados: ")
    print(valor)
    print("\n Maior valor:", maior)
    print("Posição do Maior Valor: ", posicao)

if __name__ == "__main__":
    main()