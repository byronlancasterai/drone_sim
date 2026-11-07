import sys
sys.path.insert(0, 'src')
from drone import Drone
from Viewport import Viewport

d = Drone()
print('Drone pos:', d.x, d.y, d.z)
print('Has mesh:', hasattr(d, 'mesh'))

v = Viewport(None)
v.draw(d.mesh)
print('Shapes created:', len(v.shapes))

for s in v.shapes[:3]:
    print('Line:', s.x, s.y, s.x2, s.y2)
