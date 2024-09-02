import cv2
import os

# Load the cascade file
cascade_path = 'C:/Users/VIVEK KUMAR/Python/Harry_Demo_Projects/Face_Recognition/haarcascade_frontalface_default.xml'  # e.g., 'C:/Users/VIVEK KUMAR/Python/Harry_Demo_Projects/Face_Recognition/haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    print(f"Error: The Haar Cascade file '{cascade_path}' was not found.")
    exit()

face_cascade = cv2.CascadeClassifier(cascade_path)

# Read the input image
image_path = 'C:/Users/VIVEK KUMAR/Python/Harry_Demo_Projects/Face_Recognition/image.png'  # e.g., 'C:/Users/VIVEK KUMAR/Python/Harry_Demo_Projects/Face_Recognition/1.png'
if not os.path.exists(image_path):
    print(f"Error: The image file '{image_path}' was not found.")
    exit()

image = cv2.imread(image_path)
if image is None:
    print(f"Error: The image file '{image_path}' could not be opened.")
    exit()

# Resize the image
img = cv2.resize(image, None, fx=0.3, fy=0.3)

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
