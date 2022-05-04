import pandas as pd
pokemon=pd.read_csv("pokemon.csv")

class Mediana:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  mediana=self.csv[self.columna].median()
  print("La mediana es la siguiente:")
  print(mediana)