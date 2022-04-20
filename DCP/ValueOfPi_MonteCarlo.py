# # comments
# Monte Carlo estimation 
# Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. One of the basic examples of getting started with the Monte Carlo algorithm is the estimation of Pi. 
# Estimation of Pi 
# The idea is to simulate random (x, y) points in a 2-D plane with domain as a square of side 1 unit. Imagine a circle inside the same domain with same diameter and inscribed into the square. We then calculate the ratio of number points that lied inside the circle and total number of generated points. Refer to the image below:
# # End
import random
circle_points = 0
square_points = 0
interval = 1000
pi = 0
for i in range(interval**2):
    rand_x = random.uniform(-1,1)
    rand_y = random.uniform(-1,1)
    origin_distance = rand_x ** 2 + rand_y**2
    if(origin_distance <= 1):
        circle_points += 1
    square_points+=1
    pi = 4* circle_points/square_points
print("Final Estimation of Pi=", pi)    