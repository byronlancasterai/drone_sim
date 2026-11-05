import math

class Drone:
    def __init__(self, x=0, y=0, z=0, vx=0, vy=0, vz=0):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.mass = 1.0
        self.drag_coeff = 0.1
        self.rotation = 0.0
        self.rotation_speed = 1.0
        
        # Create mesh
        vertices = [
            -0.5, -0.5, -0.5,
             0.5, -0.5, -0.5,
             0.5,  0.5, -0.5,
            -0.5,  0.5, -0.5,
            -0.5, -0.5,  0.5,
             0.5, -0.5,  0.5,
             0.5,  0.5,  0.5,
            -0.5,  0.5,  0.5,
        ]
        indices = [
            0, 1, 2, 0, 2, 3,
            4, 6, 5, 4, 7, 6,
            0, 4, 5, 0, 5, 1,
            2, 6, 7, 2, 7, 3,
            0, 3, 7, 0, 7, 4,
        ]
        import ctypes
        import pyglet
        from pyglet.graphics.vertexdomain import VertexDomain
        from pyglet.gl import GL_TRIANGLES
        
        # Convert Python list to ctypes array for VertexDomain compatibility
        VertexArrayType = ctypes.c_float * len(vertices)
        vertices_ctypes = VertexArrayType(*vertices)
        IndexType = ctypes.c_uint * len(indices)
        indices_ctypes = IndexType(*indices)
        
        domain = VertexDomain({'vertex': {'data': vertices_ctypes, 'format': 'f', 'location': 0, 'count': 3, 'instance': False}})
        self.mesh = domain.create(len(indices))

    def update(self, dt, thrust_vec=(0, 0, 0)):
        # Delegate to physics module for force integration
        from physics import Drone as PhysicsDrone
        # Apply drag before physics step
        self.vx *= (1.0 - self.drag_coeff * dt)
        self.vy *= (1.0 - self.drag_coeff * dt)
        self.vz *= (1.0 - self.drag_coeff * dt)
        # Use physics step for thrust and gravity
        temp = PhysicsDrone(x=self.x, y=self.y, z=self.z,
                           vx=self.vx, vy=self.vy, vz=self.vz,
                           mass=self.mass)
        temp.step(dt, thrust_vec)
        self.x, self.y, self.z = temp.x, temp.y, temp.z
        self.vx, self.vy, self.vz = temp.vx, temp.vy, temp.vz
        self.rotation += self.rotation_speed * dt
        self.rotation %= 2.0 * math.pi
