import geometry

line = input("Enter")

(a,b,c)= (float(x) for x in line.split(","))

P = geometry.triangle_perimeter(a,b,c)
A = geometry.triangle_heronsarea(a,b,c)

print ("Perimeter")