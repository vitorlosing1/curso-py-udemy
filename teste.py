class Cachorro():

  def __init__(self, nomeCa, racaCa):
    self.nome = nomeCa
    self.raca = racaCa

  def latir(self):
    print(f'{self.nome} latiu')

  def comer(self):
    print(f'{self.nome} comeu')


cachorro = Cachorro("Tobi", "VL")

print(cachorro.nome)
print(cachorro.raca)
cachorro.latir()
cachorro.comer()