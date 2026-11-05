import sys
sys.path.insert(0, 'src')
from drone import Drone

d = Drone()
d.drag_coeff = 0.1
d.vx = 1.0

print(f"Start: vx={d.vx:.3f}")
for i in range(10):
    d.update(0.1, (0, 0, 9.81))
    print(f"T={0.1*(i+1):.1f}s: x={d.x:.3f}, vx={d.vx:.3f}")
