#Programa em python que calcula a seguência de fibonnaci

def fibonnaci(n):
    
    """
    Gerar a série de fibonnaci (lógica) até o N-esimo termo
    """
    
    #iniciar os primeiros valores da série
    a, b = 0, 1
    resultado = [a]
    
    #Geração de termo (É a lógica por trás da resolução do problema)
    for i in range(1, n):
        resultado.append(b)
        a, b = b, a + b
    
    #Função devolve  o resultado: [0,1,1,2,3]
    return resultado 

def main():
    try:
        N = int(input())
        
        if N <= 0 or N >= 46:
            raise ValueError("O número precisa estar entre 1 e 45")
        
        fibonnaci_seguence = fibonnaci(N)
        
        print("".join(map(str, fibonnaci_seguence)))
        
        
    except ValueError as ve:
        print(f"Erro {ve}")
if __name__ == "__main__":
    main()
