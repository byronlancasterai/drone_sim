import pyglet
from pyglet import shapes

class Viewport:
    def __init__(self, miniGL, config=None):
        config = config or {}
        self.miniGL = miniGL
        self.config = config or {}
        self.width = config.get('width', 800)
        self.height = config.get('height', 600)
        self.batch = pyglet.graphics.Batch()
        self.shapes = []
        self.color = (255, 255, 255)

    def resize(self):
        pass

    def update(self):
        pass

    def set_color(self, r, g, b, a=1.0):
        self.color = (int(r*255), int(g*255), int(b*255), int(a*255))

    def draw(self, vertices=None, indices=None, color=None):
        if vertices is None:
            return
        try:
            use_color = self.color if color is None else color
            scale = 100
            offset_x = self.width // 2
            offset_y = self.height // 2

            if indices is None:
                # Draw individual vertices as small circles
                for v in vertices:
                    x = offset_x + v[0] * scale
                    y = offset_y + v[1] * scale
                    c = shapes.Circle(x, y, 2, color=use_color, batch=self.batch)
                    self.shapes.append(c)
                return

            # Draw edges from indices
            for i1, i2 in indices:
                if i1 >= len(vertices) or i2 >= len(vertices):
                    continue
                v1 = vertices[i1]
                v2 = vertices[i2]
                # Simple projection: ignore z, just x,y
                x1 = offset_x + v1[0] * scale
                y1 = offset_y + v1[1] * scale
                x2 = offset_x + v2[0] * scale
                y2 = offset_y + v2[1] * scale

                line = shapes.Line(x1, y1, x2, y2, color=use_color, batch=self.batch)
                self.shapes.append(line)

        except Exception as e:
            print(f"Viewport draw error: {e}")

    def clear(self):
        self.batch = pyglet.graphics.Batch()
        self.shapes = []

    def present(self):
        self.batch.draw()
