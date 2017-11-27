# Compute the volume fo a Cylinder

radius,length = input("Enter the radius and length of a cylinder: ").split(",")

pi = 3.142
area = int(radius) * int(radius) * pi
volume = int(area) * int(length)

print ("The area is ", area , "The volume is ", volume)



