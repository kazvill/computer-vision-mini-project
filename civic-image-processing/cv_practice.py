import cv2
import os

# Load image
img = cv2.imread("sample.jpg")  # change to your civic image name if needed

if img is None:
    raise FileNotFoundError("Could not load image. Check the filename and path for 'sample.jpg'.")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny edge detection
edges = cv2.Canny(blur, 100, 200)

# Colour masking (detect red-ish colours)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = (0, 100, 100)
upper_red = (10, 255, 255)
mask = cv2.inRange(hsv, lower_red, upper_red)
masked_img = cv2.bitwise_and(img, img, mask=mask)

# --- Save results as new image files ---
# Make output filenames (you can rename these if you want)
cv2.imwrite("civic_edges.png", edges)
cv2.imwrite("civic_red_mask.png", masked_img)
cv2.imwrite("civic_blur.png", blur)   # optional, just to see the blurred grayscale

print("Saved: civic_edges.png, civic_red_mask.png, civic_blur.png")

# Show results on screen as before
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("Red Mask", masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
