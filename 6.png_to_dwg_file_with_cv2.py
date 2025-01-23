import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyautocad import Autocad, APoint

# Load the image
image_path = 'image2.png'

# Check if the image is loaded properly
img = cv2.imread(image_path)

if img is None:
    print(f"Error: The image at {image_path} could not be loaded.")
else:
    print(f"Image loaded successfully. Shape: {img.shape}")

     

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply edge detection (Canny edge detector)
    edges = cv2.Canny(gray, 30, 200, apertureSize=7) #You can adjust the details by changing these numbers.

    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=2, maxLineGap=50) #You can adjust the details by changing these numbers.

    # Debugging: Check the number of lines detected
    if lines is not None:
        print(f"Detected {len(lines)} lines.")
    else:
        print("No lines detected.")

    # Display the image with detected edges
    cv2.imshow("Detected Edges", edges)  # Show the edges detected by the Canny detector
    cv2.waitKey(0)  # Wait for a key press to continue
    cv2.destroyAllWindows()

    # Draw the detected lines on the original image (for visualization)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show the image with detected lines
    cv2.imshow("Detected Lines", img)  # Show the image with detected lines
    cv2.waitKey(0)  # Wait for a key press to continue
    cv2.destroyAllWindows()

    # Convert image coordinates to AutoCAD coordinates (scale factor for mapping)
    scaling_factor = 0.1  # You can adjust this depending on the desired scale in AutoCAD

    # Create AutoCAD instance
    acad = Autocad(create_if_not_exists=True)
    acad.app.Documents.Add()  # Create a new document

    # Draw the detected lines in AutoCAD
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # Convert pixel coordinates to AutoCAD coordinates using scaling factor
        start_point = APoint(x1 * scaling_factor, y1 * scaling_factor)
        end_point = APoint(x2 * scaling_factor, y2 * scaling_factor)
        acad.model.AddLine(start_point, end_point)
    # Save the AutoCAD drawing as a DWG file
    acad.app.ActiveDocument.SaveAs("C:/Users/Atakan EKŞİ/Documents/autocad/drawing18.dwg")
    print("DWG file saved as 'generated_floor_plan.dwg'")

    # Optionally, close AutoCAD (can be removed if you want AutoCAD to stay open)
    #acad.app.ActiveDocument.Close()
