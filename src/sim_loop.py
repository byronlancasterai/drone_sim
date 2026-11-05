#!/usr/bin/env python3
"""Drone simulation loop."""

import time
import sys
sys.path.insert(0, 'byron/projects/drone_sim/src')
from drone import Drone

def main():
    drone = Drone()
    print("simulation started. Enter thrust (x,y,z) or quit.")
    while True:
        try:
            user_input = input("thrust: ").strip()
            if user_input.lower() == 'quit':
                break
            parts = user_input.split(',')
            if len(parts) != 3:
                print("format: x,y,z")
                continue
            thrust_vec = (float(parts[0]), float(parts[1]), float(parts[2]))
            drone.update(thrust_vec=thrust_vec, dt=0.1)
            print(f"pos: ({drone.x:.2f}, {drone.y:.2f}, {drone.z:.2f}) vel: ({drone.vx:.2f}, {drone.vy:.2f}, {drone.vz:.2f})")
        except EOFError:
            break
        except ValueError:
            print("invalid numbers")

if __name__ == "__main__":
    main()
