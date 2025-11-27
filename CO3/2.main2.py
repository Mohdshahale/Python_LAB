from graphics.rectangle import area as rect_area,perimeter as rect_peri
from graphics.circle import area as circ_area,perimeter as circ_peri
from graphics.threeDgraphics.cuboid import area as cub_area
from graphics.threeDgraphics.sphere import perimeter as sph_peri

print("Rectangle Area: ",rect_area(8,4))
print("Rectangle Perimeter: ",rect_peri(8,4))

print("Circle Area: ",circ_area(6))
print("Circle Perimeter: ",circ_peri(7))

print("Cuboid Area: ",cub_area(6,4,2))
#print("Cuboid Perimeter: ",cuboid.perimeter(10,5,4))

#print("Sphere Area: ",sphere.area(7))
print("Sphere Perimeter: ",sph_peri(5))
