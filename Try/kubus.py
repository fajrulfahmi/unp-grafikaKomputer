
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0.0
refers = 15

def lightt():
    light_position = [1, 0, 0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)

    glEnable(GL_LIGHT0)
    light_ambient = [1.0, 0.0, 0.0, 0.0]
    light_diffuse = [1.0, 0.0, 0.0, 0.0]
    light_specular = [1.0, 0.0, 0.0, 0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glShadeModel(GL_SMOOTH)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    #lightt()
   


def draw_cube():
    glBegin(GL_QUADS)
    #wajah
    glColor3f(0.0, 0.0, 0.0) 
    glVertex3f(0.2,0.2, 1.01)
    glVertex3f(0.2,0.6, 1.01) 
    glVertex3f(0.6,0.6, 1.01)
    glVertex3f(0.6,0.2, 1.01)

    glVertex3f(-0.2,0.2, 1.01)
    glVertex3f(-0.2,0.6, 1.01) 
    glVertex3f(-0.6,0.6, 1.01)
    glVertex3f(-0.6,0.2, 1.01)

    glVertex3f(-0.2,0.2, 1.01)
    glVertex3f(0.2,0.2, 1.01) 
    glVertex3f(0.2,-0.35, 1.01)
    glVertex3f(-0.2,-0.35, 1.01)

    glVertex3f(-0.2,0, 1.01)
    glVertex3f(-0.4,0, 1.01) 
    glVertex3f(-0.4,-0.55, 1.01)
    glVertex3f(-0.2,-0.55, 1.01)

    glVertex3f(0.2,0, 1.01)
    glVertex3f(0.4,0, 1.01) 
    glVertex3f(0.4,-0.55, 1.01)
    glVertex3f(0.2,-0.55, 1.01)

    #Kubus
    glColor3f(0.24, 0.69, 0.17) 
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0) 
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f (1.0, -1.0, -1.0)

    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0.0, -10)
    glRotatef(angle,0.5,5.0,0.0) 
    draw_cube()
    glutSwapBuffers()
    angle += 2.0


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(refers, timer, 0)


def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect, 1.0,100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("Kursi 3D")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glEnable(GL_DEPTH_TEST)
    init()
    #glClearColor(0.0, 0.0, 0.0, 1.0)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
