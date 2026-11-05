import sys
import os
import numpy as np
import ctypes
from ctypes import c_float

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# We need to inspect the Drone class without running the full sim
# We will mock the pyglet parts that crash to see what data is generated

import pyglet
from unittest.mock import MagicMock, patch

# Mock pyglet.gl to prevent crashes during import/inspection
mock_gl = MagicMock()
mock_gl.GLfloat = c_float  # This might fail if c_float isn't imported, let's import ctypes
import ctypes
c_float = ctypes.c_float

# Better approach: Just look at the source code for vertex generation
# and the specific line that fails.

print("Checking source for vertex generation logic...")
with open('/config/byron/projects/drone_sim/src/drone.py', 'r') as f:
    content = f.read()
    # Find where vertices are created
    if 'vertices' in content:
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'vertices' in line.lower() and ('append' in line.lower() or 'array' in line.lower() or 'np.' in line.lower()):
                print(f"Line {i}: {line}")
                # Print context
                for j in range(max(0, i-2), min(len(lines), i+3)):
                    if j != i:
                        print(f"  {j}: {lines[j]}")
                print("---")
