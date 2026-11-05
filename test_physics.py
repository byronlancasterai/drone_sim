import sys
sys.path.insert(0, 'src')
from drone import Drone

d = Drone()
print(f'Start: {d.x:.3f}, {d.y:.3f}, {d.z:.5f}')

# Thrust right and up
for i in range(10):
    d.update(0.1, (2, 0, 9.8))
    print(f'T={i*0.1+0.1:.1f}s: x={d.x:.3f}, y={d.y:.3f}, z={d.z:.5f}')
