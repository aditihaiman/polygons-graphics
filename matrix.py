"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math


def make_bezier():
    return [[-1.0, 3.0, -3.0, 1.0],[3.0, -6.0, 3.0, 0.0],[-3.0, 3.0, 0.0, 0.0],[1.0, 0.0, 0.0, 0.0]]

def make_hermite():
    return [[2.0, -3.0, 0.0, 1.0],[-2.0, 3.0, 0.0, 0.0],[1.0, -2.0, 1.0, 0.0],[1.0, -1.0, 0.0, 0.0]]

def generate_curve_coefs( p0, p1, p2, p3, t ): #0 = hermite, 1 = bezier
    m = [[p0, p1, p2, p3]]
    if (t==0): matrix_mult(make_hermite(), m)
    if (t==1): matrix_mult(make_bezier(), m)
    return m



def make_translate( x, y, z ):
    return [[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[x, y, z, 1]]

def make_scale( x, y, z ):
    return [[x, 0, 0, 0],[0, y, 0, 0],[0, 0, z, 0],[0, 0, 0, 1]]

def make_rot(axis, theta):
    if(axis=='x'): return make_rotX(theta)
    elif(axis=='y'): return make_rotY(theta)
    else: return make_rotZ(theta)

def make_rotX( theta ):
    theta = theta * math.pi / 180.0
    return [[1, 0, 0, 0],
            [0, math.cos(theta), math.sin(theta), 0],
            [0, -1*math.sin(theta), math.cos(theta), 0],
            [0, 0, 0, 1]]

def make_rotY( theta ):
    theta = theta * math.pi / 180.0
    return [[math.cos(theta), 0, -1*math.sin(theta), 0],
            [0, 1, 0, 0],
            [math.sin(theta), 0, math.cos(theta), 0],
            [0, 0, 0, 1]]

def make_rotZ( theta ):
    theta = theta * math.pi / 180.0
    return [[math.cos(theta), math.sin(theta), 0, 0],
            [-1*math.sin(theta), math.cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for x in range(len(matrix[0])):
        line = ""
        for y in range(len(matrix)):
            if(matrix[y][x]//10 == 0): line += str(matrix[y][x]) + "   "
            elif(matrix[y][x]//10 < 10): line += str(matrix[y][x]) + "  "
            else: line += str(matrix[y][x]) + " "
        print(line)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] = 0
            if(x == y): matrix[x][y] = 1
            

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        tmp = row[:]
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def copy(m1, m2):
    for list in m1:
        l = []
        for x in list:
            l.append(x)
        m2.append(l)
