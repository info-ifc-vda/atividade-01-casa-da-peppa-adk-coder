import glfw
from OpenGL.GL import *

def desenha_triangulo():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_TRIANGLES)
    
    glColor3f(0.2, 0.6, 1.0)
    
    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)

    glEnd()

def main():
    if not glfw.init():
        return
        
    janela = glfw.create_window(640, 480, "Meu Primeiro Triangulo OpenGL", None, None)
    
    if not janela:
        glfw.terminate()
        return
        
    glfw.make_context_current(janela) 
    
    glClearColor(0.15, 0.15, 0.15, 1.0)
    
    while not glfw.window_should_close(janela): 
        glfw.poll_events() 
        
        desenha_triangulo()
        
        glfw.swap_buffers(janela)
        
    glfw.terminate()
    
if __name__ == "__main__":
    main()
