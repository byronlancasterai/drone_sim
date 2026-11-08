#!/usr/bin/env python3
"""Additional physics tests for drone_sim."""
import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from physics import Drone

def test_multi_step_fall():
    d = Drone(mass=1.0)
    dt = 0.1
    for _ in range(10):
        d.update((0, 0, 0), dt)
    # After 1 second of free fall, vz should be ~-9.81
    assert abs(d.vz - (-9.81 * 10 * dt)) < 1e-4

def test_drag_decelerates():
    d = Drone(mass=1.0, drag=0.5)
    d.vx = 10.0
    dt = 0.1
    d.update((0, 0, 9.81), dt)  # hover, only drag affects x
    # vx after 0.1s: 10.0 * (1 - 0.5*0.1) = 9.5
    assert abs(d.vx - 9.5) < 1e-6

def test_torque_rotates():
    d = Drone(mass=1.0)
    dt = 0.1
    d.update((0, 0, 9.81), dt, torque=(0, 0, 2.0))
    assert abs(d.wz - 2.0 * dt) < 1e-6
    assert abs(d.rotation - 2.0 * dt * dt) < 1e-6

def test_rotation_wraps():
    d = Drone(mass=1.0)
    d.rotation = 6.0  # close to 2*pi
    dt = 0.1
    d.update((0, 0, 9.81), dt, torque=(0, 0, 20.0))
    # wz = 20*0.1 = 2.0, rotation += 2.0, total ~8.0, should wrap
    assert 0 <= d.rotation < 2 * math.pi

def test_position_tracks_velocity():
    d = Drone(mass=1.0, vx=5.0)
    dt = 0.1
    d.update((0, 0, 9.81), dt)
    assert abs(d.x - 0.5) < 1e-6

def test_mass_scaling():
    d = Drone(mass=2.0)
    dt = 0.1
    d.update((0, 0, 0), dt)
    # gravity accel is independent of mass
    assert abs(d.vz - (-9.81 * dt)) < 1e-6

if __name__ == '__main__':
    test_multi_step_fall()
    test_drag_decelerates()
    test_torque_rotates()
    test_rotation_wraps()
    test_position_tracks_velocity()
    test_mass_scaling()
