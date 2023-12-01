import cv2

def erosion(image, kernel):
    rows, cols, channels = image.shape
    result = image.copy()

    i = 1
    while i < rows - 1:
        j = 1
        while j < cols - 1:
            k = 0
            while k < channels:
                # Effectuer l'érosion en utilisant le noyau
                min_val = min(
                    image[i - 1, j - 1, k] & kernel[0][0],
                    image[i - 1, j, k] & kernel[0][1],
                    image[i - 1, j + 1, k] & kernel[0][2],
                    image[i, j - 1, k] & kernel[1][0],
                    image[i, j, k] & kernel[1][1],
                    image[i, j + 1, k] & kernel[1][2],
                    image[i + 1, j - 1, k] & kernel[2][0],
                    image[i + 1, j, k] & kernel[2][1],
                    image[i + 1, j + 1, k] & kernel[2][2]
                )
                result[i, j, k] = min_val
                k += 1
            j += 1
        i += 1

    return result

def dilatation(image, kernel):
    rows, cols, channels = image.shape
    result = image.copy()

    i = 1
    while i < rows - 1:
        j = 1
        while j < cols - 1:
            k = 0
            while k < channels:
                # Effectuer la dilatation en utilisant le noyau
                max_val = max(
                    image[i - 1, j - 1, k] | kernel[0][0],
                    image[i - 1, j, k] | kernel[0][1],
                    image[i - 1, j + 1, k] | kernel[0][2],
                    image[i, j - 1, k] | kernel[1][0],
                    image[i, j, k] | kernel[1][1],
                    image[i, j + 1, k] | kernel[1][2],
                    image[i + 1, j - 1, k] | kernel[2][0],
                    image[i + 1, j, k] | kernel[2][1],
                    image[i + 1, j + 1, k] | kernel[2][2]
                )
                result[i, j, k] = max_val
                k += 1
            j += 1
        i += 1

    return result

# Lecture de l'image en couleur
image = cv2.imread('univer.jpg')

# Noyau d'érosion
erosion_kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# Noyau de dilatation
dilatation_kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# Appliquer l'érosion
eroded_image = erosion(image, erosion_kernel)

# Appliquer la dilatation
dilated_image = dilatation(image, dilatation_kernel)

# Afficher les images originales et transformées
cv2.imshow('Image Originale', image)
cv2.imshow('Image Erodee', eroded_image)
cv2.imshow('Image Dilatee', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
