<span id="class_ColorPalette"></span>

## ColorPalette

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A resource class for managing a palette of colors, which can be loaded and saved using [ColorPicker](class_colorpicker.md#class_ColorPicker).

### Description

The **ColorPalette** resource is designed to store and manage a collection of colors. This resource is useful in scenarios where a predefined set of colors is required, such as for creating themes, designing user interfaces, or managing game assets. The built-in [ColorPicker](class_colorpicker.md#class_ColorPicker) control can also make use of **ColorPalette** without additional code.

### Properties


| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [colors](class_colorpalette.md#class_ColorPalette_property_colors) | `PackedColorArray()` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_ColorPalette_property_colors"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **colors** = `PackedColorArray()` [🔗](class_colorpalette.md#class_ColorPalette_property_colors)

- void **set_colors** ( value: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) )
- [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_colors** ( )

A [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) containing the colors in the palette.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.
