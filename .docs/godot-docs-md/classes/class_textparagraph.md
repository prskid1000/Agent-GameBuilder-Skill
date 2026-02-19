<span id="class_TextParagraph"></span>

## TextParagraph

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds a paragraph of text.

### Description

Abstraction over [TextServer](class_textserver.md#class_TextServer) for handling a single paragraph of text.

### Properties


| HorizontalAlignment | [alignment](class_textparagraph.md#class_TextParagraph_property_alignment) | `0` |
| --- | --- | --- |
| bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] | [break_flags](class_textparagraph.md#class_TextParagraph_property_break_flags) | `3` |
| [String](class_string.md#class_String) | [custom_punctuation](class_textparagraph.md#class_TextParagraph_property_custom_punctuation) | `""` |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [direction](class_textparagraph.md#class_TextParagraph_property_direction) | `0` |
| [String](class_string.md#class_String) | [ellipsis_char](class_textparagraph.md#class_TextParagraph_property_ellipsis_char) | `"…"` |
| bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] | [justification_flags](class_textparagraph.md#class_TextParagraph_property_justification_flags) | `163` |
| [float](class_float.md#class_float) | [line_spacing](class_textparagraph.md#class_TextParagraph_property_line_spacing) | `0.0` |
| [int](class_int.md#class_int) | [max_lines_visible](class_textparagraph.md#class_TextParagraph_property_max_lines_visible) | `-1` |
| [Orientation](class_textserver.md#enum_TextServer_Orientation) | [orientation](class_textparagraph.md#class_TextParagraph_property_orientation) | `0` |
| [bool](class_bool.md#class_bool) | [preserve_control](class_textparagraph.md#class_TextParagraph_property_preserve_control) | `false` |
| [bool](class_bool.md#class_bool) | [preserve_invalid](class_textparagraph.md#class_TextParagraph_property_preserve_invalid) | `true` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [text_overrun_behavior](class_textparagraph.md#class_TextParagraph_property_text_overrun_behavior) | `0` |
| [float](class_float.md#class_float) | [width](class_textparagraph.md#class_TextParagraph_property_width) | `-1.0` |

### Methods


| [bool](class_bool.md#class_bool) | [add_object](class_textparagraph.md#class_TextParagraph_method_add_object) ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, length: [int](class_int.md#class_int) = 1, baseline: [float](class_float.md#class_float) = 0.0 ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [add_string](class_textparagraph.md#class_TextParagraph_method_add_string) ( text: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int), language: [String](class_string.md#class_String) = "", meta: [Variant](class_variant.md#class_Variant) = null ) |
| void | [clear](class_textparagraph.md#class_TextParagraph_method_clear) ( ) |
| void | [clear_dropcap](class_textparagraph.md#class_TextParagraph_method_clear_dropcap) ( ) |
| void | [draw](class_textparagraph.md#class_TextParagraph_method_draw) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [draw_dropcap](class_textparagraph.md#class_TextParagraph_method_draw_dropcap) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [draw_dropcap_outline](class_textparagraph.md#class_TextParagraph_method_draw_dropcap_outline) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [draw_line](class_textparagraph.md#class_TextParagraph_method_draw_line) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), line: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [draw_line_outline](class_textparagraph.md#class_TextParagraph_method_draw_line_outline) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), line: [int](class_int.md#class_int), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [draw_outline](class_textparagraph.md#class_TextParagraph_method_draw_outline) ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| [TextParagraph](class_textparagraph.md#class_TextParagraph) | [duplicate](class_textparagraph.md#class_TextParagraph_method_duplicate) ( ) const |
| [int](class_int.md#class_int) | [get_dropcap_lines](class_textparagraph.md#class_TextParagraph_method_get_dropcap_lines) ( ) const |
| [RID](class_rid.md#class_RID) | [get_dropcap_rid](class_textparagraph.md#class_TextParagraph_method_get_dropcap_rid) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_dropcap_size](class_textparagraph.md#class_TextParagraph_method_get_dropcap_size) ( ) const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [get_inferred_direction](class_textparagraph.md#class_TextParagraph_method_get_inferred_direction) ( ) const |
| [float](class_float.md#class_float) | [get_line_ascent](class_textparagraph.md#class_TextParagraph_method_get_line_ascent) ( line: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_line_count](class_textparagraph.md#class_TextParagraph_method_get_line_count) ( ) const |
| [float](class_float.md#class_float) | [get_line_descent](class_textparagraph.md#class_TextParagraph_method_get_line_descent) ( line: [int](class_int.md#class_int) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_line_object_rect](class_textparagraph.md#class_TextParagraph_method_get_line_object_rect) ( line: [int](class_int.md#class_int), key: [Variant](class_variant.md#class_Variant) ) const |
| [Array](class_array.md#class_Array) | [get_line_objects](class_textparagraph.md#class_TextParagraph_method_get_line_objects) ( line: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_line_range](class_textparagraph.md#class_TextParagraph_method_get_line_range) ( line: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [get_line_rid](class_textparagraph.md#class_TextParagraph_method_get_line_rid) ( line: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_line_size](class_textparagraph.md#class_TextParagraph_method_get_line_size) ( line: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_line_underline_position](class_textparagraph.md#class_TextParagraph_method_get_line_underline_position) ( line: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_line_underline_thickness](class_textparagraph.md#class_TextParagraph_method_get_line_underline_thickness) ( line: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_line_width](class_textparagraph.md#class_TextParagraph_method_get_line_width) ( line: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_non_wrapped_size](class_textparagraph.md#class_TextParagraph_method_get_non_wrapped_size) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_range](class_textparagraph.md#class_TextParagraph_method_get_range) ( ) const |
| [RID](class_rid.md#class_RID) | [get_rid](class_textparagraph.md#class_TextParagraph_method_get_rid) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_size](class_textparagraph.md#class_TextParagraph_method_get_size) ( ) const |
| [bool](class_bool.md#class_bool) | [has_object](class_textparagraph.md#class_TextParagraph_method_has_object) ( key: [Variant](class_variant.md#class_Variant) ) const |
| [int](class_int.md#class_int) | [hit_test](class_textparagraph.md#class_TextParagraph_method_hit_test) ( coords: [Vector2](class_vector2.md#class_Vector2) ) const |
| [bool](class_bool.md#class_bool) | [resize_object](class_textparagraph.md#class_TextParagraph_method_resize_object) ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, baseline: [float](class_float.md#class_float) = 0.0 ) |
| void | [set_bidi_override](class_textparagraph.md#class_TextParagraph_method_set_bidi_override) ( override: [Array](class_array.md#class_Array) ) |
| [bool](class_bool.md#class_bool) | [set_dropcap](class_textparagraph.md#class_TextParagraph_method_set_dropcap) ( text: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int), dropcap_margins: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), language: [String](class_string.md#class_String) = "" ) |
| void | [tab_align](class_textparagraph.md#class_TextParagraph_method_tab_align) ( tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |

---

### Property Descriptions

<span id="class_TextParagraph_property_alignment"></span>

HorizontalAlignment **alignment** = `0` [🔗](class_textparagraph.md#class_TextParagraph_property_alignment)

- void **set_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_alignment** ( )

Paragraph horizontal alignment.

---

<span id="class_TextParagraph_property_break_flags"></span>

*BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **break_flags** = `3` [🔗](class_textparagraph.md#class_TextParagraph_property_break_flags)

- void **set_break_flags** ( value: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] )
- *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **get_break_flags** ( )

Line breaking rules. For more info see [TextServer](class_textserver.md#class_TextServer).

---

<span id="class_TextParagraph_property_custom_punctuation"></span>

[String](class_string.md#class_String) **custom_punctuation** = `""` [🔗](class_textparagraph.md#class_TextParagraph_property_custom_punctuation)

- void **set_custom_punctuation** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_custom_punctuation** ( )

Custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

<span id="class_TextParagraph_property_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **direction** = `0` [🔗](class_textparagraph.md#class_TextParagraph_property_direction)

- void **set_direction** ( value: [Direction](class_textserver.md#enum_TextServer_Direction) )
- [Direction](class_textserver.md#enum_TextServer_Direction) **get_direction** ( )

Text writing direction.

---

<span id="class_TextParagraph_property_ellipsis_char"></span>

[String](class_string.md#class_String) **ellipsis_char** = `"…"` [🔗](class_textparagraph.md#class_TextParagraph_property_ellipsis_char)

- void **set_ellipsis_char** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_ellipsis_char** ( )

Ellipsis character used for text clipping.

---

<span id="class_TextParagraph_property_justification_flags"></span>

*BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **justification_flags** = `163` [🔗](class_textparagraph.md#class_TextParagraph_property_justification_flags)

- void **set_justification_flags** ( value: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] )
- *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **get_justification_flags** ( )

Line fill alignment rules.

---

<span id="class_TextParagraph_property_line_spacing"></span>

[float](class_float.md#class_float) **line_spacing** = `0.0` [🔗](class_textparagraph.md#class_TextParagraph_property_line_spacing)

- void **set_line_spacing** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_line_spacing** ( )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_TextParagraph_property_max_lines_visible"></span>

[int](class_int.md#class_int) **max_lines_visible** = `-1` [🔗](class_textparagraph.md#class_TextParagraph_property_max_lines_visible)

- void **set_max_lines_visible** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_lines_visible** ( )

Limits the lines of text shown.

---

<span id="class_TextParagraph_property_orientation"></span>

[Orientation](class_textserver.md#enum_TextServer_Orientation) **orientation** = `0` [🔗](class_textparagraph.md#class_TextParagraph_property_orientation)

- void **set_orientation** ( value: [Orientation](class_textserver.md#enum_TextServer_Orientation) )
- [Orientation](class_textserver.md#enum_TextServer_Orientation) **get_orientation** ( )

Text orientation.

---

<span id="class_TextParagraph_property_preserve_control"></span>

[bool](class_bool.md#class_bool) **preserve_control** = `false` [🔗](class_textparagraph.md#class_TextParagraph_property_preserve_control)

- void **set_preserve_control** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_preserve_control** ( )

If set to `true` text will display control characters.

---

<span id="class_TextParagraph_property_preserve_invalid"></span>

[bool](class_bool.md#class_bool) **preserve_invalid** = `true` [🔗](class_textparagraph.md#class_TextParagraph_property_preserve_invalid)

- void **set_preserve_invalid** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_preserve_invalid** ( )

If set to `true` text will display invalid characters.

---

<span id="class_TextParagraph_property_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **text_overrun_behavior** = `0` [🔗](class_textparagraph.md#class_TextParagraph_property_text_overrun_behavior)

- void **set_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( )

The clipping behavior when the text exceeds the paragraph's set width.

---

<span id="class_TextParagraph_property_width"></span>

[float](class_float.md#class_float) **width** = `-1.0` [🔗](class_textparagraph.md#class_TextParagraph_property_width)

- void **set_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_width** ( )

Paragraph width.

---

### Method Descriptions

<span id="class_TextParagraph_method_add_object"></span>

[bool](class_bool.md#class_bool) **add_object** ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, length: [int](class_int.md#class_int) = 1, baseline: [float](class_float.md#class_float) = 0.0 ) [🔗](class_textparagraph.md#class_TextParagraph_method_add_object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

<span id="class_TextParagraph_method_add_string"></span>

[bool](class_bool.md#class_bool) **add_string** ( text: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int), language: [String](class_string.md#class_String) = "", meta: [Variant](class_variant.md#class_Variant) = null ) [🔗](class_textparagraph.md#class_TextParagraph_method_add_string)

Adds text span and font to draw it.

---

<span id="class_TextParagraph_method_clear"></span>

void **clear** ( ) [🔗](class_textparagraph.md#class_TextParagraph_method_clear)

Clears text paragraph (removes text and inline objects).

---

<span id="class_TextParagraph_method_clear_dropcap"></span>

void **clear_dropcap** ( ) [🔗](class_textparagraph.md#class_TextParagraph_method_clear_dropcap)

Removes dropcap.

---

<span id="class_TextParagraph_method_draw"></span>

void **draw** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_draw)

Draw all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextParagraph_method_draw_dropcap"></span>

void **draw_dropcap** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_draw_dropcap)

Draw drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextParagraph_method_draw_dropcap_outline"></span>

void **draw_dropcap_outline** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_draw_dropcap_outline)

Draw drop cap outline into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextParagraph_method_draw_line"></span>

void **draw_line** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), line: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_draw_line)

Draw single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextParagraph_method_draw_line_outline"></span>

void **draw_line_outline** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), line: [int](class_int.md#class_int), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_draw_line_outline)

Draw outline of the single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextParagraph_method_draw_outline"></span>

void **draw_outline** ( canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_draw_outline)

Draw outlines of all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextParagraph_method_duplicate"></span>

[TextParagraph](class_textparagraph.md#class_TextParagraph) **duplicate** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_duplicate)

Duplicates this **TextParagraph**.

---

<span id="class_TextParagraph_method_get_dropcap_lines"></span>

[int](class_int.md#class_int) **get_dropcap_lines** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_dropcap_lines)

Returns number of lines used by dropcap.

---

<span id="class_TextParagraph_method_get_dropcap_rid"></span>

[RID](class_rid.md#class_RID) **get_dropcap_rid** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_dropcap_rid)

Returns drop cap text buffer RID.

---

<span id="class_TextParagraph_method_get_dropcap_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_dropcap_size** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_dropcap_size)

Returns drop cap bounding box size.

---

<span id="class_TextParagraph_method_get_inferred_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **get_inferred_direction** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_inferred_direction)

Returns the text writing direction inferred by the BiDi algorithm.

---

<span id="class_TextParagraph_method_get_line_ascent"></span>

[float](class_float.md#class_float) **get_line_ascent** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_ascent)

Returns the text line ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---

<span id="class_TextParagraph_method_get_line_count"></span>

[int](class_int.md#class_int) **get_line_count** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_count)

Returns number of lines in the paragraph.

---

<span id="class_TextParagraph_method_get_line_descent"></span>

[float](class_float.md#class_float) **get_line_descent** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_descent)

Returns the text line descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---

<span id="class_TextParagraph_method_get_line_object_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_line_object_rect** ( line: [int](class_int.md#class_int), key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_object_rect)

Returns bounding rectangle of the inline object.

---

<span id="class_TextParagraph_method_get_line_objects"></span>

[Array](class_array.md#class_Array) **get_line_objects** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_objects)

Returns array of inline objects in the line.

---

<span id="class_TextParagraph_method_get_line_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_line_range** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_range)

Returns character range of the line.

---

<span id="class_TextParagraph_method_get_line_rid"></span>

[RID](class_rid.md#class_RID) **get_line_rid** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_rid)

Returns TextServer line buffer RID.

---

<span id="class_TextParagraph_method_get_line_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_line_size** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_size)

Returns size of the bounding box of the line of text. Returned size is rounded up.

---

<span id="class_TextParagraph_method_get_line_underline_position"></span>

[float](class_float.md#class_float) **get_line_underline_position** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_underline_position)

Returns pixel offset of the underline below the baseline.

---

<span id="class_TextParagraph_method_get_line_underline_thickness"></span>

[float](class_float.md#class_float) **get_line_underline_thickness** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_underline_thickness)

Returns thickness of the underline.

---

<span id="class_TextParagraph_method_get_line_width"></span>

[float](class_float.md#class_float) **get_line_width** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_line_width)

Returns width (for horizontal layout) or height (for vertical) of the line of text.

---

<span id="class_TextParagraph_method_get_non_wrapped_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_non_wrapped_size** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_non_wrapped_size)

Returns the size of the bounding box of the paragraph, without line breaks.

---

<span id="class_TextParagraph_method_get_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_range** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_range)

Returns the character range of the paragraph.

---

<span id="class_TextParagraph_method_get_rid"></span>

[RID](class_rid.md#class_RID) **get_rid** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_rid)

Returns TextServer full string buffer RID.

---

<span id="class_TextParagraph_method_get_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_size** ( ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_get_size)

Returns the size of the bounding box of the paragraph.

---

<span id="class_TextParagraph_method_has_object"></span>

[bool](class_bool.md#class_bool) **has_object** ( key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_has_object)

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---

<span id="class_TextParagraph_method_hit_test"></span>

[int](class_int.md#class_int) **hit_test** ( coords: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_textparagraph.md#class_TextParagraph_method_hit_test)

Returns caret character offset at the specified coordinates. This function always returns a valid position.

---

<span id="class_TextParagraph_method_resize_object"></span>

[bool](class_bool.md#class_bool) **resize_object** ( key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, baseline: [float](class_float.md#class_float) = 0.0 ) [🔗](class_textparagraph.md#class_TextParagraph_method_resize_object)

Sets new size and alignment of embedded object.

---

<span id="class_TextParagraph_method_set_bidi_override"></span>

void **set_bidi_override** ( override: [Array](class_array.md#class_Array) ) [🔗](class_textparagraph.md#class_TextParagraph_method_set_bidi_override)

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---

<span id="class_TextParagraph_method_set_dropcap"></span>

[bool](class_bool.md#class_bool) **set_dropcap** ( text: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int), dropcap_margins: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), language: [String](class_string.md#class_String) = "" ) [🔗](class_textparagraph.md#class_TextParagraph_method_set_dropcap)

Sets drop cap, overrides previously set drop cap. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.

---

<span id="class_TextParagraph_method_tab_align"></span>

void **tab_align** ( tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_textparagraph.md#class_TextParagraph_method_tab_align)

Aligns paragraph to the given tab-stops.
