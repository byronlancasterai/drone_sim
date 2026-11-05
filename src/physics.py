#!/usr/bin/env python3
"""Drone physics model."""
import math

GRAVITY = 9.81

class Drone:
    def __init__(self, x=0.0, y=0.0, z=0.0, vx=0.0, vy=0.0, vz=0.0, mass=1.0, thrust_max=10.0):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.mass = mass
        self.thrust_max = thrust_max
        self.rotation = 0.0
        self.wx = 0.0
        self.wy = 0.0
        self.wz = 0.0

    @property
    def pos(self):
        return (self.x, self.y, self.z)

    @property
    def vel(self):
        return (self.vx, self.vy, self.vz)

    def step(self, dt, thrust_vec, torque=None):
        # Calculate acceleration: F = ma -> a = F/m
        fx, fy, fz = thrust_vec
        # Clamp thrust to maximum allowed
        fx = max(-self.thrust_max, min(self.thrust_max, fx))
        fy = max(-self.thrust_max, min(self.thrust_max, fy))
        fz = max(-self.thrust_max, min(self.thrust_max, fz))
        # Add gravity (acting in negative z direction)
        fz -= self.mass * GRAVITY
        
        ax = fx / self.mass
        ay = fy / self.mass
        az = fz / self.mass

        self.vx += ax * dt
        self.vy += ay * dt
        self.vz += az * dt

        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt

        # Torque and angular velocity update
        if torque is not None:
            tx, ty, tz = torque
            # Simple rotational inertia assumption (I=1 for now)
            self.wx += tx * dt
            self.wy += ty * dt
            self.wz += tz * dt

        self.rotation += self.wz * dt  # Update yaw rotation
        # Keep rotation within 0-2π range
        if self.rotation > 2 * math.pi:
            self.rotation -= 2 * math.pi
        elif self.rotation < 0:
            self.rotation += 2 * math.pi

    def update(self, thrust_vec, dt, torque=None):
        self.step(dt, thrust_vec, torque)
