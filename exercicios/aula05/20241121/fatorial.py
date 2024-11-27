#Criar o fatorial de N (N É a multiplicação de N pelos seus antecessores)

#Inicia nossa função
def calculo_fatorial(n):
    
    """
    Função calcule o fatorial de um número inteiro "N"
    
    """

    fatorial = 1
    #Cria as regras de número fatorial    
    for i in range(2, n + 1):
        fatorial *= i
        

    return fatorial

#Cria a função principal
def main():  #Garante que a função seja executada quando chamada diretamente
    try:
        
        #Entrada de dados
        N = int(input())
        
        #Condição de entrada de dados
        if N <=0 or N >=13:
            raise ValueError(" Número precisa estar entre 1 e 12")

#Tratativa dos dados
        resultado = calculo_fatorial(N)
        
        #Mostra os dados
        print(resultado)
        
    except ValueError as  error:
        print(f"Erro {error}")
        
        
        
if __name__ == "__main__":
    main()
    
    
     