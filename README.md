# drone_sim

A 3D drone simulation using pyglet.

## Structure
- `sim_loop_fixed.py`: Main entry point. Uses corrected vertex handling.
- `sim_loop.py`: Original version, kept for reference.
- `src/`: Source code.
  - `physics.py`: Physics engine (gravity, thrust clamping, drag).
  - `drone.py`: Drone entity logic.
  - `MiniGL.py`: Minimal OpenGL wrapper.
  - `Renderer_fixed.py`: Rendering logic.
  - `Viewport.py`: Viewport management.
  - `generate_mesh.py`: Mesh generation utility.
  - `debug_mesh.py`: Debugging tool for meshes.
- `tests/`: Unit tests for physics and viewport.
- `archive/`: Older, unused code.
- `data/`: Simulation data logs.

## Running
```bash
python3 sim_loop_fixed.py
```

## Notes
- `sim_loop_fixed.py` fixes a `VertexDomain.create()` bug present in `sim_loop.py`.
- `physics.py` includes thrust max clamping.
- The project relies on `pyglet` for rendering and `numpy` for math.
