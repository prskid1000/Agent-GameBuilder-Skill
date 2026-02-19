<span id="class_LabelSettings"></span>

## LabelSettings

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides common settings to customize the text in a [Label](class_label.md#class_Label).

### Description

**LabelSettings** is a resource that provides common settings to customize the text in a [Label](class_label.md#class_Label). It will take priority over the properties defined in [Control.theme](class_control.md#class_Control_property_theme). The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.

### Properties


| [Font](class_font.md#class_Font) | [font](class_labelsettings.md#class_LabelSettings_property_font) |
| --- | --- |
| [Color](class_color.md#class_Color) | [font_color](class_labelsettings.md#class_LabelSettings_property_font_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [font_size](class_labelsettings.md#class_LabelSettings_property_font_size) | `16` |
| [float](class_float.md#class_float) | [line_spacing](class_labelsettings.md#class_LabelSettings_property_line_spacing) | `3.0` |
| [Color](class_color.md#class_Color) | [outline_color](class_labelsettings.md#class_LabelSettings_property_outline_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [outline_size](class_labelsettings.md#class_LabelSettings_property_outline_size) | `0` |
| [float](class_float.md#class_float) | [paragraph_spacing](class_labelsettings.md#class_LabelSettings_property_paragraph_spacing) | `0.0` |
| [Color](class_color.md#class_Color) | [shadow_color](class_labelsettings.md#class_LabelSettings_property_shadow_color) | `Color(0, 0, 0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [shadow_offset](class_labelsettings.md#class_LabelSettings_property_shadow_offset) | `Vector2(1, 1)` |
| [int](class_int.md#class_int) | [shadow_size](class_labelsettings.md#class_LabelSettings_property_shadow_size) | `1` |
| [int](class_int.md#class_int) | [stacked_outline_count](class_labelsettings.md#class_LabelSettings_property_stacked_outline_count) | `0` |
| [int](class_int.md#class_int) | [stacked_shadow_count](class_labelsettings.md#class_LabelSettings_property_stacked_shadow_count) | `0` |

### Methods


| void | [add_stacked_outline](class_labelsettings.md#class_LabelSettings_method_add_stacked_outline) ( index: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [add_stacked_shadow](class_labelsettings.md#class_LabelSettings_method_add_stacked_shadow) ( index: [int](class_int.md#class_int) = -1 ) |
| [Color](class_color.md#class_Color) | [get_stacked_outline_color](class_labelsettings.md#class_LabelSettings_method_get_stacked_outline_color) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_stacked_outline_size](class_labelsettings.md#class_LabelSettings_method_get_stacked_outline_size) ( index: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_stacked_shadow_color](class_labelsettings.md#class_LabelSettings_method_get_stacked_shadow_color) ( index: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_stacked_shadow_offset](class_labelsettings.md#class_LabelSettings_method_get_stacked_shadow_offset) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_stacked_shadow_outline_size](class_labelsettings.md#class_LabelSettings_method_get_stacked_shadow_outline_size) ( index: [int](class_int.md#class_int) ) const |
| void | [move_stacked_outline](class_labelsettings.md#class_LabelSettings_method_move_stacked_outline) ( from_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [move_stacked_shadow](class_labelsettings.md#class_LabelSettings_method_move_stacked_shadow) ( from_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [remove_stacked_outline](class_labelsettings.md#class_LabelSettings_method_remove_stacked_outline) ( index: [int](class_int.md#class_int) ) |
| void | [remove_stacked_shadow](class_labelsettings.md#class_LabelSettings_method_remove_stacked_shadow) ( index: [int](class_int.md#class_int) ) |
| void | [set_stacked_outline_color](class_labelsettings.md#class_LabelSettings_method_set_stacked_outline_color) ( index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_stacked_outline_size](class_labelsettings.md#class_LabelSettings_method_set_stacked_outline_size) ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) |
| void | [set_stacked_shadow_color](class_labelsettings.md#class_LabelSettings_method_set_stacked_shadow_color) ( index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_stacked_shadow_offset](class_labelsettings.md#class_LabelSettings_method_set_stacked_shadow_offset) ( index: [int](class_int.md#class_int), offset: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_stacked_shadow_outline_size](class_labelsettings.md#class_LabelSettings_method_set_stacked_shadow_outline_size) ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_LabelSettings_property_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_labelsettings.md#class_LabelSettings_property_font)

- void **set_font** ( value: [Font](class_font.md#class_Font) )
- [Font](class_font.md#class_Font) **get_font** ( )

[Font](class_font.md#class_Font) used for the text.

---

<span id="class_LabelSettings_property_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(1, 1, 1, 1)` [🔗](class_labelsettings.md#class_LabelSettings_property_font_color)

- void **set_font_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_font_color** ( )

Color of the text.

---

<span id="class_LabelSettings_property_font_size"></span>

[int](class_int.md#class_int) **font_size** = `16` [🔗](class_labelsettings.md#class_LabelSettings_property_font_size)

- void **set_font_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_font_size** ( )

Size of the text.

---

<span id="class_LabelSettings_property_line_spacing"></span>

[float](class_float.md#class_float) **line_spacing** = `3.0` [🔗](class_labelsettings.md#class_LabelSettings_property_line_spacing)

- void **set_line_spacing** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_line_spacing** ( )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_LabelSettings_property_outline_color"></span>

[Color](class_color.md#class_Color) **outline_color** = `Color(1, 1, 1, 1)` [🔗](class_labelsettings.md#class_LabelSettings_property_outline_color)

- void **set_outline_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_outline_color** ( )

The color of the outline.

---

<span id="class_LabelSettings_property_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_labelsettings.md#class_LabelSettings_property_outline_size)

- void **set_outline_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_outline_size** ( )

Text outline size.

---

<span id="class_LabelSettings_property_paragraph_spacing"></span>

[float](class_float.md#class_float) **paragraph_spacing** = `0.0` [🔗](class_labelsettings.md#class_LabelSettings_property_paragraph_spacing)

- void **set_paragraph_spacing** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_paragraph_spacing** ( )

Vertical space between paragraphs. Added on top of [line_spacing](class_labelsettings.md#class_LabelSettings_property_line_spacing).

---

<span id="class_LabelSettings_property_shadow_color"></span>

[Color](class_color.md#class_Color) **shadow_color** = `Color(0, 0, 0, 0)` [🔗](class_labelsettings.md#class_LabelSettings_property_shadow_color)

- void **set_shadow_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_shadow_color** ( )

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

---

<span id="class_LabelSettings_property_shadow_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **shadow_offset** = `Vector2(1, 1)` [🔗](class_labelsettings.md#class_LabelSettings_property_shadow_offset)

- void **set_shadow_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_shadow_offset** ( )

Offset of the shadow effect, in pixels.

---

<span id="class_LabelSettings_property_shadow_size"></span>

[int](class_int.md#class_int) **shadow_size** = `1` [🔗](class_labelsettings.md#class_LabelSettings_property_shadow_size)

- void **set_shadow_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_shadow_size** ( )

Size of the shadow effect.

---

<span id="class_LabelSettings_property_stacked_outline_count"></span>

[int](class_int.md#class_int) **stacked_outline_count** = `0` [🔗](class_labelsettings.md#class_LabelSettings_property_stacked_outline_count)

- void **set_stacked_outline_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stacked_outline_count** ( )

The number of stacked outlines.

---

<span id="class_LabelSettings_property_stacked_shadow_count"></span>

[int](class_int.md#class_int) **stacked_shadow_count** = `0` [🔗](class_labelsettings.md#class_LabelSettings_property_stacked_shadow_count)

- void **set_stacked_shadow_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stacked_shadow_count** ( )

The number of stacked shadows.

---

### Method Descriptions

<span id="class_LabelSettings_method_add_stacked_outline"></span>

void **add_stacked_outline** ( index: [int](class_int.md#class_int) = -1 ) [🔗](class_labelsettings.md#class_LabelSettings_method_add_stacked_outline)

Adds a new stacked outline to the label at the given `index`. If `index` is `-1`, the new stacked outline will be added at the end of the list.

---

<span id="class_LabelSettings_method_add_stacked_shadow"></span>

void **add_stacked_shadow** ( index: [int](class_int.md#class_int) = -1 ) [🔗](class_labelsettings.md#class_LabelSettings_method_add_stacked_shadow)

Adds a new stacked shadow to the label at the given `index`. If `index` is `-1`, the new stacked shadow will be added at the end of the list.

---

<span id="class_LabelSettings_method_get_stacked_outline_color"></span>

[Color](class_color.md#class_Color) **get_stacked_outline_color** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_labelsettings.md#class_LabelSettings_method_get_stacked_outline_color)

Returns the color of the stacked outline at `index`.

---

<span id="class_LabelSettings_method_get_stacked_outline_size"></span>

[int](class_int.md#class_int) **get_stacked_outline_size** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_labelsettings.md#class_LabelSettings_method_get_stacked_outline_size)

Returns the size of the stacked outline at `index`.

---

<span id="class_LabelSettings_method_get_stacked_shadow_color"></span>

[Color](class_color.md#class_Color) **get_stacked_shadow_color** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_labelsettings.md#class_LabelSettings_method_get_stacked_shadow_color)

Returns the color of the stacked shadow at `index`.

---

<span id="class_LabelSettings_method_get_stacked_shadow_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **get_stacked_shadow_offset** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_labelsettings.md#class_LabelSettings_method_get_stacked_shadow_offset)

Returns the offset of the stacked shadow at `index`.

---

<span id="class_LabelSettings_method_get_stacked_shadow_outline_size"></span>

[int](class_int.md#class_int) **get_stacked_shadow_outline_size** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_labelsettings.md#class_LabelSettings_method_get_stacked_shadow_outline_size)

Returns the outline size of the stacked shadow at `index`.

---

<span id="class_LabelSettings_method_move_stacked_outline"></span>

void **move_stacked_outline** ( from_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_labelsettings.md#class_LabelSettings_method_move_stacked_outline)

Moves the stacked outline at index `from_index` to the given position `to_position` in the array.

---

<span id="class_LabelSettings_method_move_stacked_shadow"></span>

void **move_stacked_shadow** ( from_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_labelsettings.md#class_LabelSettings_method_move_stacked_shadow)

Moves the stacked shadow at index `from_index` to the given position `to_position` in the array.

---

<span id="class_LabelSettings_method_remove_stacked_outline"></span>

void **remove_stacked_outline** ( index: [int](class_int.md#class_int) ) [🔗](class_labelsettings.md#class_LabelSettings_method_remove_stacked_outline)

Removes the stacked outline at index `index`.

---

<span id="class_LabelSettings_method_remove_stacked_shadow"></span>

void **remove_stacked_shadow** ( index: [int](class_int.md#class_int) ) [🔗](class_labelsettings.md#class_LabelSettings_method_remove_stacked_shadow)

Removes the stacked shadow at index `index`.

---

<span id="class_LabelSettings_method_set_stacked_outline_color"></span>

void **set_stacked_outline_color** ( index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_labelsettings.md#class_LabelSettings_method_set_stacked_outline_color)

Sets the color of the stacked outline identified by the given `index` to `color`.

---

<span id="class_LabelSettings_method_set_stacked_outline_size"></span>

void **set_stacked_outline_size** ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) [🔗](class_labelsettings.md#class_LabelSettings_method_set_stacked_outline_size)

Sets the size of the stacked outline identified by the given `index` to `size`.

---

<span id="class_LabelSettings_method_set_stacked_shadow_color"></span>

void **set_stacked_shadow_color** ( index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_labelsettings.md#class_LabelSettings_method_set_stacked_shadow_color)

Sets the color of the stacked shadow identified by the given `index` to `color`.

---

<span id="class_LabelSettings_method_set_stacked_shadow_offset"></span>

void **set_stacked_shadow_offset** ( index: [int](class_int.md#class_int), offset: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_labelsettings.md#class_LabelSettings_method_set_stacked_shadow_offset)

Sets the offset of the stacked shadow identified by the given `index` to `offset`.

---

<span id="class_LabelSettings_method_set_stacked_shadow_outline_size"></span>

void **set_stacked_shadow_outline_size** ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) [🔗](class_labelsettings.md#class_LabelSettings_method_set_stacked_shadow_outline_size)

Sets the outline size of the stacked shadow identified by the given `index` to `size`.
