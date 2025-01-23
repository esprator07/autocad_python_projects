from pyautocad import Autocad, APoint

# Connect to AutoCAD
acad = Autocad(create_if_not_exists=True)

# Open an existing drawing
drawing_path = r"/Documents/autocad/Drawing6.dwg"
acad.app.Documents.Open(drawing_path)

# Iterate over all lines in the drawing and delete the first line found
for obj in acad.iter_objects("AcDbLine"):
    print(f"Deleting line with start point: {obj.StartPoint}, end point: {obj.EndPoint}")
    obj.Delete()  # This deletes the line object
    print("Line deleted.")
    break  # Stop after deleting the first line (you can remove this to delete all lines)

# Iterate over all circles in the drawing and delete the first circle found
for obj in acad.iter_objects("AcDbCircle"):
    print(f"Deleting circle with center: {obj.Center}, radius: {obj.Radius}")
    obj.Delete()  # This deletes the circle object
    print("Circle deleted.")
    break  # Stop after deleting the first circle (you can remove this to delete all circles)

# Save the modified drawing
acad.app.ActiveDocument.SaveAs("C:/Users/Atakan EKŞİ/Documents/autocad/Drawing8.dwg")
print("Drawing has been modified and saved as 'drawing_with_deleted_object.dwg'")

# Optional: Close the drawing after saving
acad.app.ActiveDocument.Close()
