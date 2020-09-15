# Alejandro Restrepo Girldo  CC: 1001389709

# Librerías  
import numpy as np

"----------------------------------------------------------------------------------------"

# Clase de vector cartesiano
class VectorCartesiano:
   
   # Constructor
   def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z
      # Se calcula la magnitud de inmediato
      self.magnitud = (self.x**2 + self.y**2 + self.z**2)**0.5
      
   # Producto escalar
   def __mul__(self,other):
      return self.x*other.x + self.y*other.y + self.z*other.z

   # Producto cruz
   def Cruz(self, other):
      return VectorCartesiano(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z , self.x*other.y - self.y*other.x)

   # Suma de vectores
   def __add__(self, other):
      return VectorCartesiano(self.x + other.x,  self.y + other.y, self.z + other.z)

   # Resta de vectores
   def __sub__(self, other):
      return VectorCartesiano(self.x - other.x,  self.y - other.y, self.z - other.z)

   # Componentes del vector
   def __getitem__(self,index):
      if index == 1:
         print("La componente x del vector es %f" %self.x)
         return self.x
      if index == 2:
         print("La componente y del vector es %f" %self.y)
         return self.y
      if index == 3:
         print(f"La componente z del vector es %f" %self.z)
         return self.z
      
   # Comparación de vectores
   def __eq__(self, other):
      if self.x != other.x or self.y != other.y or self.z != other.z:
         print("Los vectores son diferentes.")
      
      else:
         print("Los vectores son iguales.")



   # Componentes del vector en coordenadas esféricas
   def VectorEsferico(self):

      # Componentes esféricas
      r = self.magnitud
      # Ángulo polar
      th = np.arccos(self.z/self.magnitud)
      # Ángulo azimutal
      if self.x == 0:
         ph = np.pi/2
      else:
         ph = np.arctan(self.y/self.x)
      
      # Componentes del vector en coordenadas esféricas. Calculadas como el producto punto entre el vector y el unitario correspondiente. 
      # vector*u_r
      Ar = np.sin(th)*np.cos(ph)*self.x + np.sin(th)*np.sin(ph)*self.y + np.cos(th)*self.z
      # vector*u_th
      Ath = np.cos(th)*np.cos(ph)*self.x + np.cos(th)*np.sin(ph)*self.y - np.sin(th)*self.z
      # vector*u_ph
      Aph = -np.sin(ph)*self.x + np.cos(th)*self.y

      print("El vector en coordenadas esféricas es %f r + %f θ + %f φ "%(Ar,Ath,Aph))
      print("Cuyas coordenadas son r = %f, θ = %f y φ = %f \n"%(r,th,ph))
      
   # Impresión de vectores
   def Print(self):
      print(f"[{self.x},{self.y},{self.z}]")
      



"------------------------------------------------------------------------------------------"




# Clase de vector dadas las coordenadas polares
class VectorPolar(VectorCartesiano):
   
   def __init__(self, r, th, ph):
      
      # Componente radial. Se toma el valor absoluto para que esté en el rango [0,inf).
      self.r = abs(r)


      # Ángulo polar theta. Debe estar en [0,pi]
      # Si está en el intervalo se define el atributo de inmediato
      if th <= np.pi and 0 <= th:
         self.th = th

      # Si se entrega un valor menor que cero
      if th < 0 :
         # Se lleva el valor al intervalo (-2pi,0)
         while th <= -2*np.pi :
            th = th + 2*np.pi
         # Si está en [-pi,0) se toma el valor absoluto
         if th >= -np.pi:
            self.th = abs(th)
         # Si está en (pi, 2pi) se toma el complemento
         if th < -np.pi:
            self.th = 2*np.pi + th
      
      # Si se entrega un valor en (pi,inf)
      if th > np.pi :
         # Se lleva al intervalo [0,2pi)
         while np.pi <= th:
            th = th - 2*np.pi
         # Si está en (0,pi] se toma el valor
         if th <= np.pi:
            self.th = th
         # Si está en (pi,2pi) se toma el suplemento
         if th > np.pi:
            self.th = 2*np.pi - th

    
      # Ángulo azimutal phi. Debe estar en [0,2pi)
      # Si está en este intervalo se define el atributo de inmediato
      if ph < 2*np.pi and 0 <= ph:
         self.ph = ph

      # Si se entrega un valor negativo
      if ph < 0 :
         # Se lleva al intervalo (-2pi,0)
         while ph < -2*np.pi :
            ph = ph + 2*np.pi
         # Se toma el ángulo conjugado
         self.ph = 2*np.pi + ph
      
      # Si se entrega un valor en (2pi, inf)
      if ph >= 2*np.pi :
         # Se lleva al intervalo (0,2pi)
         while 2*np.pi <= ph:
            ph = ph - 2*np.pi
         self.ph = ph


      # Coordenadas x,y,z correspondientes a las r, th, ph
      x = self.r*np.sin(self.th)*np.cos(self.ph)
      y = self.r*np.sin(self.th)*np.sin(self.ph)
      z = self.r*np.cos(self.th)

      # Vector cartesiano correspondiente al punto r, th, ph
      VectorCartesiano.__init__(self,x,y,z)



   # Impresión de coordenadas polares
   def PrintCoord(self):
      print(f"[{self.r},{self.th},{self.ph}]")



"------------------------------------------------------------------------------------------"

































