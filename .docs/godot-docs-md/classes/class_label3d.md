.. meta::
	:keywords: text

<span id="class_Label3D"></span>

## Label3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node for displaying plain text in 3D space.

### Description

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.

### Tutorials

- [3D text](../tutorials/3d/3d_text.md)

### Properties


| [float](class_float.md#class_float) | [alpha_antialiasing_edge](class_label3d.md#class_Label3D_property_alpha_antialiasing_edge) | `0.0` |
| --- | --- | --- |
| [AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) | [alpha_antialiasing_mode](class_label3d.md#class_Label3D_property_alpha_antialiasing_mode) | `0` |
| [AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) | [alpha_cut](class_label3d.md#class_Label3D_property_alpha_cut) | `0` |
| [float](class_float.md#class_float) | [alpha_hash_scale](class_label3d.md#class_Label3D_property_alpha_hash_scale) | `1.0` |
| [float](class_float.md#class_float) | [alpha_scissor_threshold](class_label3d.md#class_Label3D_property_alpha_scissor_threshold) | `0.5` |
| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [autowrap_mode](class_label3d.md#class_Label3D_property_autowrap_mode) | `0` |
| bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] | [autowrap_trim_flags](class_label3d.md#class_Label3D_property_autowrap_trim_flags) | `192` |
| [BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) | [billboard](class_label3d.md#class_Label3D_property_billboard) | `0` |
| [ShadowCastingSetting](class_geometryinstance3d.md#enum_GeometryInstance3D_ShadowCastingSetting) | cast_shadow | `0` (overrides [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D_property_cast_shadow)) |
| [bool](class_bool.md#class_bool) | [double_sided](class_label3d.md#class_Label3D_property_double_sided) | `true` |
| [bool](class_bool.md#class_bool) | [fixed_size](class_label3d.md#class_Label3D_property_fixed_size) | `false` |
| [Font](class_font.md#class_Font) | [font](class_label3d.md#class_Label3D_property_font) |
| [int](class_int.md#class_int) | [font_size](class_label3d.md#class_Label3D_property_font_size) | `32` |
| [GIMode](class_geometryinstance3d.md#enum_GeometryInstance3D_GIMode) | gi_mode | `0` (overrides [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_mode)) |
| HorizontalAlignment | [horizontal_alignment](class_label3d.md#class_Label3D_property_horizontal_alignment) | `1` |
| bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] | [justification_flags](class_label3d.md#class_Label3D_property_justification_flags) | `163` |
| [String](class_string.md#class_String) | [language](class_label3d.md#class_Label3D_property_language) | `""` |
| [float](class_float.md#class_float) | [line_spacing](class_label3d.md#class_Label3D_property_line_spacing) | `0.0` |
| [Color](class_color.md#class_Color) | [modulate](class_label3d.md#class_Label3D_property_modulate) | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class_bool) | [no_depth_test](class_label3d.md#class_Label3D_property_no_depth_test) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [offset](class_label3d.md#class_Label3D_property_offset) | `Vector2(0, 0)` |
| [Color](class_color.md#class_Color) | [outline_modulate](class_label3d.md#class_Label3D_property_outline_modulate) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class_int) | [outline_render_priority](class_label3d.md#class_Label3D_property_outline_render_priority) | `-1` |
| [int](class_int.md#class_int) | [outline_size](class_label3d.md#class_Label3D_property_outline_size) | `12` |
| [float](class_float.md#class_float) | [pixel_size](class_label3d.md#class_Label3D_property_pixel_size) | `0.005` |
| [int](class_int.md#class_int) | [render_priority](class_label3d.md#class_Label3D_property_render_priority) | `0` |
| [bool](class_bool.md#class_bool) | [shaded](class_label3d.md#class_Label3D_property_shaded) | `false` |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_label3d.md#class_Label3D_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_label3d.md#class_Label3D_property_structured_text_bidi_override_options) | `[]` |
| [String](class_string.md#class_String) | [text](class_label3d.md#class_Label3D_property_text) | `""` |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [text_direction](class_label3d.md#class_Label3D_property_text_direction) | `0` |
| [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) | [texture_filter](class_label3d.md#class_Label3D_property_texture_filter) | `3` |
| [bool](class_bool.md#class_bool) | [uppercase](class_label3d.md#class_Label3D_property_uppercase) | `false` |
| VerticalAlignment | [vertical_alignment](class_label3d.md#class_Label3D_property_vertical_alignment) | `1` |
| [float](class_float.md#class_float) | [width](class_label3d.md#class_Label3D_property_width) | `500.0` |

### Methods


| [TriangleMesh](class_trianglemesh.md#class_TriangleMesh) | [generate_triangle_mesh](class_label3d.md#class_Label3D_method_generate_triangle_mesh) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_draw_flag](class_label3d.md#class_Label3D_method_get_draw_flag) ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) ) const |
| void | [set_draw_flag](class_label3d.md#class_Label3D_method_set_draw_flag) ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags), enabled: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_Label3D_DrawFlags"></span>

enum **DrawFlags**: [🔗](class_label3d.md#enum_Label3D_DrawFlags)

<span id="class_Label3D_constant_FLAG_SHADED"></span>

[DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) **FLAG_SHADED** = `0`

If set, lights in the environment affect the label.

<span id="class_Label3D_constant_FLAG_DOUBLE_SIDED"></span>

[DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) **FLAG_DOUBLE_SIDED** = `1`

If set, text can be seen from the back as well. If not, the text is invisible when looking at it from behind.

<span id="class_Label3D_constant_FLAG_DISABLE_DEPTH_TEST"></span>

[DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) **FLAG_DISABLE_DEPTH_TEST** = `2`

Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.

<span id="class_Label3D_constant_FLAG_FIXED_SIZE"></span>

[DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) **FLAG_FIXED_SIZE** = `3`

Label is scaled by depth so that it always appears the same size on screen.

<span id="class_Label3D_constant_FLAG_MAX"></span>

[DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) **FLAG_MAX** = `4`

Represents the size of the [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) enum.

---

<span id="enum_Label3D_AlphaCutMode"></span>

enum **AlphaCutMode**: [🔗](class_label3d.md#enum_Label3D_AlphaCutMode)

<span id="class_Label3D_constant_ALPHA_CUT_DISABLED"></span>

[AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping. [GeometryInstance3D.cast_shadow](class_geometryinstance3d.md#class_GeometryInstance3D_property_cast_shadow) has no effect when this transparency mode is used; the **Label3D** will never cast shadows.

<span id="class_Label3D_constant_ALPHA_CUT_DISCARD"></span>

[AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (see ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa). This mode is also known as *alpha testing* or *1-bit transparency*.

 **Note:** This mode might have issues with anti-aliased fonts and outlines, try adjusting [alpha_scissor_threshold](class_label3d.md#class_Label3D_property_alpha_scissor_threshold) or using MSDF font.

 **Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.

<span id="class_Label3D_constant_ALPHA_CUT_OPAQUE_PREPASS"></span>

[AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower than [ALPHA_CUT_DISABLED](class_label3d.md#class_Label3D_constant_ALPHA_CUT_DISABLED) or [ALPHA_CUT_DISCARD](class_label3d.md#class_Label3D_constant_ALPHA_CUT_DISCARD), but it allows displaying translucent areas and smooth edges while using proper sorting.

 **Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.

<span id="class_Label3D_constant_ALPHA_CUT_HASH"></span>

[AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) **ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic threshold, the rest will remain opaque.

---

### Property Descriptions

<span id="class_Label3D_property_alpha_antialiasing_edge"></span>

[float](class_float.md#class_float) **alpha_antialiasing_edge** = `0.0` [🔗](class_label3d.md#class_Label3D_property_alpha_antialiasing_edge)

- void **set_alpha_antialiasing_edge** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_alpha_antialiasing_edge** ( )

Threshold at which antialiasing will be applied on the alpha channel.

---

<span id="class_Label3D_property_alpha_antialiasing_mode"></span>

[AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **alpha_antialiasing_mode** = `0` [🔗](class_label3d.md#class_Label3D_property_alpha_antialiasing_mode)

- void **set_alpha_antialiasing** ( value: [AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) )
- [AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **get_alpha_antialiasing** ( )

The type of alpha antialiasing to apply.

---

<span id="class_Label3D_property_alpha_cut"></span>

[AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) **alpha_cut** = `0` [🔗](class_label3d.md#class_Label3D_property_alpha_cut)

- void **set_alpha_cut_mode** ( value: [AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) )
- [AlphaCutMode](class_label3d.md#enum_Label3D_AlphaCutMode) **get_alpha_cut_mode** ( )

The alpha cutting mode to use for the sprite.

---

<span id="class_Label3D_property_alpha_hash_scale"></span>

[float](class_float.md#class_float) **alpha_hash_scale** = `1.0` [🔗](class_label3d.md#class_Label3D_property_alpha_hash_scale)

- void **set_alpha_hash_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_alpha_hash_scale** ( )

The hashing scale for Alpha Hash. Recommended values between `0` and `2`.

---

<span id="class_Label3D_property_alpha_scissor_threshold"></span>

[float](class_float.md#class_float) **alpha_scissor_threshold** = `0.5` [🔗](class_label3d.md#class_Label3D_property_alpha_scissor_threshold)

- void **set_alpha_scissor_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_alpha_scissor_threshold** ( )

Threshold at which the alpha scissor will discard values.

---

<span id="class_Label3D_property_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **autowrap_mode** = `0` [🔗](class_label3d.md#class_Label3D_property_autowrap_mode)

- void **set_autowrap_mode** ( value: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) )
- [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( )

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

---

<span id="class_Label3D_property_autowrap_trim_flags"></span>

*BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **autowrap_trim_flags** = `192` [🔗](class_label3d.md#class_Label3D_property_autowrap_trim_flags)

- void **set_autowrap_trim_flags** ( value: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] )
- *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **get_autowrap_trim_flags** ( )

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES) for more info.

---

<span id="class_Label3D_property_billboard"></span>

[BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **billboard** = `0` [🔗](class_label3d.md#class_Label3D_property_billboard)

- void **set_billboard_mode** ( value: [BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) )
- [BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **get_billboard_mode** ( )

The billboard mode to use for the label.

---

<span id="class_Label3D_property_double_sided"></span>

[bool](class_bool.md#class_bool) **double_sided** = `true` [🔗](class_label3d.md#class_Label3D_property_double_sided)

- void **set_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) ) *const*

If `true`, text can be seen from the back as well, if `false`, it is invisible when looking at it from behind.

---

<span id="class_Label3D_property_fixed_size"></span>

[bool](class_bool.md#class_bool) **fixed_size** = `false` [🔗](class_label3d.md#class_Label3D_property_fixed_size)

- void **set_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) ) *const*

If `true`, the label is rendered at the same size regardless of distance. The label's size on screen is the same as if the camera was `1.0` units away from the label's origin, regardless of the actual distance from the camera. The [Camera3D](class_camera3d.md#class_Camera3D)'s field of view (or [Camera3D.size](class_camera3d.md#class_Camera3D_property_size) when in orthogonal/frustum mode) still affects the size the label is drawn at.

---

<span id="class_Label3D_property_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_label3d.md#class_Label3D_property_font)

- void **set_font** ( value: [Font](class_font.md#class_Font) )
- [Font](class_font.md#class_Font) **get_font** ( )

Font configuration used to display text.

---

<span id="class_Label3D_property_font_size"></span>

[int](class_int.md#class_int) **font_size** = `32` [🔗](class_label3d.md#class_Label3D_property_font_size)

- void **set_font_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_font_size** ( )

Font size of the **Label3D**'s text. To make the font look more detailed when up close, increase [font_size](class_label3d.md#class_Label3D_property_font_size) while decreasing [pixel_size](class_label3d.md#class_Label3D_property_pixel_size) at the same time.

Higher font sizes require more time to render new characters, which can cause stuttering during gameplay.

---

<span id="class_Label3D_property_horizontal_alignment"></span>

HorizontalAlignment **horizontal_alignment** = `1` [🔗](class_label3d.md#class_Label3D_property_horizontal_alignment)

- void **set_horizontal_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_horizontal_alignment** ( )

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

<span id="class_Label3D_property_justification_flags"></span>

*BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **justification_flags** = `163` [🔗](class_label3d.md#class_Label3D_property_justification_flags)

- void **set_justification_flags** ( value: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] )
- *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **get_justification_flags** ( )

Line fill alignment rules.

---

<span id="class_Label3D_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_label3d.md#class_Label3D_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_Label3D_property_line_spacing"></span>

[float](class_float.md#class_float) **line_spacing** = `0.0` [🔗](class_label3d.md#class_Label3D_property_line_spacing)

- void **set_line_spacing** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_line_spacing** ( )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_Label3D_property_modulate"></span>

[Color](class_color.md#class_Color) **modulate** = `Color(1, 1, 1, 1)` [🔗](class_label3d.md#class_Label3D_property_modulate)

- void **set_modulate** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_modulate** ( )

Text [Color](class_color.md#class_Color) of the **Label3D**.

---

<span id="class_Label3D_property_no_depth_test"></span>

[bool](class_bool.md#class_bool) **no_depth_test** = `false` [🔗](class_label3d.md#class_Label3D_property_no_depth_test)

- void **set_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) ) *const*

If `true`, depth testing is disabled and the object will be drawn in render order.

---

<span id="class_Label3D_property_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **offset** = `Vector2(0, 0)` [🔗](class_label3d.md#class_Label3D_property_offset)

- void **set_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_offset** ( )

The text drawing offset (in pixels).

---

<span id="class_Label3D_property_outline_modulate"></span>

[Color](class_color.md#class_Color) **outline_modulate** = `Color(0, 0, 0, 1)` [🔗](class_label3d.md#class_Label3D_property_outline_modulate)

- void **set_outline_modulate** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_outline_modulate** ( )

The tint of text outline.

---

<span id="class_Label3D_property_outline_render_priority"></span>

[int](class_int.md#class_int) **outline_render_priority** = `-1` [🔗](class_label3d.md#class_Label3D_property_outline_render_priority)

- void **set_outline_render_priority** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_outline_render_priority** ( )

Sets the render priority for the text outline. Higher priority objects will be sorted in front of lower priority objects.

 **Note:** This only applies if [alpha_cut](class_label3d.md#class_Label3D_property_alpha_cut) is set to [ALPHA_CUT_DISABLED](class_label3d.md#class_Label3D_constant_ALPHA_CUT_DISABLED) (default value).

 **Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---

<span id="class_Label3D_property_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `12` [🔗](class_label3d.md#class_Label3D_property_outline_size)

- void **set_outline_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_outline_size** ( )

Text outline size.

---

<span id="class_Label3D_property_pixel_size"></span>

[float](class_float.md#class_float) **pixel_size** = `0.005` [🔗](class_label3d.md#class_Label3D_property_pixel_size)

- void **set_pixel_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pixel_size** ( )

The size of one pixel's width on the label to scale it in 3D. To make the font look more detailed when up close, increase [font_size](class_label3d.md#class_Label3D_property_font_size) while decreasing [pixel_size](class_label3d.md#class_Label3D_property_pixel_size) at the same time.

---

<span id="class_Label3D_property_render_priority"></span>

[int](class_int.md#class_int) **render_priority** = `0` [🔗](class_label3d.md#class_Label3D_property_render_priority)

- void **set_render_priority** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_render_priority** ( )

Sets the render priority for the text. Higher priority objects will be sorted in front of lower priority objects.

 **Note:** This only applies if [alpha_cut](class_label3d.md#class_Label3D_property_alpha_cut) is set to [ALPHA_CUT_DISABLED](class_label3d.md#class_Label3D_constant_ALPHA_CUT_DISABLED) (default value).

 **Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---

<span id="class_Label3D_property_shaded"></span>

[bool](class_bool.md#class_bool) **shaded** = `false` [🔗](class_label3d.md#class_Label3D_property_shaded)

- void **set_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) ) *const*

If `true`, the [Light3D](class_light3d.md#class_Light3D) in the [Environment](class_environment.md#class_Environment) has effects on the label.

---

<span id="class_Label3D_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_label3d.md#class_Label3D_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_Label3D_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_label3d.md#class_Label3D_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_Label3D_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_label3d.md#class_Label3D_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The text to display on screen.

---

<span id="class_Label3D_property_text_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **text_direction** = `0` [🔗](class_label3d.md#class_Label3D_property_text_direction)

- void **set_text_direction** ( value: [Direction](class_textserver.md#enum_TextServer_Direction) )
- [Direction](class_textserver.md#enum_TextServer_Direction) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_Label3D_property_texture_filter"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **texture_filter** = `3` [🔗](class_label3d.md#class_Label3D_property_texture_filter)

- void **set_texture_filter** ( value: [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) )
- [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **get_texture_filter** ( )

Filter flags for the texture.

---

<span id="class_Label3D_property_uppercase"></span>

[bool](class_bool.md#class_bool) **uppercase** = `false` [🔗](class_label3d.md#class_Label3D_property_uppercase)

- void **set_uppercase** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_uppercase** ( )

If `true`, all the text displays as UPPERCASE.

---

<span id="class_Label3D_property_vertical_alignment"></span>

VerticalAlignment **vertical_alignment** = `1` [🔗](class_label3d.md#class_Label3D_property_vertical_alignment)

- void **set_vertical_alignment** ( value: VerticalAlignment )
- VerticalAlignment **get_vertical_alignment** ( )

Controls the text's vertical alignment. Supports top, center, and bottom.

---

<span id="class_Label3D_property_width"></span>

[float](class_float.md#class_float) **width** = `500.0` [🔗](class_label3d.md#class_Label3D_property_width)

- void **set_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_width** ( )

Text width (in pixels), used for autowrap and fill alignment.

---

### Method Descriptions

<span id="class_Label3D_method_generate_triangle_mesh"></span>

[TriangleMesh](class_trianglemesh.md#class_TriangleMesh) **generate_triangle_mesh** ( ) *const* [🔗](class_label3d.md#class_Label3D_method_generate_triangle_mesh)

Returns a [TriangleMesh](class_trianglemesh.md#class_TriangleMesh) with the label's vertices following its current configuration (such as its [pixel_size](class_label3d.md#class_Label3D_property_pixel_size)).

---

<span id="class_Label3D_method_get_draw_flag"></span>

[bool](class_bool.md#class_bool) **get_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags) ) *const* [🔗](class_label3d.md#class_Label3D_method_get_draw_flag)

Returns the value of the specified flag.

---

<span id="class_Label3D_method_set_draw_flag"></span>

void **set_draw_flag** ( flag: [DrawFlags](class_label3d.md#enum_Label3D_DrawFlags), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_label3d.md#class_Label3D_method_set_draw_flag)

If `true`, the specified `flag` will be enabled.
