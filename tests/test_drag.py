import sys
import pytest

sys.path.insert(0, 'src')
from drone import Drone

def test_drag_decelerates():
    """Test that drag reduces velocity over time."""
    d = Drone()
    d.drag_coeff = 0.1
    d.vx = 1.0
    
    # Run simulation for 1 second (10 steps of 0.1s)
    for _ in range(10):
        d.update(0.1, (0, 0, 9.81))
        
    # Velocity should be lower than start but positive (drag opposes motion)
    assert 0 < d.vx < 1.0, f"Expected vx to decrease, got {d.vx}"

def test_drag_direction():
    """Test that drag opposes velocity direction."""
    d = Drone()
    d.drag_coeff = 0.1
    d.vx = -1.0
    
    for _ in range(10):
        d.update(0.1, (0, 0, 9.81))
        
    # Velocity should be higher (closer to 0) than start
    assert -1.0 < d.vx < 0, f"Expected vx to increase toward 0, got {d.vx}"
