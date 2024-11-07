import math
import numpy as np
import matplotlib.pyplot as plt

def probabilidad(grupo, year=365):
    grupo = int(grupo)
    probabilidad_negativa = ((math.factorial(year) / math.factorial(year - grupo)) / (year ** grupo))
    probabilidad_positiva = 1 - probabilidad_negativa
    return probabilidad_positiva

# Generar valores de x
x_values = np.arange(2, 100)
y_values = [probabilidad(x) for x in x_values]

# Graficar
plt.plot(x_values, y_values, label='Probabilidad de coincidencia de cumpleaños', color='blue')
plt.title('Probabilidad de al menos dos personas compartiendo cumpleaños')
plt.xlabel('Número de personas en el grupo')
plt.ylabel('Probabilidad')
plt.ylim(0, 2)
plt.legend()
plt.grid(True)
plt.show()
