from pyautocad import Autocad, APoint

# Connect to AutoCAD
acad = Autocad(create_if_not_exists=True)

# Open an existing drawing
drawing_path = r"/Documents/autocad/Drawing6.dwg"
acad.app.Documents.Open(drawing_path)

# Iterate over all lines in the drawing and modify them
for obj in acad.iter_objects("AcDbLine"):
    # Reading line properties
    start_point = APoint(obj.StartPoint[0], obj.StartPoint[1])
    end_point = APoint(obj.EndPoint[0], obj.EndPoint[1])
    print(f"Line: Start Point: {start_point}, End Point: {end_point}")
    
    # Example modification: Move the line by (5, 5)
    new_start = APoint(start_point.x + 5, start_point.y + 5)
    new_end = APoint(end_point.x + 5, end_point.y + 5)
    
    # Modify the line by updating the start and end points
    obj.StartPoint = new_start
    obj.EndPoint = new_end
    print(f"Line moved to new Start Point: {new_start}, End Point: {new_end}")

# Iterate over all circles in the drawing and modify them
for obj in acad.iter_objects("AcDbCircle"):
    # Reading circle properties
    center = APoint(obj.Center[0], obj.Center[1])
    radius = obj.Radius
    print(f"Circle: Center: {center}, Radius: {radius}")
    
    # Example modification: Change the color of the circle (to Red)
    obj.Color = 1  # 1 represents Red in AutoCAD
    
    # Example modification: Increase the radius by 2 units
    obj.Radius = radius + 2
    print(f"Circle modified: New Radius: {obj.Radius}, New Color: Red")

# Save the modified drawing
acad.app.ActiveDocument.SaveAs("C:/Users/Atakan EKŞİ/Documents/autocad/Drawing7.dwg")
print("Drawing has been modified and saved as 'modified_drawing.dwg'")

# Optional: Close the drawing after saving
acad.app.ActiveDocument.Close()
