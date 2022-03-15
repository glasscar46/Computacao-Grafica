from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

global a
a = 0
n = 10
phi0 = 0
phin = 360
theta0 = -pi/2
thetan = pi/2

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1),
            (0.5, 1, 1), (1, 0, 0.5))
dphi = (phin-phi0)/n
dtheta = (thetan-theta0)/n

def esfera():
    glRotatef(1, 1, 0, 0)
    raio = 1
    phi = phi0
    for i in range(0, n):
        glBegin(GL_TRIANGLE_STRIP)
        theta = theta0
        glColor3fv(cores[i%8])
        for j in range(0, n+1):
            x = raio * cos(theta) * cos(phi)
            y = raio * sin(theta)
            z = raio * cos(theta) * sin(phi)
        
            x0 = raio * cos(theta) * cos(phi+dphi)
            y0 = raio * sin(theta)
            z0 = raio * cos(theta)* sin(phi+dphi)
            glVertex3f(x, y, z)
            glVertex3f(x0,y0,z0)
            theta += dtheta
        glEnd()
        phi += dphi
        # # theta = ((i * pi) / (n)) - pi / 2
        # # glColor3fv(cores[i % 8])
        # # for j in range(0, n):
        # #     phi = (j * 2 * pi) / n  # phi0
        # #     pontos = calculePonto(theta, phi)
        # #     print(pontos)
        # #     pontos2 = calculePonto(theta, phi + dt)
        # #     glVertex3f(pontos["x"], pontos["y"], pontos["z"])
        # #     glVertex3f(pontos2["x"], pontos2["y"], pontos2["z"])
        # #     print(pontos2)


def calculePonto(theta, phi):
    raio = 1
    x = raio * cos(theta) * cos(phi)
    y = raio * sin(theta)
    z = raio * cos(theta) * sin(phi)
    return {"x": x, "y": y, "z": z}


def desenha():
    global a
    a = 0
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    esfera()
    glutSwapBuffers()
    a = a + 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


def mouse(botao, estado, x, y):
    pass
    # print(botao, estado, x, y)


def mouseMove(x, y):
    pass
    # print("-->", x, y)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
# glutMotionFunc(mouseMove)
glutPassiveMotionFunc(mouseMove)
glutMouseFunc(mouse)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -5)
glutTimerFunc(50, timer, 1)
glutMainLoop()
