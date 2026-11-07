import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from physics import Drone
from pid import PID

def test_pid_altitude_hold():
    # Create drone with higher thrust max to allow PID to work effectively
    # mass=1.0, gravity=9.81, so hover thrust is 9.81. 
    # thrust_max=20.0 allows max net thrust of 10.19 N upwards.
    d = Drone(z=0.0, vz=0.0, thrust_max=20.0)
    target_z = 5.0
    dt = 0.01
    gravity_thrust = d.mass * 9.81
    
    # PID gains: Kp=2.0, Ki=0.1, Kd=1.0
    pid = PID(kp=2.0, ki=0.1, kd=1.0)
    
    stable_count = 0
    required_stable_steps = 50
    
    for i in range(1000):
        error = target_z - d.z
        pid_output = pid.update(error, dt)
        thrust_z = gravity_thrust + pid_output
        
        d.step(dt, (0, 0, thrust_z))
        
        # Check for stability: within 0.1m of target and vz < 0.1 m/s
        if abs(d.z - target_z) < 0.1 and abs(d.vz) < 0.1:
            stable_count += 1
        else:
            stable_count = 0
            
        if stable_count >= required_stable_steps:
            break
            
    # Assert that we reached stability
    assert stable_count >= required_stable_steps, f"Did not stabilize. Final z: {d.z}, vz: {d.vz}"
    
    # Print for visibility in test output
    print(f"Stabilized at t={i*dt:.2f}s, z={d.z:.3f}, vz={d.vz:.3f}")
