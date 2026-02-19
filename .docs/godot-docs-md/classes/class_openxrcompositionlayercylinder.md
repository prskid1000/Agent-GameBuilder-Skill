<span id="class_OpenXRCompositionLayerCylinder"></span>

## OpenXRCompositionLayerCylinder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class_OpenXRCompositionLayer) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

An OpenXR composition layer that is rendered as an internal slice of a cylinder.

### Description

An OpenXR composition layer that allows rendering a [SubViewport](class_subviewport.md#class_SubViewport) on an internal slice of a cylinder.

### Properties


| [float](class_float.md#class_float) | [aspect_ratio](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_aspect_ratio) | `1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [central_angle](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_central_angle) | `1.5707964` |
| [int](class_int.md#class_int) | [fallback_segments](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_fallback_segments) | `10` |
| [float](class_float.md#class_float) | [radius](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_radius) | `1.0` |

---

### Property Descriptions

<span id="class_OpenXRCompositionLayerCylinder_property_aspect_ratio"></span>

[float](class_float.md#class_float) **aspect_ratio** = `1.0` [🔗](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_aspect_ratio)

- void **set_aspect_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_aspect_ratio** ( )

The aspect ratio of the slice. Used to set the height relative to the width.

---

<span id="class_OpenXRCompositionLayerCylinder_property_central_angle"></span>

[float](class_float.md#class_float) **central_angle** = `1.5707964` [🔗](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_central_angle)

- void **set_central_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_central_angle** ( )

The central angle of the cylinder. Used to set the width.

---

<span id="class_OpenXRCompositionLayerCylinder_property_fallback_segments"></span>

[int](class_int.md#class_int) **fallback_segments** = `10` [🔗](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_fallback_segments)

- void **set_fallback_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fallback_segments** ( )

The number of segments to use in the fallback mesh.

---

<span id="class_OpenXRCompositionLayerCylinder_property_radius"></span>

[float](class_float.md#class_float) **radius** = `1.0` [🔗](class_openxrcompositionlayercylinder.md#class_OpenXRCompositionLayerCylinder_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The radius of the cylinder.
