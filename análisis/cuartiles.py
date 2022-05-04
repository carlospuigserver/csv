import pandas as pd 
pokemon=pd.read_csv("pokemon.csv")

class Q1:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    q1=self.csv[self.columna].mad()
    print("El primer cuartil  es :")
    print(q1)


class Q3:
  def __init__(self,csv,columna):
    self.csv=csv
    self.columna=columna
  def operacion(self):
    q3=self.csv[self.columna].mad()
    print("El tercer cuartil  es :")
    print(q3)

