import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from MiniGL import MiniGL

class Renderer:
    def __init__(self, miniGL, config=None):
        self.miniGL = miniGL
        self.config = config if config else {}
        self.width = self.config.get('width', 800)
        self.height = self.config.get('height', 600)
        self.viewport = miniGL.viewport

    def clear(self):
        print("Renderer: clear called")
        if self.viewport:
            self.viewport.clear()

    def draw(self, drone):
        print(f"Renderer: draw called for drone {id(drone)}")
        if self.viewport:
            # Set up a simple wireframe draw
            self.viewport.set_color(0.0, 1.0, 0.0, 1.0) # Green wireframe
            
            # Draw the drone mesh
            # Assuming drone has a mesh attribute with vertices and indices
            if hasattr(drone, 'mesh') and drone.mesh:
                # Extract raw vertices from VertexList
                try:
                    buf = drone.mesh.domain.attrib_name_buffers['vertex']
                    # buf.data is c_float_Array_96 (96 floats = 32 vec3s)
                    raw_data = buf.data
                    # Convert to list of (x, y, z) tuples
                    vertices = [(raw_data[i], raw_data[i+1], raw_data[i+2]) for i in range(0, len(raw_data), 3)]
                    self.viewport.draw(vertices=vertices)
                except Exception as e:
                    print(f"Renderer: mesh extraction error: {e}")
            else:
                print("Renderer: no mesh found on drone")
            
            # Draw rotation indicator (a line from origin to rotated vector)
            import math
            angle = getattr(drone, 'rotation', 0.0)
            # Simple 2D projection for visualization
            line_x = math.cos(angle) * 0.8
            line_y = math.sin(angle) * 0.8
            # Assuming viewport has a draw_line method or similar; if not, this is a placeholder logic
            # For now, just print to verify rotation is accessible in render loop
            print(f"Renderer: Drone rotation={angle:.2f} rad")

    def present(self):
        print("Renderer: present called")
        if self.viewport:
            self.viewport.present()