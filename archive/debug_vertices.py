import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from drone import Drone

d = Drone()
print(f"Vertices type: {type(d.vertices)}")
print(f"Vertices length: {len(d.vertices)}")
print(f"First 10 values: {d.vertices[:10]}")
