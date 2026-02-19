<span id="class_DPITexture"></span>

## DPITexture

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An automatically scalable [Texture2D](class_texture2d.md#class_Texture2D) based on an SVG image.

### Description

An automatically scalable [Texture2D](class_texture2d.md#class_Texture2D) based on an SVG image. **DPITexture** s are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also ProjectSettings.display/window/stretch/mode ("canvas_items" mode) and [Viewport.oversampling_override](class_viewport.md#class_Viewport_property_oversampling_override).

### Properties


| [float](class_float.md#class_float) | [base_scale](class_dpitexture.md#class_DPITexture_property_base_scale) | `1.0` |
| --- | --- | --- |
| [Dictionary](class_dictionary.md#class_Dictionary) | [color_map](class_dpitexture.md#class_DPITexture_property_color_map) | `{}` |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [float](class_float.md#class_float) | [saturation](class_dpitexture.md#class_DPITexture_property_saturation) | `1.0` |

### Methods


| [DPITexture](class_dpitexture.md#class_DPITexture) | [create_from_string](class_dpitexture.md#class_DPITexture_method_create_from_string) ( source: [String](class_string.md#class_String), scale: [float](class_float.md#class_float) = 1.0, saturation: [float](class_float.md#class_float) = 1.0, color_map: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) static |
| --- | --- |
| [RID](class_rid.md#class_RID) | [get_scaled_rid](class_dpitexture.md#class_DPITexture_method_get_scaled_rid) ( ) const |
| [String](class_string.md#class_String) | [get_source](class_dpitexture.md#class_DPITexture_method_get_source) ( ) const |
| void | [set_size_override](class_dpitexture.md#class_DPITexture_method_set_size_override) ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [set_source](class_dpitexture.md#class_DPITexture_method_set_source) ( source: [String](class_string.md#class_String) ) |

---

### Property Descriptions

<span id="class_DPITexture_property_base_scale"></span>

[float](class_float.md#class_float) **base_scale** = `1.0` [🔗](class_dpitexture.md#class_DPITexture_property_base_scale)

- void **set_base_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_base_scale** ( )

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

---

<span id="class_DPITexture_property_color_map"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **color_map** = `{}` [🔗](class_dpitexture.md#class_DPITexture_property_color_map)

- void **set_color_map** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_color_map** ( )

If set, remaps texture colors according to [Color](class_color.md#class_Color)-[Color](class_color.md#class_Color) map.

---

<span id="class_DPITexture_property_saturation"></span>

[float](class_float.md#class_float) **saturation** = `1.0` [🔗](class_dpitexture.md#class_DPITexture_property_saturation)

- void **set_saturation** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_saturation** ( )

Overrides texture saturation.

---

### Method Descriptions

<span id="class_DPITexture_method_create_from_string"></span>

[DPITexture](class_dpitexture.md#class_DPITexture) **create_from_string** ( source: [String](class_string.md#class_String), scale: [float](class_float.md#class_float) = 1.0, saturation: [float](class_float.md#class_float) = 1.0, color_map: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) *static* [🔗](class_dpitexture.md#class_DPITexture_method_create_from_string)

Creates a new **DPITexture** and initializes it by allocating and setting the SVG data to `source`.

---

<span id="class_DPITexture_method_get_scaled_rid"></span>

[RID](class_rid.md#class_RID) **get_scaled_rid** ( ) *const* [🔗](class_dpitexture.md#class_DPITexture_method_get_scaled_rid)

Returns the [RID](class_rid.md#class_RID) of the texture rasterized to match the oversampling of the currently drawn canvas item.

---

<span id="class_DPITexture_method_get_source"></span>

[String](class_string.md#class_String) **get_source** ( ) *const* [🔗](class_dpitexture.md#class_DPITexture_method_get_source)

Returns this SVG texture's source code.

---

<span id="class_DPITexture_method_set_size_override"></span>

void **set_size_override** ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_dpitexture.md#class_DPITexture_method_set_size_override)

Resizes the texture to the specified dimensions.

---

<span id="class_DPITexture_method_set_source"></span>

void **set_source** ( source: [String](class_string.md#class_String) ) [🔗](class_dpitexture.md#class_DPITexture_method_set_source)

Sets this SVG texture's source code.
