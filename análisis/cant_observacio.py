class columnas:
  def __init__(self,csv):
    self.csv=csv
  def operacion(self):
    print("La cantidad de columnas que hay es de:", self.csv.shape[1])


class filas:
  def __init__(self,csv):
    self.csv=csv
  def operacion(self):
    print("La cantidad de filas que hay es de:", self.csv.shape[0])