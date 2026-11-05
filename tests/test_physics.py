#!/usr/bin/env python3
"""Basic physics tests for drone_sim."""
import sys
import os

# Add src to path to import physics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from physics import Drone

def test_gravity():
    d = Drone(mass=1.0)
    dt = 0.1
    # No thrust, should fall at 9.81 m/s^2
    d.update((0, 0, 0), dt)
    expected_vz = -9.81 * dt
    if abs(d.vz - expected_vz) > 1e-6:
        print(f"FAIL: Expected vz={expected_vz}, got {d.vz}")
        return False
    print(f"PASS: Gravity check. vz={d.vz}")
    return True

def test_thrust_clamping():
    d = Drone(mass=1.0)
    d.thrust_max = 10.0
    dt = 0.1
    # Thrust larger than max should clamp to 10, giving az=(10-9.81)/1=0.19
    d.update((0, 0, 100), dt)
    expected_vz = 0.19 * dt
    if abs(d.vz - expected_vz) > 1e-6:
        print(f"FAIL: Expected clamped vz={expected_vz}, got {d.vz}")
        return False
    print(f"PASS: Thrust clamp check. vz={d.vz}")
    return True

if __name__ == '__main__':
    test_gravity()
    test_thrust_clamping()
