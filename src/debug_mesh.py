import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from drone import Drone

d = Drone()
print(f"Mesh exists: {hasattr(d, 'mesh')}")
if hasattr(d, 'mesh'):
    print(f"Mesh type: {type(d.mesh)}")
    if d.mesh:
        print(f"Vertices: {d.mesh.vertices}")
        print(f"Indices: {d.mesh.indices}")
    else:
        print("Mesh is None")
else:
    print("No mesh attribute")