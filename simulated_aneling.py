import matplotlib.pyplot as plt
import random
import math

def objfun(x):
  return 10 * math.sin(0.3 * x) * math.sin(1.3 * x ** 2) + 0.00001 * x ** 4 + 0.2 * x + 80

xmin = -50
xmax = 50

points_qtd = 1000

step = (xmax - xmin) / float(points_qtd - 1)

vector = [xmin]
for i in range(1, points_qtd + 1):
  vector.append(vector[-1] + step)

# print(vector)

fx = [ objfun(x) for x in vector ]

plt.clf()
plt.plot(vector, fx, "b")
plt.plot(minx, miny, "g", marker="x",
  markersize=12, markeredgewidth=3,
  linewidth=3)

sol = random.uniform(xmin, xmax)
y = objfun(sol)
prob = 0.5
initial_temp = 100
alpha = 0.9
best_sol = sol
best_y = y

for iter in range(100):
  vizinha = sol + random.uniform(-20, 20)
  if vizinha > xmax
    vizinha = xmax
  else if vizinha < xmin
    vizinha = xmin

  y_vizinha = objfun(vizinha)

  delta = y_vizinha - y

  if y_vizinha < y or random.uniform(0, 1) < math.exp(-delta / initial_temp):
    y = y_vizinha
    sol = vizinha

    if y < best_y
      best_y = y
      best_sol = sol

    plt.plot(sol, y, "go", markersize=7)
    plt.draw()
    plt.pause(0.5)

  initial_temp = initial_temp * alpha