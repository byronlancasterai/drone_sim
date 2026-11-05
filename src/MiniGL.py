import pyglet
from pyglet.gl import *

import ctypes

class MiniGL:
    def __init__(self, config=None):
        self.window = pyglet.window.Window(
            width=800,
            height=600,
            caption="Drone Sim",
            resizable=True
        )
        self.window.on_draw = self.on_draw
        self.window.on_resize = self.on_resize
        self.viewport = None
        self.initialized = False

    def init(self):
        # OpenGL initialization must happen after context creation.
        # We do it here, but calls might still fail if context isn't current.
        # Safer to do in on_draw for first frame.
        from Viewport import Viewport
        self.viewport = Viewport(self)
        self.initialized = True

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        return True

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glLoadIdentity() removed: Pyglet 2.x does not support legacy OpenGL 1.1
        # Placeholder draw
        pass

    def present(self):
        self.window.flip()

    def loop(self, callback):
        pyglet.app.run()
