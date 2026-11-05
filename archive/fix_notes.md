# Pyglet VertexDomain Fix

## Problem
GL_INVALID_VALUE when creating VertexDomain with a Python list.

## Cause
VertexDomain requires a ctypes array, not a Python list.

## Solution
Convert the list to a ctypes array before passing to VertexDomain.

```python
import ctypes

vertices = [ ... ] # list of floats
VertexArrayType = ctypes.c_float * len(vertices)
vertices_ctypes = VertexArrayType(*vertices)

domain = VertexDomain({
    'vertex': {
        'data': vertices_ctypes,
        'format': 'f',
        'location': 0,
        'count': len(vertices),
        'instance': False
    }
})
```