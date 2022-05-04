import pandas as pd 
pokemon=pd.read_csv("pokemon.csv")



class varianza:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    varianza=self.csv[self.columna].var()
    print("La Varianza es :")
    print(varianza)