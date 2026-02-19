.. meta::
	:keywords: omni, spot

<span id="class_PointLight2D"></span>

## PointLight2D

**Inherits:** [Light2D](class_light2d.md#class_Light2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Positional 2D light source.

### Description

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

### Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

### Properties


| [float](class_float.md#class_float) | [height](class_pointlight2d.md#class_PointLight2D_property_height) | `0.0` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [offset](class_pointlight2d.md#class_PointLight2D_property_offset) | `Vector2(0, 0)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_pointlight2d.md#class_PointLight2D_property_texture) |
| [float](class_float.md#class_float) | [texture_scale](class_pointlight2d.md#class_PointLight2D_property_texture_scale) | `1.0` |

---

### Property Descriptions

<span id="class_PointLight2D_property_height"></span>

[float](class_float.md#class_float) **height** = `0.0` [🔗](class_pointlight2d.md#class_PointLight2D_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The height of the light. Used with 2D normal mapping. The units are in pixels, e.g. if the height is 100, then it will illuminate an object 100 pixels away at a 45° angle to the plane.

---

<span id="class_PointLight2D_property_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **offset** = `Vector2(0, 0)` [🔗](class_pointlight2d.md#class_PointLight2D_property_offset)

- void **set_texture_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_texture_offset** ( )

The offset of the light's [texture](class_pointlight2d.md#class_PointLight2D_property_texture).

---

<span id="class_PointLight2D_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_pointlight2d.md#class_PointLight2D_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

[Texture2D](class_texture2d.md#class_Texture2D) used for the light's appearance.

---

<span id="class_PointLight2D_property_texture_scale"></span>

[float](class_float.md#class_float) **texture_scale** = `1.0` [🔗](class_pointlight2d.md#class_PointLight2D_property_texture_scale)

- void **set_texture_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_scale** ( )

The [texture](class_pointlight2d.md#class_PointLight2D_property_texture)'s scale factor.
