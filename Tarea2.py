# Alejandro Restrepo Giraldo CC: 1001389709

import numpy as np
from vector import VectorCartesiano
from vector import VectorPolar

# Vectores
a = VectorCartesiano(1.5, 0, 2.4)
print("a = ", end="")
a.Print()
b = VectorCartesiano(0, 1, 9)
print("b = ", end="")
b.Print()
c = VectorCartesiano(4.2, 0.05, 0)
print("c = ", end="")
c.Print()
print("\n")

# Vectores en coordenadas esféricas
a.VectorEsferico()
b.VectorEsferico()
c.VectorEsferico()

# Producto punto
ab = a*b
ac = a*c
bc = b*c

# Productos Cruz
axb = a.Cruz(b)
axc = a.Cruz(c)
bxc = b.Cruz(c)

# Ángulos entre vectores está dado por ángulo = arcos(a*b/|a||b|)
aab = np.arccos(a*b/(a.magnitud*b.magnitud))
aac = np.arccos(a*c/(a.magnitud*c.magnitud))
abc = np.arccos(b*c/(b.magnitud*c.magnitud))


print("\nProductos punto:")
print("a*b = %f"%ab)
print("a*c = %f"%ac)
print("b*c = %f"%bc)


print("\nProductos cruz:")
print("axb = ", end="")
axb.Print()
print("axc = ", end="")
axc.Print()
print("bxc = ", end="")
bxc.Print()


print("\nÁngulos entre vectores:")
print("Ángulo entre a y b : %f"%aab)
print("Ángulo entre a y c : %f"%aac)
print("Ángulo entre b y c : %f"%abc)













