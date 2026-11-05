import sys
import os
import time

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from MiniGL import MiniGL
from Renderer_fixed import Renderer
from drone import Drone

def main():
    print("Initializing simulation...")
    
    # Initialize MiniGL
    miniGL = MiniGL()
    miniGL.init()
    
    # Create Renderer
    config = {'width': 800, 'height': 600}
    renderer = Renderer(miniGL, config)
    
    # Create Drone
    drone = Drone()
    
    print("Starting loop")
    
    # Run the simulation loop using pyglet's event loop
    # We need to hook into pyglet's draw event
    last_time = [time.time()]

    def update(dt):
        thrust = (0, 0, 0)
        if drone.z <= -10.0:
            drone.z = -10.0
            drone.vz = 0
        drone.update(dt, thrust)
        print(f"pos: {drone.x:.3f}, {drone.y:.3f}, {drone.z:.3f}")

    @miniGL.window.event
    def on_draw():
        now = time.time()
        dt = now - last_time[0]
        last_time[0] = now
        update(dt)
        renderer.clear()
        renderer.draw(drone)
        renderer.present()
    
    # Change drone color to red on start to verify edit
    drone.color = (1.0, 0.0, 0.0)
    print(f"Drone color set to: {drone.color}")
    
    # Start the loop
    miniGL.loop(None)

if __name__ == '__main__':
    main()
