# %%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos serve para calcular o juros financeiro 
    a partir de um aporte. Deve-se considedar o valor, a taxa 
    de juros atual e o tempo (em anos) para cálculo do valor 
    a ser retornado.
    
    aporte:
        um número inteiro, que represente o valor em Reais(R$)
    taxa:
        um número float entre 0 e 1 que represente o valor da taxa de juros
    anos:
        um número inteiro maior ou igual a 1 que representa o tempo que o investimento terá liquidez. 
    """
    return aporte * (1 + taxa) ** anos
  
# %%
juros_compostos(1000, 0.13, 4)

# %%
juros_compostos(taxa=0.13, anos=4, aporte=1000)
# %%
