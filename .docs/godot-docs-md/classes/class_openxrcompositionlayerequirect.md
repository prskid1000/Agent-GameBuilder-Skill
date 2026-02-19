<span id="class_OpenXRCompositionLayerEquirect"></span>

## OpenXRCompositionLayerEquirect

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class_OpenXRCompositionLayer) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

An OpenXR composition layer that is rendered as an internal slice of a sphere.

### Description

An OpenXR composition layer that allows rendering a [SubViewport](class_subviewport.md#class_SubViewport) on an internal slice of a sphere.

### Properties


| [float](class_float.md#class_float) | [central_horizontal_angle](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle) | `1.5707964` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [fallback_segments](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_fallback_segments) | `10` |
| [float](class_float.md#class_float) | [lower_vertical_angle](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle) | `0.7853982` |
| [float](class_float.md#class_float) | [radius](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_radius) | `1.0` |
| [float](class_float.md#class_float) | [upper_vertical_angle](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle) | `0.7853982` |

---

### Property Descriptions

<span id="class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle"></span>

[float](class_float.md#class_float) **central_horizontal_angle** = `1.5707964` [🔗](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle)

- void **set_central_horizontal_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_central_horizontal_angle** ( )

The central horizontal angle of the sphere. Used to set the width.

---

<span id="class_OpenXRCompositionLayerEquirect_property_fallback_segments"></span>

[int](class_int.md#class_int) **fallback_segments** = `10` [🔗](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_fallback_segments)

- void **set_fallback_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fallback_segments** ( )

The number of segments to use in the fallback mesh.

---

<span id="class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle"></span>

[float](class_float.md#class_float) **lower_vertical_angle** = `0.7853982` [🔗](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle)

- void **set_lower_vertical_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lower_vertical_angle** ( )

The lower vertical angle of the sphere. Used (together with [upper_vertical_angle](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle)) to set the height.

---

<span id="class_OpenXRCompositionLayerEquirect_property_radius"></span>

[float](class_float.md#class_float) **radius** = `1.0` [🔗](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The radius of the sphere.

---

<span id="class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle"></span>

[float](class_float.md#class_float) **upper_vertical_angle** = `0.7853982` [🔗](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle)

- void **set_upper_vertical_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_upper_vertical_angle** ( )

The upper vertical angle of the sphere. Used (together with [lower_vertical_angle](class_openxrcompositionlayerequirect.md#class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle)) to set the height.
