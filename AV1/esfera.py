from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *


def esfera():
    glRotatef(1,1,0,0)
    glBegin(GL_POINTS)
    raio = 1
    n = 50
    for i in range(0,n):
        theta = (i*pi/n) - pi/2
        for j in range(0,n):
            phi = (j*2*pi)/n
            x = raio * cos(theta) * cos(phi)
            y = raio * sin(theta)
            z = raio * cos(theta) * sin(phi)
            glVertex3f(x,y,z)
    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    esfera()
