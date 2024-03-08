import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math


def init():
    glClearColor(0.24, 0.69, 0.17,1.0)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)

def drawRumah():

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
   
def render(): #digunakan untuk membuat transformasi 2D
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    drawRumah()
    glPushMatrix()
    glTranslate(2,2,0) #proses translasi (gambar menjadi dua)
    glRotate(0,0,0,-1) #proses rotasi (gambar menjadi miring)
    glScalef(0.5,0.5,0) #proses skala (diperkecil)
    drawRumah()
    glPopMatrix()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(10,10)
    glutCreateWindow("OpenGL rumah")
    glutDisplayFunc(render)
    init()
    glutMainLoop()

main()
