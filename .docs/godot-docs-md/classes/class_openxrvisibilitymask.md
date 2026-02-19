<span id="class_OpenXRVisibilityMask"></span>

## OpenXRVisibilityMask

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Draws a stereo correct visibility mask.

### Description

The visibility mask allows us to black out the part of the render result that is invisible due to lens distortion.

As this is rendered first, it prevents fragments with expensive lighting calculations to be processed as they are discarded through z-checking.
