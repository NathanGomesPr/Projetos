x = 10.0
precision = 1E-06
iterations = 0

while x > precision:
    x = x / 2.0
    iterations += 1

print("Último valor de x:", x)
print("Número de iterações:", iterations)