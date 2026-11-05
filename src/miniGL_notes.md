# MiniGL Source Analysis

## Files Downloaded
- `MiniGL_src.ts`: Main entry point (re-exports).
- `View_Canvas.ts`: Canvas implementation. Handles transforms and uniform updates.
- `Mesh_src.ts`: Mesh rendering. Uses `gl.drawElements`. Supports wireframe.

## Key Observations
- Mesh extends Base.
- Uses custom shaders from `../Shaders/mesh.js`.
- `setData` and `setBufferDatas` handle vertex/attribute buffer upload.
- `setIndices` handles index buffer and wireframe conversion.
- Render loop binds buffers and calls `drawElements`.

## Canvas (View_Canvas.ts)
- `Canvas.update()` uses `requestAnimationFrame` and computes `delta` from `Date.now()`.
- `Canvas.add()` pushes a mesh, calls `mesh.onAdd`, sets `mesh.parent`, and returns the mesh.
- `Canvas.render()` clears depth, disables `DEPTH_TEST` and `CULL_FACE`, enables `BLEND`, and iterates `this.meshes` calling `renderMesh`.
- `Canvas.renderMesh()` checks `mesh.visible`, calls `makeTransform`, `makeNeedUniform`, then `mesh.render`. It recurses into `mesh.children` passing `mesh.uniformData.modelView.value` as `parentMatrix`.
- `Canvas.makeTransform()` multiplies `item.matrix` by `parentMatrix` with `mat3.mul` when a parent matrix exists, otherwise uses `item.matrix`. It injects `uniformData.modelView` and `uniformData.transform`.
- `Canvas.makeNeedUniform()` injects `aspect`, `pixelRatio`, and `scale` uniforms from `this.miniGL.viewport`.