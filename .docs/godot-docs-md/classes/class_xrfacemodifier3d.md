<span id="class_XRFaceModifier3D"></span>

## XRFaceModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node for driving standard face meshes from [XRFaceTracker](class_xrfacetracker.md#class_XRFaceTracker) weights.

### Description

This node applies weights from an [XRFaceTracker](class_xrfacetracker.md#class_XRFaceTracker) to a mesh with supporting face blend shapes.

The Unified Expressions blend shapes are supported, as well as ARKit and SRanipal blend shapes.

The node attempts to identify blend shapes based on name matching. Blend shapes should match the names listed in the Unified Expressions Compatibility chart.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [StringName](class_stringname.md#class_StringName) | [face_tracker](class_xrfacemodifier3d.md#class_XRFaceModifier3D_property_face_tracker) | `&"/user/face_tracker"` |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [target](class_xrfacemodifier3d.md#class_XRFaceModifier3D_property_target) | `NodePath("")` |

---

### Property Descriptions

<span id="class_XRFaceModifier3D_property_face_tracker"></span>

[StringName](class_stringname.md#class_StringName) **face_tracker** = `&"/user/face_tracker"` [🔗](class_xrfacemodifier3d.md#class_XRFaceModifier3D_property_face_tracker)

- void **set_face_tracker** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_face_tracker** ( )

The [XRFaceTracker](class_xrfacetracker.md#class_XRFaceTracker) path.

---

<span id="class_XRFaceModifier3D_property_target"></span>

[NodePath](class_nodepath.md#class_NodePath) **target** = `NodePath("")` [🔗](class_xrfacemodifier3d.md#class_XRFaceModifier3D_property_target)

- void **set_target** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_target** ( )

The [NodePath](class_nodepath.md#class_NodePath) of the face [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D).
