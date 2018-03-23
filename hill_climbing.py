import matplotlib.pyplot as plt
import random

def objfun(x):
  return va * (x ** 2) + vb * x + vc

va = 1
vb = -5
vc = 30

xmin = -100
xmax = 100

points_qtd = 50

step = (xmax - xmin) / (points_qtd - 1)

vector = [xmin]
for i in range(1, points_qtd + 1):
  vector.append(vector[-1] + step)

# print(vector)

fx = [ objfun(x) for x in vector ]

minx = - vb / (2 * va)
delta = vb ** 2 - 4 * va * vc
miny = - delta / 4 * va

plt.clf()
plt.plot(vector, fx, "b")
plt.plot(minx, miny, "g", marker="x",
  markersize=12, markeredgewidth=3,
  linewidth=3)

sol = random.uniform(xmin, xmax)

for iter in range(100):
  vizinha = sol + random.uniform(-20, 20)
  y_vizinha = objfun(vizinha)

  if y_vizinha < y:
    y = y_vizinha
    sol = vizinha

    plt.plot(sol, y, "go", markersize=7)
    plt.draw()
    plt.pause(0.5)