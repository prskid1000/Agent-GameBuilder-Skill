<span id="class_LightOccluder2D"></span>

## LightOccluder2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Occludes light cast by a Light2D, casting shadows.

### Description

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D must be provided with an [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) in order for the shadow to be computed.

### Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

### Properties


| [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) | [occluder](class_lightoccluder2d.md#class_LightOccluder2D_property_occluder) |
| --- | --- |
| [int](class_int.md#class_int) | [occluder_light_mask](class_lightoccluder2d.md#class_LightOccluder2D_property_occluder_light_mask) | `1` |
| [bool](class_bool.md#class_bool) | [sdf_collision](class_lightoccluder2d.md#class_LightOccluder2D_property_sdf_collision) | `true` |

---

### Property Descriptions

<span id="class_LightOccluder2D_property_occluder"></span>

[OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) **occluder** [🔗](class_lightoccluder2d.md#class_LightOccluder2D_property_occluder)

- void **set_occluder_polygon** ( value: [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) )
- [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) **get_occluder_polygon** ( )

The [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) used to compute the shadow.

---

<span id="class_LightOccluder2D_property_occluder_light_mask"></span>

[int](class_int.md#class_int) **occluder_light_mask** = `1` [🔗](class_lightoccluder2d.md#class_LightOccluder2D_property_occluder_light_mask)

- void **set_occluder_light_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_occluder_light_mask** ( )

The LightOccluder2D's occluder light mask. The LightOccluder2D will cast shadows only from Light2D(s) that have the same light mask(s).

---

<span id="class_LightOccluder2D_property_sdf_collision"></span>

[bool](class_bool.md#class_bool) **sdf_collision** = `true` [🔗](class_lightoccluder2d.md#class_LightOccluder2D_property_sdf_collision)

- void **set_as_sdf_collision** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_set_as_sdf_collision** ( )

If enabled, the occluder will be part of a real-time generated signed distance field that can be used in custom shaders.
