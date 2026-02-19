<span id="class_OccluderPolygon2D"></span>

## OccluderPolygon2D

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Defines a 2D polygon for LightOccluder2D.

### Description

Editor facility that helps you draw a 2D polygon used as resource for [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D).

### Properties


| [bool](class_bool.md#class_bool) | [closed](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_closed) | `true` |
| --- | --- | --- |
| [CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) | [cull_mode](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_cull_mode) | `0` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [polygon](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_polygon) | `PackedVector2Array()` |

---

### Enumerations

<span id="enum_OccluderPolygon2D_CullMode"></span>

enum **CullMode**: [🔗](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode)

<span id="class_OccluderPolygon2D_constant_CULL_DISABLED"></span>

[CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) **CULL_DISABLED** = `0`

Culling is disabled. See [cull_mode](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_cull_mode).

<span id="class_OccluderPolygon2D_constant_CULL_CLOCKWISE"></span>

[CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) **CULL_CLOCKWISE** = `1`

Culling is performed in the clockwise direction. See [cull_mode](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_cull_mode).

<span id="class_OccluderPolygon2D_constant_CULL_COUNTER_CLOCKWISE"></span>

[CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) **CULL_COUNTER_CLOCKWISE** = `2`

Culling is performed in the counterclockwise direction. See [cull_mode](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_cull_mode).

---

### Property Descriptions

<span id="class_OccluderPolygon2D_property_closed"></span>

[bool](class_bool.md#class_bool) **closed** = `true` [🔗](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_closed)

- void **set_closed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_closed** ( )

If `true`, closes the polygon. A closed OccluderPolygon2D occludes the light coming from any direction. An opened OccluderPolygon2D occludes the light only at its outline's direction.

---

<span id="class_OccluderPolygon2D_property_cull_mode"></span>

[CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) **cull_mode** = `0` [🔗](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_cull_mode)

- void **set_cull_mode** ( value: [CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) )
- [CullMode](class_occluderpolygon2d.md#enum_OccluderPolygon2D_CullMode) **get_cull_mode** ( )

The culling mode to use.

---

<span id="class_OccluderPolygon2D_property_polygon"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **polygon** = `PackedVector2Array()` [🔗](class_occluderpolygon2d.md#class_OccluderPolygon2D_property_polygon)

- void **set_polygon** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_polygon** ( )

A [Vector2](class_vector2.md#class_Vector2) array with the index for polygon's vertices positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.
