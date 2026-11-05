import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import os
import time
import threading

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from drone import Drone
from renderer import Renderer

def main():
    renderer = Renderer()
    drone = Drone()
    
    last_time = time.time()
    
    try:
        while True:
            now = time.time()
            delta = now - last_time
            last_time = now

            drone.update(delta)
            renderer.clear()
            renderer.draw(drone)
            renderer.present()
            time.sleep(0.016)
    except KeyboardInterrupt:
        print("Simulation ended.")

if __name__ == "__main__":
    main()
