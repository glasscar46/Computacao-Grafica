import sdl2
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

def circle():
    glPushMatrix()
    glTranslatef(1,0,0)
    glBegin(GL_POINTS)
    raio = 0.5
    n = 50
    for i in range(0,n):
        theta = i*(2*pi)/(n)
        for j in range(0,n):
            phi = (j*2*pi)/n
            x = raio * cos(theta)
            y = raio * sin(theta)
            z = 0
            glVertex3f(x,y,z)
    glEnd()
    glPopMatrix()
    
def doughnut():
    glRotatef(10,1,0,0)
    glPushMatrix()
    n = 100
    for i in range(0,n):
        glPushMatrix()
        theta = i*(360)/(n)
        glRotatef(theta,0,1,0)
        circle()
        glPopMatrix()  
    glPopMatrix()  
    
def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    doughnut()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Cubo", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
print(glGetString(GL_VERSION))
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-5)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
        if (event.type == sdl2.SDL_MOUSEMOTION):
            print("SDL_MOUSEMOTION")
        if (event.type == sdl2.SDL_MOUSEBUTTONDOWN):
            print("SDL_MOUSEBUTTONDOWN")
    desenha()
    sdl2.SDL_GL_SwapWindow(window)
    sdl2.SDL_Delay(50)