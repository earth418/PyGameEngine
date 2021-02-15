import OpenGL
import math, time
# import noise
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Math.vector import Vec2, Vec3
from Math.color import Color
from Objects.mesh import Mesh

def triangle_from_points(p1 : Vec2, p2 : Vec2, p3 : Vec2):

    glBegin(GL_TRIANGLES)

    glVertex3f(p1.X, p1.Y, 0.0)
    glVertex3f(p2.X, p2.Y, 0.0)
    glVertex3f(p3.X, p3.Y, 0.0)

    glEnd()

def square_from_points(corner1 : Vec2, corner2 : Vec2):
    glBegin(GL_QUADS)

    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)

    glEnd()

def showScreen():
    c = time.time()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # triangle_from_points()

    glutSwapBuffers()

    if c != time.time():
        print(f'FPS: {int(1/(time.time() - c))}')
    c = time.time()

def generate_plane():
    triangle_size = 10
    plane_size = 30
    for i in range(plane_size):
        for j in range(plane_size):
            glColor3f(noise.snoise3(i / plane_size, j / plane_size, time.time() / 10000), noise.snoise3(i / plane_size, j / plane_size, time.time() / 10000), noise.snoise3(i / plane_size, j / plane_size, time.time() / 100))
            # glColor3f(i / plane_size, j / plane_size, (j + i) / (2 * plane_size))
            triangle_from_points(Point(i, j) * triangle_size, Point(i, j + 1) * triangle_size, Point(i + 1, j + 1) * triangle_size)
            triangle_from_points(Point(i, j) * triangle_size, Point(i + 1, j) * triangle_size, Point(i + 1, j + 1) * triangle_size)

def iterate():
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0,0)
window = glutCreateWindow("OpenGL Testing")

# gluPerspective(90, 16/9, 0.0, 1.0)

# glTranslatef(0.0, 0.0, -5)

glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()