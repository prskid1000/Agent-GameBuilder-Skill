<span id="class_StyleBoxLine"></span>

## StyleBoxLine

**Inherits:** [StyleBox](class_stylebox.md#class_StyleBox) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [StyleBox](class_stylebox.md#class_StyleBox) that displays a single line of a given color and thickness.

### Description

A [StyleBox](class_stylebox.md#class_StyleBox) that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.

### Properties


| [Color](class_color.md#class_Color) | [color](class_styleboxline.md#class_StyleBoxLine_property_color) | `Color(0, 0, 0, 1)` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [grow_begin](class_styleboxline.md#class_StyleBoxLine_property_grow_begin) | `1.0` |
| [float](class_float.md#class_float) | [grow_end](class_styleboxline.md#class_StyleBoxLine_property_grow_end) | `1.0` |
| [int](class_int.md#class_int) | [thickness](class_styleboxline.md#class_StyleBoxLine_property_thickness) | `1` |
| [bool](class_bool.md#class_bool) | [vertical](class_styleboxline.md#class_StyleBoxLine_property_vertical) | `false` |

---

### Property Descriptions

<span id="class_StyleBoxLine_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(0, 0, 0, 1)` [🔗](class_styleboxline.md#class_StyleBoxLine_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

The line's color.

---

<span id="class_StyleBoxLine_property_grow_begin"></span>

[float](class_float.md#class_float) **grow_begin** = `1.0` [🔗](class_styleboxline.md#class_StyleBoxLine_property_grow_begin)

- void **set_grow_begin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_grow_begin** ( )

The number of pixels the line will extend before the **StyleBoxLine**'s bounds. If set to a negative value, the line will begin inside the **StyleBoxLine**'s bounds.

---

<span id="class_StyleBoxLine_property_grow_end"></span>

[float](class_float.md#class_float) **grow_end** = `1.0` [🔗](class_styleboxline.md#class_StyleBoxLine_property_grow_end)

- void **set_grow_end** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_grow_end** ( )

The number of pixels the line will extend past the **StyleBoxLine**'s bounds. If set to a negative value, the line will end inside the **StyleBoxLine**'s bounds.

---

<span id="class_StyleBoxLine_property_thickness"></span>

[int](class_int.md#class_int) **thickness** = `1` [🔗](class_styleboxline.md#class_StyleBoxLine_property_thickness)

- void **set_thickness** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_thickness** ( )

The line's thickness in pixels.

---

<span id="class_StyleBoxLine_property_vertical"></span>

[bool](class_bool.md#class_bool) **vertical** = `false` [🔗](class_styleboxline.md#class_StyleBoxLine_property_vertical)

- void **set_vertical** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_vertical** ( )

If `true`, the line will be vertical. If `false`, the line will be horizontal.
