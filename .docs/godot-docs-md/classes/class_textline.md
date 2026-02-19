<span id="class_TextLine"></span>

## TextLine

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds a line of text.

### Description

Abstraction over [TextServer](class_textserver.md#class_TextServer) for handling a single line of text.

### Properties


| HorizontalAlignment | [alignment](class_textline.md#class_TextLine_property_alignment) | `0` |
| --- | --- | --- |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [direction](class_textline.md#class_TextLine_property_direction) | `0` |
| [String](class_string.md#class_String) | [ellipsis_char](class_textline.md#class_TextLine_property_ellipsis_char) | `"…"` |
| bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] | [flags](class_textline.md#class_TextLine_property_flags) | `3` |
| [Orientation](class_textserver.md#enum_TextServer_Orientation) | [orientation](class_textline.md#class_TextLine_property_orientation) | `0` |
| [bool](class_bool.md#class_bool) | [preserve_control](class_textline.md#class_TextLine_property_preserve_control) | `false` |
| [bool](class_bool.md#class_bool) | [preserve_invalid](class_textline.md#class_TextLine_property_preserve_invalid) | `true` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [text_overrun_behavior](class_textline.md#class_TextLine_property_text_overrun_behavior) | `3` |
| [float](class_float.md#class_float) | [width](class_textline.md#class_TextLine_property_width) | `-1.0` |

### Methods


| [bool](class_bool.md#class_bool) | [add_object](class_textline.md#class_TextLine_method_add_object) ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, length: [int](class_int.md#class_int) = 1, baseline: [float](class_float.md#class_float) = 0.0 ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [add_string](class_textline.md#class_TextLine_method_add_string) ( text: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int), language: [String](class_string.md#class_String) = "", meta: [Variant](class_variant.md#class_Variant) = null ) |
| void | [clear](class_textline.md#class_TextLine_method_clear) ( ) |
| void | [draw](class_textline.md#class_TextLine_method_draw) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [draw_outline](class_textline.md#class_TextLine_method_draw_outline) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| [TextLine](class_textline.md#class_TextLine) | [duplicate](class_textline.md#class_TextLine_method_duplicate) ( ) const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [get_inferred_direction](class_textline.md#class_TextLine_method_get_inferred_direction) ( ) const |
| [float](class_float.md#class_float) | [get_line_ascent](class_textline.md#class_TextLine_method_get_line_ascent) ( ) const |
| [float](class_float.md#class_float) | [get_line_descent](class_textline.md#class_TextLine_method_get_line_descent) ( ) const |
| [float](class_float.md#class_float) | [get_line_underline_position](class_textline.md#class_TextLine_method_get_line_underline_position) ( ) const |
| [float](class_float.md#class_float) | [get_line_underline_thickness](class_textline.md#class_TextLine_method_get_line_underline_thickness) ( ) const |
| [float](class_float.md#class_float) | [get_line_width](class_textline.md#class_TextLine_method_get_line_width) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_object_rect](class_textline.md#class_TextLine_method_get_object_rect) ( key: [Variant](class_variant.md#class_Variant) ) const |
| [Array](class_array.md#class_Array) | [get_objects](class_textline.md#class_TextLine_method_get_objects) ( ) const |
| [RID](class_rid.md#class_RID) | [get_rid](class_textline.md#class_TextLine_method_get_rid) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_size](class_textline.md#class_TextLine_method_get_size) ( ) const |
| [bool](class_bool.md#class_bool) | [has_object](class_textline.md#class_TextLine_method_has_object) ( key: [Variant](class_variant.md#class_Variant) ) const |
| [int](class_int.md#class_int) | [hit_test](class_textline.md#class_TextLine_method_hit_test) ( coords: [float](class_float.md#class_float) ) const |
| [bool](class_bool.md#class_bool) | [resize_object](class_textline.md#class_TextLine_method_resize_object) ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, baseline: [float](class_float.md#class_float) = 0.0 ) |
| void | [set_bidi_override](class_textline.md#class_TextLine_method_set_bidi_override) ( override: [Array](class_array.md#class_Array) ) |
| void | [tab_align](class_textline.md#class_TextLine_method_tab_align) ( tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |

---

### Property Descriptions

<span id="class_TextLine_property_alignment"></span>

HorizontalAlignment **alignment** = `0` [🔗](class_textline.md#class_TextLine_property_alignment)

- void **set_horizontal_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_horizontal_alignment** ( )

Sets text alignment within the line as if the line was horizontal.

---

<span id="class_TextLine_property_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **direction** = `0` [🔗](class_textline.md#class_TextLine_property_direction)

- void **set_direction** ( value: [Direction](class_textserver.md#enum_TextServer_Direction) )
- [Direction](class_textserver.md#enum_TextServer_Direction) **get_direction** ( )

Text writing direction.

---

<span id="class_TextLine_property_ellipsis_char"></span>

[String](class_string.md#class_String) **ellipsis_char** = `"…"` [🔗](class_textline.md#class_TextLine_property_ellipsis_char)

- void **set_ellipsis_char** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_ellipsis_char** ( )

Ellipsis character used for text clipping.

---

<span id="class_TextLine_property_flags"></span>

*BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **flags** = `3` [🔗](class_textline.md#class_TextLine_property_flags)

- void **set_flags** ( value: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] )
- *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **get_flags** ( )

Line alignment rules. For more info see [TextServer](class_textserver.md#class_TextServer).

---

<span id="class_TextLine_property_orientation"></span>

[Orientation](class_textserver.md#enum_TextServer_Orientation) **orientation** = `0` [🔗](class_textline.md#class_TextLine_property_orientation)

- void **set_orientation** ( value: [Orientation](class_textserver.md#enum_TextServer_Orientation) )
- [Orientation](class_textserver.md#enum_TextServer_Orientation) **get_orientation** ( )

Text orientation.

---

<span id="class_TextLine_property_preserve_control"></span>

[bool](class_bool.md#class_bool) **preserve_control** = `false` [🔗](class_textline.md#class_TextLine_property_preserve_control)

- void **set_preserve_control** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_preserve_control** ( )

If set to `true` text will display control characters.

---

<span id="class_TextLine_property_preserve_invalid"></span>

[bool](class_bool.md#class_bool) **preserve_invalid** = `true` [🔗](class_textline.md#class_TextLine_property_preserve_invalid)

- void **set_preserve_invalid** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_preserve_invalid** ( )

If set to `true` text will display invalid characters.

---

<span id="class_TextLine_property_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **text_overrun_behavior** = `3` [🔗](class_textline.md#class_TextLine_property_text_overrun_behavior)

- void **set_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( )

The clipping behavior when the text exceeds the text line's set width.

---

<span id="class_TextLine_property_width"></span>

[float](class_float.md#class_float) **width** = `-1.0` [🔗](class_textline.md#class_TextLine_property_width)

- void **set_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_width** ( )

Text line width.

---

### Method Descriptions

<span id="class_TextLine_method_add_object"></span>

[bool](class_bool.md#class_bool) **add_object** ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, length: [int](class_int.md#class_int) = 1, baseline: [float](class_float.md#class_float) = 0.0 ) [🔗](class_textline.md#class_TextLine_method_add_object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

<span id="class_TextLine_method_add_string"></span>

[bool](class_bool.md#class_bool) **add_string** ( text: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int), language: [String](class_string.md#class_String) = "", meta: [Variant](class_variant.md#class_Variant) = null ) [🔗](class_textline.md#class_TextLine_method_add_string)

Adds text span and font to draw it.

---

<span id="class_TextLine_method_clear"></span>

void **clear** ( ) [🔗](class_textline.md#class_TextLine_method_clear)

Clears text line (removes text and inline objects).

---

<span id="class_TextLine_method_draw"></span>

void **draw** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textline.md#class_TextLine_method_draw)

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextLine_method_draw_outline"></span>

void **draw_outline** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textline.md#class_TextLine_method_draw_outline)

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextLine_method_duplicate"></span>

[TextLine](class_textline.md#class_TextLine) **duplicate** ( ) *const* [🔗](class_textline.md#class_TextLine_method_duplicate)

Duplicates this **TextLine**.

---

<span id="class_TextLine_method_get_inferred_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **get_inferred_direction** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_inferred_direction)

Returns the text writing direction inferred by the BiDi algorithm.

---

<span id="class_TextLine_method_get_line_ascent"></span>

[float](class_float.md#class_float) **get_line_ascent** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_line_ascent)

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---

<span id="class_TextLine_method_get_line_descent"></span>

[float](class_float.md#class_float) **get_line_descent** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_line_descent)

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---

<span id="class_TextLine_method_get_line_underline_position"></span>

[float](class_float.md#class_float) **get_line_underline_position** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_line_underline_position)

Returns pixel offset of the underline below the baseline.

---

<span id="class_TextLine_method_get_line_underline_thickness"></span>

[float](class_float.md#class_float) **get_line_underline_thickness** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_line_underline_thickness)

Returns thickness of the underline.

---

<span id="class_TextLine_method_get_line_width"></span>

[float](class_float.md#class_float) **get_line_width** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_line_width)

Returns width (for horizontal layout) or height (for vertical) of the text.

---

<span id="class_TextLine_method_get_object_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_object_rect** ( key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textline.md#class_TextLine_method_get_object_rect)

Returns bounding rectangle of the inline object.

---

<span id="class_TextLine_method_get_objects"></span>

[Array](class_array.md#class_Array) **get_objects** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_objects)

Returns array of inline objects.

---

<span id="class_TextLine_method_get_rid"></span>

[RID](class_rid.md#class_RID) **get_rid** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_rid)

Returns TextServer buffer RID.

---

<span id="class_TextLine_method_get_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_size** ( ) *const* [🔗](class_textline.md#class_TextLine_method_get_size)

Returns size of the bounding box of the text.

---

<span id="class_TextLine_method_has_object"></span>

[bool](class_bool.md#class_bool) **has_object** ( key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textline.md#class_TextLine_method_has_object)

Returns `true` if an object with `key` is embedded in this line.

---

<span id="class_TextLine_method_hit_test"></span>

[int](class_int.md#class_int) **hit_test** ( coords: [float](class_float.md#class_float) ) *const* [🔗](class_textline.md#class_TextLine_method_hit_test)

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---

<span id="class_TextLine_method_resize_object"></span>

[bool](class_bool.md#class_bool) **resize_object** ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, baseline: [float](class_float.md#class_float) = 0.0 ) [🔗](class_textline.md#class_TextLine_method_resize_object)

Sets new size and alignment of embedded object.

---

<span id="class_TextLine_method_set_bidi_override"></span>

void **set_bidi_override** ( override: [Array](class_array.md#class_Array) ) [🔗](class_textline.md#class_TextLine_method_set_bidi_override)

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---

<span id="class_TextLine_method_tab_align"></span>

void **tab_align** ( tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_textline.md#class_TextLine_method_tab_align)

Aligns text to the given tab-stops.
