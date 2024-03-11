import numpy as np

#Fiquei em dúvida sobre o produto interno, então passei pra um array e usei o produto da numpy
def dot(matriz1, matriz2):

 
    matriz1_np = np.array(matriz1)
    matriz2_np = np.array(matriz2)
  
    produto = np.vdot(matriz1_np, matriz2_np)
    
    return produto

