# Librería scikit-image
print("Librería scikit-image")

from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from skimage.transform import swirl

print("---------"*7)

from skimage import exposure

# Ajustes de brillo
print("\nAjustes de brillo - Girasol\n")

imagen1 = imread('girasol.png')

# Modificación de la exposición de la imagen, de modo que quede más brillante (gamma más baja), o más oscura (gamma más alta)
brillante = exposure.adjust_gamma(imagen1, gamma=0.25,gain=1)
oscura = exposure.adjust_gamma(imagen1, gamma=2.5,gain=1)

# Gráfica de las imágenes, todas juntas para poderlas comparar
plt.subplot(131), imshow(imagen1)
plt.title('Imagen original')

plt.subplot(132),imshow(brillante)
plt.title('Imagen brillante')

plt.subplot(133),imshow(oscura)
plt.title('Imagen oscura')

#plt.tight_layout()
plt.savefig("gira-brill-oscur.png")

plt.close()

print("---------"*7)

from skimage.color import rgb2hsv

# Cambiar formato de imagen
print("\nCambiar formato de imagen - Mariposa")

# Permite devolver un vector de un único color o una matriz de imagen en paquete RGB en la representación de color RGB convertida en la representación de color HSV

# RGB: los valores del color rojo, verde y azul están entre 0 y 255. HSV: sus valores definen el matiz (entre 0 y 359 grados), saturación (entre 0% y 100%) y valor (entre 0% y 100%).

# Traemos la imagen a utlizar usando imread
imagen2 = imread('mariposa.png')

# Creamos una variable con la función de skimage que convierte del formato RGB al HSV
imagen2_nueva = rgb2hsv(imagen2)

# Usar matplotlib para ubicar las imágenes juntas y ver la comparación
plt.subplot(121), imshow(imagen2)
plt.title('En formato RGB') 

plt.subplot(122), imshow(imagen2_nueva)
plt.title('En formato HSV') 

plt.savefig("mari-HSV.png")