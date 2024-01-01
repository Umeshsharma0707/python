#Write a Python program to calculate surface volume and
# area of acylinder



def cylinder_surface_area(radius, height):
    area = 2 * 3.14 * radius**2 + 2 * 3.14 * radius * height
    return area

def cylinder_volume(radius, height):
    volume = 3.14 * radius**2 * height
    return volume

radius = 5
height = 10

surface_volume = cylinder_surface_area(radius,height)
c_volume = cylinder_volume(radius,height)

print(f"surface volume : {surface_volume}")
print(f"cylinder volume : {c_volume}")