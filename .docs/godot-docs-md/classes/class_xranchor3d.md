<span id="class_XRAnchor3D"></span>

## XRAnchor3D

**Inherits:** [XRNode3D](class_xrnode3d.md#class_XRNode3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

An anchor point in AR space.

### Description

The **XRAnchor3D** point is an [XRNode3D](class_xrnode3d.md#class_XRNode3D) that maps a real world location identified by the AR platform to a position within the game world. For example, as long as plane detection in ARKit is on, ARKit will identify and update the position of planes (tables, floors, etc.) and create anchors for them.

This node is mapped to one of the anchors through its unique ID. When you receive a signal that a new anchor is available, you should add this node to your scene for that anchor. You can predefine nodes and set the ID; the nodes will simply remain on `(0, 0, 0)` until a plane is recognized.

Keep in mind that, as long as plane detection is enabled, the size, placing and orientation of an anchor will be updated as the detection logic learns more about the real world out there especially if only part of the surface is in view.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Methods


| [Plane](class_plane.md#class_Plane) | [get_plane](class_xranchor3d.md#class_XRAnchor3D_method_get_plane) ( ) const |
| --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [get_size](class_xranchor3d.md#class_XRAnchor3D_method_get_size) ( ) const |

---

### Method Descriptions

<span id="class_XRAnchor3D_method_get_plane"></span>

[Plane](class_plane.md#class_Plane) **get_plane** ( ) *const* [🔗](class_xranchor3d.md#class_XRAnchor3D_method_get_plane)

Returns a plane aligned with our anchor; handy for intersection testing.

---

<span id="class_XRAnchor3D_method_get_size"></span>

[Vector3](class_vector3.md#class_Vector3) **get_size** ( ) *const* [🔗](class_xranchor3d.md#class_XRAnchor3D_method_get_size)

Returns the estimated size of the plane that was detected. Say when the anchor relates to a table in the real world, this is the estimated size of the surface of that table.
