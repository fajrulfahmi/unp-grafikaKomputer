from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
    
def init():
    glClearColor(1.5,1.0,1.0,1.0)
    gluOrtho2D(0.0,1.0, 0.0,1.0)

def gambar():
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(0.24, 0.69, 0.17)

     glBegin(GL_QUAD_STRIP)
     glVertex2f(1,1)
     glVertex2f(-1,1)
     glVertex2f(1,-1)
     glVertex2f(-1,-1)
     glEnd()

     glColor3f(0.0, 0.0, 0.0)
     glBegin(GL_QUAD_STRIP)
     glVertex2f(0.2,0.2)
     glVertex2f(0.2,0.6)
     glVertex2f(0.6,0.2)
     glVertex2f(0.6,0.6)
     glEnd()

     glBegin(GL_QUAD_STRIP)
     glVertex2f(-0.2,0.2)
     glVertex2f(-0.2,0.6)
     glVertex2f(-0.6,0.2)
     glVertex2f(-0.6,0.6)
     glEnd()

     glBegin(GL_QUAD_STRIP)
     glVertex2f(-0.2,0.2)
     glVertex2f(0.2,0.2)
     glVertex2f(-0.2,-0.35) 
     glVertex2f(0.2,-0.35)
     glEnd()

     glBegin(GL_QUAD_STRIP)
     glVertex2f(-0.2,0)
     glVertex2f(-0.4,0)
     glVertex2f(-0.2,-0.55)
     glVertex2f(-0.4,-0.55) 
     glEnd()

     glBegin(GL_QUAD_STRIP)
     glVertex2f(0.2,0)
     glVertex2f(0.4,0)
     glVertex2f(0.2,-0.55)
     glVertex2f(0.4,-0.55) 
     glEnd()

     glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(800,100)
    glutCreateWindow("Creeper")
    glutDisplayFunc(gambar)
    glutMainLoop()

main()