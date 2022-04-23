import numpy as np


def eliminacaoGauss(matriz):
  for e in range(len(matriz)-1):
    for i in range(e+1, len(matriz)):
      pivo = matriz[e][e]
      multiplicador = -(matriz[i][e]/pivo)
      matriz[i][:] = matriz[i][:] + (multiplicador*matriz[e][:])

  print(matriz)