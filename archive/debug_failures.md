# GL_INVALID_VALUE Failure Analysis

## Symptoms
- `pyglet.gl.lib.GLException: (0x1281): Invalid value.`
- Occurs in `VertexDomain.__init__` at `attribute.set_pointer(buffer.ptr)`.
- Occurs before `main()` loop starts.

## Verified Data
- `vertices` list: 24 floats.
- `vertices_ctypes`: `ctypes` array of 24 `c_float`.
- `len(vertices_ctypes)`: 24.
- Format string: `'f'` (matches `GL_FLOAT`).
- Location: 0.
- Count: 24.

## Hypothesis
1. The buffer pointer is invalid or not aligned correctly for OpenGL.
2. `VertexDomain` expects a different format string or stride.
3. The context is not fully initialized when `VertexDomain` is created.

## Next Steps
- Check if `pyglet.window.Window` must exist before creating `VertexDomain`.
- Verify `ctypes` array alignment.