import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math


def init():
    glClearColor(0.24, 0.69, 0.17,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def creeper():

     glClear(GL_COLOR_BUFFER_BIT)

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



initSkala = 0.0  #membuat animasi memperbesar ukuran
def animSkala ():
    global initSkala
    glPushMatrix()
    glScalef(initSkala,initSkala,0)
    creeper()
    initSkala = initSkala +0.25 #menentukan perubahan ukuran
    glPopMatrix()
    glFlush()

def Timer():
    glutPostRedisplay()
    glutTimerFunc(10,Timer,5)
    glFlush()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    animSkala()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(10,10)
    glutCreateWindow("OpenGL rumah")
    glutDisplayFunc(render)
    glutTimerFunc(10,Timer,5)
    init()
    glutMainLoop()

main()
