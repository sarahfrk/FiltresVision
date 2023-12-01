import cv2
import numpy as np

# Charger l'image en niveaux de gris
image = cv2.imread('univer.jpg')

# Appliquer le filtre Laplacien
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convertir l'image de sortie en uint8 et ajuster les valeurs pour l'affichage
laplacian_output = np.uint8(np.absolute(laplacian))

# Afficher l'image originale et l'image filtrée
cv2.imshow('Image Originale', image)
cv2.imshow('Filtre Laplacien', laplacian_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
