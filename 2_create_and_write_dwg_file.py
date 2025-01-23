from pyautocad import Autocad, APoint
import math

# Connect to AutoCAD
acad = Autocad(create_if_not_exists=True)

# Create a new drawing
acad.app.Documents.Add()

# Start point for adding objects
origin = APoint(0, 0)

# 1. Add a Line
start_point = APoint(0, 0)
end_point = APoint(10, 0)  # Horizontal line of length 10
acad.model.AddLine(start_point, end_point)
print("Line added from (0,0) to (10,0)")

# 2. Add a Circle
center_point = APoint(5, 5)  # Circle center
radius = 3  # Radius
acad.model.AddCircle(center_point, radius)
print(f"Circle added with center at {center_point} and radius {radius}")

# 3. Add a Polygon (Hexagon)
polygon_center = APoint(0, -5)
polygon_sides = 6  # Hexagon (6 sides)
polygon_radius = 4
angle = 360 / polygon_sides  # Angle between each side

# Drawing the polygon
points = []
for i in range(polygon_sides):
    x = polygon_center.x + polygon_radius * math.cos(math.radians(i * angle))
    y = polygon_center.y + polygon_radius * math.sin(math.radians(i * angle))
    points.append(APoint(x, y))

# Drawing the polygon edges
for i in range(polygon_sides):
    start = points[i]
    end = points[(i + 1) % polygon_sides]
    acad.model.AddLine(start, end)
print(f"Polygon (Hexagon) added with center at {polygon_center}, radius {polygon_radius}")

# 4. Add Text
text_point = APoint(10, 10)
acad.model.AddText("Hello AutoCAD!", text_point, 1)
print(f"Text 'Hello AutoCAD!' added at {text_point}")


# 5. Add an Arrow
arrow_start = APoint(10, -5)
arrow_end = APoint(15, -5)
acad.model.AddLine(arrow_start, arrow_end)

# Drawing the arrowhead
acad.model.AddLine(arrow_end, APoint(14.5, -4.5))
acad.model.AddLine(arrow_end, APoint(14.5, -5.5))

print("Arrow added with a line from (10,-5) to (15,-5) and an arrowhead")

# 6. Add an Arc (Circular arc)
arc_center = APoint(10, -15)
arc_radius = 5
start_angle = 0
end_angle = 180
acad.model.AddArc(arc_center, arc_radius, math.radians(start_angle), math.radians(end_angle))
print("Arc added with center at (10,-15), radius 5, from angle 0 to 180 degrees")

# Save the drawing
acad.app.ActiveDocument.SaveAs("C:Documents/autocad/Drawing6.dwg") #Enter the name and location you want to save.
print("Drawing has been saved as 'complex_drawing.dwg'")
