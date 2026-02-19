<span id="class_XRCamera3D"></span>

## XRCamera3D

**Inherits:** [Camera3D](class_camera3d.md#class_Camera3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A camera node which automatically positions itself based on XR tracking data.

### Description

A camera node which automatically positions itself based on XR tracking data.

In contrast to [XRController3D](class_xrcontroller3d.md#class_XRController3D), the render thread has access to more up-to-date tracking data, and the location of the **XRCamera3D** node can lag a few milliseconds behind what is used for rendering.

 **Note:** If [Viewport.use_xr](class_viewport.md#class_Viewport_property_use_xr) is `true`, most of the camera properties are overridden by the active [XRInterface](class_xrinterface.md#class_XRInterface). The only properties that can be trusted are the near and far planes.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [PhysicsInterpolationMode](class_node.md#enum_Node_PhysicsInterpolationMode) | physics_interpolation_mode | `2` (overrides [Node](class_node.md#class_Node_property_physics_interpolation_mode)) |
| --- | --- | --- |
