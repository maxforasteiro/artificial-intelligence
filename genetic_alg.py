import random

def fitness (indiv):
  fit = 0
  for var in indiv:
    fit = fit + var**2
  return fit

def cria_ind(nDim, valMin, valMax):
  return [
    random.uniform(valMin, valMax) for i in range(nDim)
  ]

def cria_pop (tamPop, nDim, valMin, valMax):
  return [
    cria_ind(nDim, valMin, valMax) for i in range(tamPop)
  ]

def torneio(vetFitness, tamTorneio):
  competidores = list(range(len(vetFitness)))
  indices = random.sample(competidores, tamTorneio)
  valores = [vetFitness[i] for i in indices]
  vencedor1 = indices[valores.index(min(valores))]
  competidores.remove(vencedor1)
  indices = random.sample(competidores, tamTorneio)
  valores = [vetFitness[i] for i in indices]
  vencedor2 = indices[valores.index(min(valores))]
  return vencedor1, vencedor2

def cruzamento(ind1, ind2):
  return [(ind1[i]+ind2[i])/2 for i in (range(len(ind1)))]

def mutacao(indiv, probMulti, ruido):
  indiv = list(indiv)
  for i in range(len(indiv)):
    if random.random() < probMulti:
      indiv[i] = indiv[i] + random.uniform(-ruido, ruido)
  return indiv

v1, v2 = torneio(vetFitness, tamTorneio)

valMin = -10
valMax = 10
nDim = 2
