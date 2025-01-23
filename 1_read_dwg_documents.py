from pyautocad import Autocad
import math

# Connect to AutoCAD
acad = Autocad(create_if_not_exists=True)

# Open an existing drawing
drawing_path = r"/Documents/autocad/Drawing6.dwg" #Your dwg address
acad.app.Documents.Open(drawing_path)

# Function to print detailed information for each object
def print_line_details(obj):
    print(f"Line: Start Point: {obj.StartPoint}, End Point: {obj.EndPoint}")
    print(f"Line Length: {obj.Length}")
    print(f"Layer: {obj.Layer}, Color: {obj.Color}")

def print_circle_details(obj):
    print(f"Circle: Center: {obj.Center}, Radius: {obj.Radius}")
    print(f"Circle Area: {math.pi * obj.Radius ** 2}")
    print(f"Layer: {obj.Layer}, Color: {obj.Color}")

def print_block_details(obj):
    print(f"Block: Name: {obj.Name}, Insertion Point: {obj.InsertionPoint}")
    print(f"Layer: {obj.Layer}, Color: {obj.Color}")

def print_arc_details(obj):
    print(f"Arc: Center: {obj.Center}, Radius: {obj.Radius}, Start Angle: {obj.StartAngle}, End Angle: {obj.EndAngle}")
    print(f"Layer: {obj.Layer}, Color: {obj.Color}")

def print_polyline_details(obj):
    print(f"Polyline: Number of Vertices: {obj.NumVertices}")
    vertices = [obj.GetPointAt(i) for i in range(obj.NumVertices)]
    print(f"Vertices: {vertices}")
    print(f"Layer: {obj.Layer}, Color: {obj.Color}")

def print_text_details(obj):
    print(f"Text: Value: {obj.TextString}, Position: {obj.InsertionPoint}")
    print(f"Height: {obj.Height}, Rotation: {obj.Rotation}")
    print(f"Layer: {obj.Layer}, Color: {obj.Color}")

# Iterate over all objects in the drawing and print their details
for obj in acad.iter_objects("AcDbLine"):
    print_line_details(obj)

for obj in acad.iter_objects("AcDbCircle"):
    print_circle_details(obj)

for obj in acad.iter_objects("AcDbBlockReference"):
    print_block_details(obj)

for obj in acad.iter_objects("AcDbArc"):
    print_arc_details(obj)

for obj in acad.iter_objects("AcDbPolyline"):
    print_polyline_details(obj)

for obj in acad.iter_objects("AcDbText"):
    print_text_details(obj)

# Closing the drawing (optional)
acad.app.ActiveDocument.Close()
print("Data from the drawing has been successfully read.")
