import numpy as np
import struct

def generate_cube_mesh(filename):
    # Simple cube: 8 vertices, 36 indices (12 triangles)
    # Vertices: x, y, z
    vertices = np.array([
        # Front face
        -0.5, -0.5,  0.5,
         0.5, -0.5,  0.5,
         0.5,  0.5,  0.5,
        -0.5,  0.5,  0.5,
        # Back face
        -0.5, -0.5, -0.5,
         0.5, -0.5, -0.5,
         0.5,  0.5, -0.5,
        -0.5,  0.5, -0.5
    ], dtype=np.float32)

    # Indices for 12 triangles (2 triangles per face * 6 faces)
    indices = np.array([
        0, 1, 2,  0, 2, 3,  # Front
        4, 6, 5,  4, 7, 6,  # Back
        0, 5, 1,  0, 4, 5,  # Bottom
        3, 7, 2,  3, 6, 7,  # Top
        0, 3, 4,  4, 3, 7,  # Left
        1, 5, 2,  2, 5, 6   # Right
    ], dtype=np.uint32)

    with open(filename, 'wb') as f:
        # Write vertex count
        f.write(struct.pack('I', len(vertices) // 3))
        # Write vertices
        f.write(vertices.tobytes())
        # Write index count
        f.write(struct.pack('I', len(indices)))
        # Write indices
        f.write(indices.tobytes())

if __name__ == '__main__':
    generate_mesh('/config/byron/projects/drone_sim/data/drone_mesh.dat')
    print("Mesh generated.")
