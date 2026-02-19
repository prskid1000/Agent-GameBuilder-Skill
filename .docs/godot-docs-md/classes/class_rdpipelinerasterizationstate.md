<span id="class_RDPipelineRasterizationState"></span>

## RDPipelineRasterizationState

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Pipeline rasterization state (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) | [cull_mode](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_cull_mode) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [depth_bias_clamp](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_clamp) | `0.0` |
| [float](class_float.md#class_float) | [depth_bias_constant_factor](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_constant_factor) | `0.0` |
| [bool](class_bool.md#class_bool) | [depth_bias_enabled](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_enabled) | `false` |
| [float](class_float.md#class_float) | [depth_bias_slope_factor](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_slope_factor) | `0.0` |
| [bool](class_bool.md#class_bool) | [discard_primitives](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_discard_primitives) | `false` |
| [bool](class_bool.md#class_bool) | [enable_depth_clamp](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_enable_depth_clamp) | `false` |
| [PolygonFrontFace](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace) | [front_face](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_front_face) | `0` |
| [float](class_float.md#class_float) | [line_width](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_line_width) | `1.0` |
| [int](class_int.md#class_int) | [patch_control_points](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_patch_control_points) | `1` |
| [bool](class_bool.md#class_bool) | [wireframe](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_wireframe) | `false` |

---

### Property Descriptions

<span id="class_RDPipelineRasterizationState_property_cull_mode"></span>

[PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) **cull_mode** = `0` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_cull_mode)

- void **set_cull_mode** ( value: [PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) )
- [PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) **get_cull_mode** ( )

The cull mode to use when drawing polygons, which determines whether front faces or backfaces are hidden.

---

<span id="class_RDPipelineRasterizationState_property_depth_bias_clamp"></span>

[float](class_float.md#class_float) **depth_bias_clamp** = `0.0` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_clamp)

- void **set_depth_bias_clamp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_bias_clamp** ( )

A limit for how much each depth value can be offset. If negative, it serves as a minimum value, but if positive, it serves as a maximum value.

---

<span id="class_RDPipelineRasterizationState_property_depth_bias_constant_factor"></span>

[float](class_float.md#class_float) **depth_bias_constant_factor** = `0.0` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_constant_factor)

- void **set_depth_bias_constant_factor** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_bias_constant_factor** ( )

A constant offset added to each depth value. Applied after [depth_bias_slope_factor](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_slope_factor).

---

<span id="class_RDPipelineRasterizationState_property_depth_bias_enabled"></span>

[bool](class_bool.md#class_bool) **depth_bias_enabled** = `false` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_enabled)

- void **set_depth_bias_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_depth_bias_enabled** ( )

If `true`, each generated depth value will by offset by some amount. The specific amount is generated per polygon based on the values of [depth_bias_slope_factor](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_slope_factor) and [depth_bias_constant_factor](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_constant_factor).

---

<span id="class_RDPipelineRasterizationState_property_depth_bias_slope_factor"></span>

[float](class_float.md#class_float) **depth_bias_slope_factor** = `0.0` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_slope_factor)

- void **set_depth_bias_slope_factor** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_bias_slope_factor** ( )

A constant scale applied to the slope of each polygons' depth. Applied before [depth_bias_constant_factor](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_depth_bias_constant_factor).

---

<span id="class_RDPipelineRasterizationState_property_discard_primitives"></span>

[bool](class_bool.md#class_bool) **discard_primitives** = `false` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_discard_primitives)

- void **set_discard_primitives** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_discard_primitives** ( )

If `true`, primitives are discarded immediately before the rasterization stage.

---

<span id="class_RDPipelineRasterizationState_property_enable_depth_clamp"></span>

[bool](class_bool.md#class_bool) **enable_depth_clamp** = `false` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_enable_depth_clamp)

- void **set_enable_depth_clamp** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_depth_clamp** ( )

If `true`, clamps depth values according to the minimum and maximum depth of the associated viewport.

---

<span id="class_RDPipelineRasterizationState_property_front_face"></span>

[PolygonFrontFace](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace) **front_face** = `0` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_front_face)

- void **set_front_face** ( value: [PolygonFrontFace](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace) )
- [PolygonFrontFace](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace) **get_front_face** ( )

The winding order to use to determine which face of a triangle is considered its front face.

---

<span id="class_RDPipelineRasterizationState_property_line_width"></span>

[float](class_float.md#class_float) **line_width** = `1.0` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_line_width)

- void **set_line_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_line_width** ( )

The line width to use when drawing lines (in pixels). Thick lines may not be supported on all hardware.

---

<span id="class_RDPipelineRasterizationState_property_patch_control_points"></span>

[int](class_int.md#class_int) **patch_control_points** = `1` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_patch_control_points)

- void **set_patch_control_points** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_patch_control_points** ( )

The number of control points to use when drawing a patch with tessellation enabled. Higher values result in higher quality at the cost of performance.

---

<span id="class_RDPipelineRasterizationState_property_wireframe"></span>

[bool](class_bool.md#class_bool) **wireframe** = `false` [🔗](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState_property_wireframe)

- void **set_wireframe** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_wireframe** ( )

If `true`, performs wireframe rendering for triangles instead of flat or textured rendering.
