<span id="class_TextMesh"></span>

## TextMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Generate a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) from the text.

### Description

Generate a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) from the text.

TextMesh can be generated only when using dynamic fonts with vector glyph contours. Bitmap fonts (including bitmap data in the TrueType/OpenType containers, like color emoji fonts) are not supported.

The UV layout is arranged in 4 horizontal strips, top to bottom: 40% of the height for the front face, 40% for the back face, 10% for the outer edges and 10% for the inner edges.

### Tutorials

- [3D text](../tutorials/3d/3d_text.md)

### Properties


| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [autowrap_mode](class_textmesh.md#class_TextMesh_property_autowrap_mode) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [curve_step](class_textmesh.md#class_TextMesh_property_curve_step) | `0.5` |
| [float](class_float.md#class_float) | [depth](class_textmesh.md#class_TextMesh_property_depth) | `0.05` |
| [Font](class_font.md#class_Font) | [font](class_textmesh.md#class_TextMesh_property_font) |
| [int](class_int.md#class_int) | [font_size](class_textmesh.md#class_TextMesh_property_font_size) | `16` |
| HorizontalAlignment | [horizontal_alignment](class_textmesh.md#class_TextMesh_property_horizontal_alignment) | `1` |
| bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] | [justification_flags](class_textmesh.md#class_TextMesh_property_justification_flags) | `163` |
| [String](class_string.md#class_String) | [language](class_textmesh.md#class_TextMesh_property_language) | `""` |
| [float](class_float.md#class_float) | [line_spacing](class_textmesh.md#class_TextMesh_property_line_spacing) | `0.0` |
| [Vector2](class_vector2.md#class_Vector2) | [offset](class_textmesh.md#class_TextMesh_property_offset) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [pixel_size](class_textmesh.md#class_TextMesh_property_pixel_size) | `0.01` |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_textmesh.md#class_TextMesh_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_textmesh.md#class_TextMesh_property_structured_text_bidi_override_options) | `[]` |
| [String](class_string.md#class_String) | [text](class_textmesh.md#class_TextMesh_property_text) | `""` |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [text_direction](class_textmesh.md#class_TextMesh_property_text_direction) | `0` |
| [bool](class_bool.md#class_bool) | [uppercase](class_textmesh.md#class_TextMesh_property_uppercase) | `false` |
| VerticalAlignment | [vertical_alignment](class_textmesh.md#class_TextMesh_property_vertical_alignment) | `1` |
| [float](class_float.md#class_float) | [width](class_textmesh.md#class_TextMesh_property_width) | `500.0` |

---

### Property Descriptions

<span id="class_TextMesh_property_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **autowrap_mode** = `0` [🔗](class_textmesh.md#class_TextMesh_property_autowrap_mode)

- void **set_autowrap_mode** ( value: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) )
- [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( )

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

---

<span id="class_TextMesh_property_curve_step"></span>

[float](class_float.md#class_float) **curve_step** = `0.5` [🔗](class_textmesh.md#class_TextMesh_property_curve_step)

- void **set_curve_step** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_curve_step** ( )

Step (in pixels) used to approximate Bézier curves. Lower values result in smoother curves, but is slower to generate and render. Consider adjusting this according to the font size and the typical viewing distance.

 **Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts.

---

<span id="class_TextMesh_property_depth"></span>

[float](class_float.md#class_float) **depth** = `0.05` [🔗](class_textmesh.md#class_TextMesh_property_depth)

- void **set_depth** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth** ( )

Depths of the mesh, if set to `0.0` only front surface, is generated, and UV layout is changed to use full texture for the front face only.

---

<span id="class_TextMesh_property_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_textmesh.md#class_TextMesh_property_font)

- void **set_font** ( value: [Font](class_font.md#class_Font) )
- [Font](class_font.md#class_Font) **get_font** ( )

Font configuration used to display text.

---

<span id="class_TextMesh_property_font_size"></span>

[int](class_int.md#class_int) **font_size** = `16` [🔗](class_textmesh.md#class_TextMesh_property_font_size)

- void **set_font_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_font_size** ( )

Font size of the **TextMesh**'s text. This property works in tandem with [pixel_size](class_textmesh.md#class_TextMesh_property_pixel_size). Higher values will result in a more detailed font, regardless of [curve_step](class_textmesh.md#class_TextMesh_property_curve_step) and [pixel_size](class_textmesh.md#class_TextMesh_property_pixel_size). Consider keeping this value below 63 (inclusive) for good performance, and adjust [pixel_size](class_textmesh.md#class_TextMesh_property_pixel_size) as needed to enlarge text.

 **Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's [Node3D.scale](class_node3d.md#class_Node3D_property_scale) instead.

---

<span id="class_TextMesh_property_horizontal_alignment"></span>

HorizontalAlignment **horizontal_alignment** = `1` [🔗](class_textmesh.md#class_TextMesh_property_horizontal_alignment)

- void **set_horizontal_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_horizontal_alignment** ( )

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

<span id="class_TextMesh_property_justification_flags"></span>

*BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **justification_flags** = `163` [🔗](class_textmesh.md#class_TextMesh_property_justification_flags)

- void **set_justification_flags** ( value: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] )
- *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **get_justification_flags** ( )

Line fill alignment rules.

---

<span id="class_TextMesh_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_textmesh.md#class_TextMesh_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_TextMesh_property_line_spacing"></span>

[float](class_float.md#class_float) **line_spacing** = `0.0` [🔗](class_textmesh.md#class_TextMesh_property_line_spacing)

- void **set_line_spacing** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_line_spacing** ( )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_TextMesh_property_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **offset** = `Vector2(0, 0)` [🔗](class_textmesh.md#class_TextMesh_property_offset)

- void **set_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_offset** ( )

The text drawing offset (in pixels).

 **Note:** Changing this property will regenerate the mesh, which is a slow operation. To change the text's position in real-time efficiently, change the node's [Node3D.position](class_node3d.md#class_Node3D_property_position) instead.

---

<span id="class_TextMesh_property_pixel_size"></span>

[float](class_float.md#class_float) **pixel_size** = `0.01` [🔗](class_textmesh.md#class_TextMesh_property_pixel_size)

- void **set_pixel_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pixel_size** ( )

The size of one pixel's width on the text to scale it in 3D. This property works in tandem with [font_size](class_textmesh.md#class_TextMesh_property_font_size).

 **Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's [Node3D.scale](class_node3d.md#class_Node3D_property_scale) instead.

---

<span id="class_TextMesh_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_textmesh.md#class_TextMesh_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_TextMesh_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_textmesh.md#class_TextMesh_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_TextMesh_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_textmesh.md#class_TextMesh_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The text to generate mesh from.

 **Note:** Due to being a [Resource](class_resource.md#class_Resource), it doesn't follow the rules of [Node.auto_translate_mode](class_node.md#class_Node_property_auto_translate_mode). If disabling translation is desired, it should be done manually with [Object.set_message_translation()](class_object.md#class_Object_method_set_message_translation).

---

<span id="class_TextMesh_property_text_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **text_direction** = `0` [🔗](class_textmesh.md#class_TextMesh_property_text_direction)

- void **set_text_direction** ( value: [Direction](class_textserver.md#enum_TextServer_Direction) )
- [Direction](class_textserver.md#enum_TextServer_Direction) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_TextMesh_property_uppercase"></span>

[bool](class_bool.md#class_bool) **uppercase** = `false` [🔗](class_textmesh.md#class_TextMesh_property_uppercase)

- void **set_uppercase** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_uppercase** ( )

If `true`, all the text displays as UPPERCASE.

---

<span id="class_TextMesh_property_vertical_alignment"></span>

VerticalAlignment **vertical_alignment** = `1` [🔗](class_textmesh.md#class_TextMesh_property_vertical_alignment)

- void **set_vertical_alignment** ( value: VerticalAlignment )
- VerticalAlignment **get_vertical_alignment** ( )

Controls the text's vertical alignment. Supports top, center, and bottom.

---

<span id="class_TextMesh_property_width"></span>

[float](class_float.md#class_float) **width** = `500.0` [🔗](class_textmesh.md#class_TextMesh_property_width)

- void **set_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_width** ( )

Text width (in pixels), used for fill alignment.
