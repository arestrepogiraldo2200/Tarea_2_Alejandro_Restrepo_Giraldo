# Alejandro Restrepo Giraldo CC: 1001389709

import numpy as np
from vector import VectorCartesiano
from vector import VectorPolar


print("Se prueba la clase VectorCartesiano para ")
  
v1 = VectorCartesiano(1,1,0)
print("v1 = ", end="")
v1.Print()
v2 = VectorCartesiano(0,1,1)
print("v2 = ", end="")
v2.Print()

print("\nProducto interno debe resultar en 1:")
v3 = v1*v2
print(v3)

print("\nProducto cruz v1xv2 debe resultar en (1,-1,1):")
v4 = v1.Cruz(v2)
v4.Print()

print("\nSuma v1 + v2 debe resultar en (1,2,1):")
v5 = v1+v2
v5.Print()

print("\nResta v1 - v2 debe resultar en (1,0,-1):")
v6 = v1-v2
v6.Print()

print("Entradas de v1:")
a = v1[1]

b = v1[2]

c = v1[3]


print("Test de igualdad:")
v1 == v2


print("\n\nPrueba de la clase VectorPolar. Se prueba que para las coordenadas r = -3, θ = -3pi/2 y φ = -5pi se llevan a los dominios adecuados r = 3, θ = pi/2 y φ = pi ")

pol = VectorPolar(-3,-3*np.pi/2,-5*np.pi)
pol.PrintCoord()

print("\n El vector cartesiano correspondiente a las coordenadas (3^0.5, arctan(2^0.5), pi/4) debe ser (1,1,1) y su magnitud debe ser 3^0.5 = 1.73205080757")

pol1 = VectorPolar(np.sqrt(3), np.arctan(np.sqrt(2)), (np.pi)/4)
print("El vector es:", end="")
pol1.Print()
print("La magnitud es ", end = "" )
print(pol1.magnitud)


print("Como ya se comprobaron todas las operaciones vectorales de VectorCartesiano, estas funcionan para VectorPolar.")



































