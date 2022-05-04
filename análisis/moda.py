import pandas as pd
pokemon=pd.read_csv("pokemon.csv")

class Moda:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  moda=self.csv[self.columna].mode()
  print("La moda es la siguiente:")
  print(moda)