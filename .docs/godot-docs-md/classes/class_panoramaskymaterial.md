<span id="class_PanoramaSkyMaterial"></span>

## PanoramaSkyMaterial

**Inherits:** [Material](class_material.md#class_Material) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A material that provides a special texture to a [Sky](class_sky.md#class_Sky), usually an HDR panorama.

### Description

A resource referenced in a [Sky](class_sky.md#class_Sky) that is used to draw a background. **PanoramaSkyMaterial** functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a [Cubemap](class_cubemap.md#class_Cubemap).

Using an HDR panorama is strongly recommended for accurate, high-quality reflections. Godot supports the Radiance HDR (`.hdr`) and OpenEXR (`.exr`) image formats for this purpose.

You can use this tool to convert a cubemap to an equirectangular sky map.

### Properties


| [float](class_float.md#class_float) | [energy_multiplier](class_panoramaskymaterial.md#class_PanoramaSkyMaterial_property_energy_multiplier) | `1.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [filter](class_panoramaskymaterial.md#class_PanoramaSkyMaterial_property_filter) | `true` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [panorama](class_panoramaskymaterial.md#class_PanoramaSkyMaterial_property_panorama) |

---

### Property Descriptions

<span id="class_PanoramaSkyMaterial_property_energy_multiplier"></span>

[float](class_float.md#class_float) **energy_multiplier** = `1.0` [🔗](class_panoramaskymaterial.md#class_PanoramaSkyMaterial_property_energy_multiplier)

- void **set_energy_multiplier** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_energy_multiplier** ( )

The sky's overall brightness multiplier. Higher values result in a brighter sky.

---

<span id="class_PanoramaSkyMaterial_property_filter"></span>

[bool](class_bool.md#class_bool) **filter** = `true` [🔗](class_panoramaskymaterial.md#class_PanoramaSkyMaterial_property_filter)

- void **set_filtering_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_filtering_enabled** ( )

A boolean value to determine if the background texture should be filtered or not.

---

<span id="class_PanoramaSkyMaterial_property_panorama"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **panorama** [🔗](class_panoramaskymaterial.md#class_PanoramaSkyMaterial_property_panorama)

- void **set_panorama** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_panorama** ( )

[Texture2D](class_texture2d.md#class_Texture2D) to be applied to the **PanoramaSkyMaterial**.
