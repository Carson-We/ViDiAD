import cv2

def calculate_distance(focal_length, known_width, pixel_width):
    distance = (known_width * focal_length) / pixel_width
    return distance

# Set the known parameters
known_width = 0.2  # Width of the known object in meters
focal_length = 0.3  # Focal length of the camera in meters

# Measure the pixel width of the known object in the image
image = cv2.imread('image.jpg')
# Mark the region of the known object in the image (e.g., using bounding box or other detection methods)
pixel_width = 100  # Pixel width of the known object in the image

# Calculate the distance
distance = calculate_distance(focal_length, known_width, pixel_width)
print("Estimated distance:", distance, "meters")
