import pandas as pd
pokemon=pd.read_csv("pokemon.csv")

  class Rango:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  rango=self.csv[self.columna].mode()
  print("El rango es el siguiente:")
  print(rango)