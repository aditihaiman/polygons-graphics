from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     
        sphere: add a sphere to the edge matrix -
                takes 5 arguemnts (cx, cy, cz, r, step)
        torus: add a torus to the edge matrix -
               takes 5 arguemnts (cx, cy, cz, r1, r2)
        box: add a rectangular prism to the edge matrix -
             takes 6 arguemnts (x, y, z, width, height, depth)
             
             
        circle: add a circle to the edge matrix -
                takes 4 arguments (cx, cy, cz, r)
        hermite: add a hermite curve to the edge matrix -
                 takes 8 arguments (x0, y0, x1, y1, rx0, ry0, rx1, ry1)
        bezier: add a bezier curve to the edge matrix -
                takes 8 arguments (x0, y0, x1, y1, x2, y2, x3, y3)
     
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, pofloats, transform, screen, color ):
    f = open(fname, 'r')
    file = f.read()
    lines = file.split("\n")
    x = 0
    while(x < len(lines)):
        line = lines[x].split(" ")
        line2 = []
        if(x+1 < len(lines)): line2 = lines[x+1].split(" ")
        
        if(line[0] == 'line'):
            add_edge(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), float(line2[4]), float(line2[5]))
        
        elif(line[0] == 'ident'):
            ident(transform)
        
        elif(line[0] == 'scale'):
            matrix_mult(make_scale(float(line2[0]), float(line2[1]), float(line2[2])), transform)
        
        elif(line[0] == 'move'):
            matrix_mult(make_translate(float(line2[0]), float(line2[1]), float(line2[2])), transform)
        
        elif(line[0] == 'rotate'):
            matrix_mult(make_rot(line2[0], float(line2[1])), transform)
        
        elif(line[0] == 'apply'):
            matrix_mult(transform, pofloats)
            
        elif(line[0] == 'box'):
            add_box(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), float(line2[4]), float(line2[5]))
        
        elif(line[0] == 'sphere'):
            add_sphere(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), STEP)
            
        elif(line[0] == 'torus'):
            add_torus(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), float(line2[4]), STEP)
            
        elif(line[0] == 'bezier'):
            add_curve(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), float(line2[4]), float(line2[5]), float(line2[6]), float(line2[7]), STEP, 1)
            
        elif(line[0] == 'hermite'):
            add_curve(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), float(line2[4]), float(line2[5]), float(line2[6]), float(line2[7]), STEP, 0)
        
        elif(line[0] == 'circle'):
            add_circle(pofloats, float(line2[0]), float(line2[1]), float(line2[2]), float(line2[3]), STEP)

        elif(line[0] == 'clear'):
            pofloats = []
        
        elif(line[0] == 'display'):
            clear_screen(screen)
            draw_lines(pofloats, screen, color)
            display(screen)
        
        elif(line[0] == 'save'):
            clear_screen(screen)
            draw_lines(pofloats, screen, color)
            save_extension(screen, line2[0])
        
        x = x + 1
