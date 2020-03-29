import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot product of a . b
def dot_product(a, b):
    return 0

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    x0 = polygons[i][0]
    y0 = polygons[i][1]
    z0 = polygons[i][2]
    x1 = polygons[i+1][0]
    y1 = polygons[i+1][1]
    z1 = polygons[i+1][2]
    x2 = polygons[i+2][0]
    y2 = polygons[i+2][1]
    z2 = polygons[i+2][2]
    
    ax = x1 - x0
    ay = y1 - y0
    az = z1 - z0
    
    bx = x2 - x0
    by = y2 - y0
    bz = z2 - z0
    
    nx = ay*bz - az*by
    ny = az*bx - ax*bz
    nz = ax*by - ay*bx
    
    return [nx, ny, nz]
    
