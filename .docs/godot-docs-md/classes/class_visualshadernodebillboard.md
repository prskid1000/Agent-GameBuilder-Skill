<span id="class_VisualShaderNodeBillboard"></span>

## VisualShaderNodeBillboard

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A node that controls how the object faces the camera to be used within the visual shader graph.

### Description

The output port of this node needs to be connected to `Model View Matrix` port of [VisualShaderNodeOutput](class_visualshadernodeoutput.md#class_VisualShaderNodeOutput).

### Properties


| [BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) | [billboard_type](class_visualshadernodebillboard.md#class_VisualShaderNodeBillboard_property_billboard_type) | `1` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [keep_scale](class_visualshadernodebillboard.md#class_VisualShaderNodeBillboard_property_keep_scale) | `false` |

---

### Enumerations

<span id="enum_VisualShaderNodeBillboard_BillboardType"></span>

enum **BillboardType**: [🔗](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType)

<span id="class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_DISABLED"></span>

[BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **BILLBOARD_TYPE_DISABLED** = `0`

Billboarding is disabled and the node does nothing.

<span id="class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_ENABLED"></span>

[BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **BILLBOARD_TYPE_ENABLED** = `1`

A standard billboarding algorithm is enabled.

<span id="class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_FIXED_Y"></span>

[BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **BILLBOARD_TYPE_FIXED_Y** = `2`

A billboarding algorithm to rotate around Y-axis is enabled.

<span id="class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_PARTICLES"></span>

[BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **BILLBOARD_TYPE_PARTICLES** = `3`

A billboarding algorithm designed to use on particles is enabled.

<span id="class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_MAX"></span>

[BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **BILLBOARD_TYPE_MAX** = `4`

Represents the size of the [BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeBillboard_property_billboard_type"></span>

[BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **billboard_type** = `1` [🔗](class_visualshadernodebillboard.md#class_VisualShaderNodeBillboard_property_billboard_type)

- void **set_billboard_type** ( value: [BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) )
- [BillboardType](class_visualshadernodebillboard.md#enum_VisualShaderNodeBillboard_BillboardType) **get_billboard_type** ( )

Controls how the object faces the camera.

---

<span id="class_VisualShaderNodeBillboard_property_keep_scale"></span>

[bool](class_bool.md#class_bool) **keep_scale** = `false` [🔗](class_visualshadernodebillboard.md#class_VisualShaderNodeBillboard_property_keep_scale)

- void **set_keep_scale_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_keep_scale_enabled** ( )

If `true`, the shader will keep the scale set for the mesh. Otherwise, the scale is lost when billboarding.
