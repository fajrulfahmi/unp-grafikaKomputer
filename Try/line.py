import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL. GLUT import*
import sys
import math

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0.0,500.0, 0.0,500.0)

def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(70,110)
    glVertex2i(70,250)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(18,18)
    glutCreateWindow("Moon")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()

main()