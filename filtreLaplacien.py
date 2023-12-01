import cv2

def laplacian_filter(img):
    rows, cols, channels = img.shape
    filtered_img = img.copy()

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            for k in range(channels):
                # Calculate the Laplacian value
                laplacian_value = (
                    img[i - 1, j, k] +
                    img[i + 1, j, k] +
                    img[i, j - 1, k] +
                    img[i, j + 1, k] -
                    4 * img[i, j, k]
                )

                # Update the pixel value with the absolute Laplacian value
                filtered_img[i, j, k] = abs(laplacian_value)

    return filtered_img

# Execution
# Read the image
image = cv2.imread('univer.jpg')

# Apply the Laplacian filter
filtered_image = laplacian_filter(image)

# Display the original and filtered images
cv2.imshow('Image Originale', image)
cv2.imshow('Image Filtree (Laplacien)', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
