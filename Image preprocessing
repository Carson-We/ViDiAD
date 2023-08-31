import cv2
import numpy as np

def preprocess_image(image):
    # Resize the image
    resized_image = cv2.resize(image, (640, 480))

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blurred_image, 100, 200)

    # Return the preprocessed image
    return edges

# Read the input image
image = cv2.imread('input_image.jpg')

# Perform image preprocessing
preprocessed_image = preprocess_image(image)

# Display the preprocessed image
cv2.imshow('Preprocessed Image', preprocessed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
