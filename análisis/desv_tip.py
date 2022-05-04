import pandas as pd 
pokemon=pd.read_csv("pokemon.csv")

class desvia_típica:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    desv=self.csv[self.columna].mad()
    print("La desv típic es :")
    print(desv)