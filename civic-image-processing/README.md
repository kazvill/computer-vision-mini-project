# Civic Image Processing (OpenCV)

This project demonstrates basic image processing techniques using OpenCV on a car image. It focuses on feature extraction and colour segmentation.

---

## 🚗 Features Implemented

### **1. Grayscale Conversion**
Converts the original BGR image into grayscale for easier processing.

### **2. Gaussian Blur**
Smooths the image and reduces noise before edge detection.

### **3. Canny Edge Detection**
Detects the edges and outlines of the vehicle.

### **4. HSV Colour Masking (Red Detection)**
Isolates red regions (e.g., badges or lights) using HSV colour ranges.

---

## 📁 Files in This Folder

- `cv_practice.py` — main processing script  
- `sample.jpg` — image used in the demo  
- `civic_edges.png` — result of edge detection  
- `civic_blur.png` — blurred grayscale image  
- `civic_red_mask.png` — red-colour mask overlay  

---

## 🛠️ Technologies Used
- **Python**
- **OpenCV (cv2)**
- **NumPy**

---

## ▶️ How to Run

```bash
python cv_practice.py
