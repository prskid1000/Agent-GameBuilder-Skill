<span id="class_TextServer"></span>

## TextServer

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [TextServerExtension](class_textserverextension.md#class_TextServerExtension)

A server interface for font management and text rendering.

### Description

**TextServer** is the API backend for managing fonts and rendering text.

 **Note:** This is a low-level API, consider using [TextLine](class_textline.md#class_TextLine), [TextParagraph](class_textparagraph.md#class_TextParagraph), and [Font](class_font.md#class_Font) classes instead.

This is an abstract class, so to get the currently active **TextServer** instance, use the following code:

.. tabs::

```
```

    var ts = TextServerManager.get_primary_interface()

```
```

    var ts = TextServerManager.GetPrimaryInterface();

### Methods


| [RID](class_rid.md#class_RID) | [create_font](class_textserver.md#class_TextServer_method_create_font) ( ) |
| --- | --- |
| [RID](class_rid.md#class_RID) | [create_font_linked_variation](class_textserver.md#class_TextServer_method_create_font_linked_variation) ( font_rid: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [create_shaped_text](class_textserver.md#class_TextServer_method_create_shaped_text) ( direction: [Direction](class_textserver.md#enum_TextServer_Direction) = 0, orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) = 0 ) |
| void | [draw_hex_code_box](class_textserver.md#class_TextServer_method_draw_hex_code_box) ( canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) const |
| void | [font_clear_glyphs](class_textserver.md#class_TextServer_method_font_clear_glyphs) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [font_clear_kerning_map](class_textserver.md#class_TextServer_method_font_clear_kerning_map) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) |
| void | [font_clear_size_cache](class_textserver.md#class_TextServer_method_font_clear_size_cache) ( font_rid: [RID](class_rid.md#class_RID) ) |
| void | [font_clear_system_fallback_cache](class_textserver.md#class_TextServer_method_font_clear_system_fallback_cache) ( ) |
| void | [font_clear_textures](class_textserver.md#class_TextServer_method_font_clear_textures) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [font_draw_glyph](class_textserver.md#class_TextServer_method_font_draw_glyph) ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [font_draw_glyph_outline](class_textserver.md#class_TextServer_method_font_draw_glyph_outline) ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), outline_size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| [FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) | [font_get_antialiasing](class_textserver.md#class_TextServer_method_font_get_antialiasing) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [font_get_ascent](class_textserver.md#class_TextServer_method_font_get_ascent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [font_get_baseline_offset](class_textserver.md#class_TextServer_method_font_get_baseline_offset) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_char_from_glyph_index](class_textserver.md#class_TextServer_method_font_get_char_from_glyph_index) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [font_get_descent](class_textserver.md#class_TextServer_method_font_get_descent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [font_get_disable_embedded_bitmaps](class_textserver.md#class_TextServer_method_font_get_disable_embedded_bitmaps) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [font_get_embolden](class_textserver.md#class_TextServer_method_font_get_embolden) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_face_count](class_textserver.md#class_TextServer_method_font_get_face_count) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_face_index](class_textserver.md#class_TextServer_method_font_get_face_index) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_fixed_size](class_textserver.md#class_TextServer_method_font_get_fixed_size) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) | [font_get_fixed_size_scale_mode](class_textserver.md#class_TextServer_method_font_get_fixed_size_scale_mode) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_get_generate_mipmaps](class_textserver.md#class_TextServer_method_font_get_generate_mipmaps) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [font_get_global_oversampling](class_textserver.md#class_TextServer_method_font_get_global_oversampling) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [font_get_glyph_advance](class_textserver.md#class_TextServer_method_font_get_glyph_advance) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [font_get_glyph_contours](class_textserver.md#class_TextServer_method_font_get_glyph_contours) ( font: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [font_get_glyph_index](class_textserver.md#class_TextServer_method_font_get_glyph_index) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), char: [int](class_int.md#class_int), variation_selector: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [font_get_glyph_list](class_textserver.md#class_TextServer_method_font_get_glyph_list) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [font_get_glyph_offset](class_textserver.md#class_TextServer_method_font_get_glyph_offset) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [font_get_glyph_size](class_textserver.md#class_TextServer_method_font_get_glyph_size) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [font_get_glyph_texture_idx](class_textserver.md#class_TextServer_method_font_get_glyph_texture_idx) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [font_get_glyph_texture_rid](class_textserver.md#class_TextServer_method_font_get_glyph_texture_rid) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [font_get_glyph_texture_size](class_textserver.md#class_TextServer_method_font_get_glyph_texture_size) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [font_get_glyph_uv_rect](class_textserver.md#class_TextServer_method_font_get_glyph_uv_rect) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) const |
| [Hinting](class_textserver.md#enum_TextServer_Hinting) | [font_get_hinting](class_textserver.md#class_TextServer_method_font_get_hinting) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_get_keep_rounding_remainders](class_textserver.md#class_TextServer_method_font_get_keep_rounding_remainders) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [font_get_kerning](class_textserver.md#class_TextServer_method_font_get_kerning) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [font_get_kerning_list](class_textserver.md#class_TextServer_method_font_get_kerning_list) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [font_get_language_support_override](class_textserver.md#class_TextServer_method_font_get_language_support_override) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [font_get_language_support_overrides](class_textserver.md#class_TextServer_method_font_get_language_support_overrides) ( font_rid: [RID](class_rid.md#class_RID) ) |
| [int](class_int.md#class_int) | [font_get_msdf_pixel_range](class_textserver.md#class_TextServer_method_font_get_msdf_pixel_range) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_msdf_size](class_textserver.md#class_TextServer_method_font_get_msdf_size) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [String](class_string.md#class_String) | [font_get_name](class_textserver.md#class_TextServer_method_font_get_name) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [font_get_opentype_feature_overrides](class_textserver.md#class_TextServer_method_font_get_opentype_feature_overrides) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [font_get_ot_name_strings](class_textserver.md#class_TextServer_method_font_get_ot_name_strings) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [font_get_oversampling](class_textserver.md#class_TextServer_method_font_get_oversampling) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [font_get_scale](class_textserver.md#class_TextServer_method_font_get_scale) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [font_get_script_support_override](class_textserver.md#class_TextServer_method_font_get_script_support_override) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [font_get_script_support_overrides](class_textserver.md#class_TextServer_method_font_get_script_support_overrides) ( font_rid: [RID](class_rid.md#class_RID) ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [font_get_size_cache_info](class_textserver.md#class_TextServer_method_font_get_size_cache_info) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [font_get_size_cache_list](class_textserver.md#class_TextServer_method_font_get_size_cache_list) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_spacing](class_textserver.md#class_TextServer_method_font_get_spacing) ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) const |
| [int](class_int.md#class_int) | [font_get_stretch](class_textserver.md#class_TextServer_method_font_get_stretch) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| bitfield | \[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] | [font_get_style](class_textserver.md#class_TextServer_method_font_get_style) ( font_rid: [RID](class_rid.md#class_RID) ) | const |
| [String](class_string.md#class_String) | [font_get_style_name](class_textserver.md#class_TextServer_method_font_get_style_name) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) | [font_get_subpixel_positioning](class_textserver.md#class_TextServer_method_font_get_subpixel_positioning) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [String](class_string.md#class_String) | [font_get_supported_chars](class_textserver.md#class_TextServer_method_font_get_supported_chars) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [font_get_supported_glyphs](class_textserver.md#class_TextServer_method_font_get_supported_glyphs) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_texture_count](class_textserver.md#class_TextServer_method_font_get_texture_count) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Image](class_image.md#class_Image) | [font_get_texture_image](class_textserver.md#class_TextServer_method_font_get_texture_image) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [font_get_texture_offsets](class_textserver.md#class_TextServer_method_font_get_texture_offsets) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [font_get_transform](class_textserver.md#class_TextServer_method_font_get_transform) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [font_get_underline_position](class_textserver.md#class_TextServer_method_font_get_underline_position) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [font_get_underline_thickness](class_textserver.md#class_TextServer_method_font_get_underline_thickness) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [font_get_variation_coordinates](class_textserver.md#class_TextServer_method_font_get_variation_coordinates) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [font_get_weight](class_textserver.md#class_TextServer_method_font_get_weight) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_has_char](class_textserver.md#class_TextServer_method_font_has_char) ( font_rid: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [font_is_allow_system_fallback](class_textserver.md#class_TextServer_method_font_is_allow_system_fallback) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_is_force_autohinter](class_textserver.md#class_TextServer_method_font_is_force_autohinter) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_is_language_supported](class_textserver.md#class_TextServer_method_font_is_language_supported) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [font_is_modulate_color_glyphs](class_textserver.md#class_TextServer_method_font_is_modulate_color_glyphs) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_is_multichannel_signed_distance_field](class_textserver.md#class_TextServer_method_font_is_multichannel_signed_distance_field) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [font_is_script_supported](class_textserver.md#class_TextServer_method_font_is_script_supported) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) const |
| void | [font_remove_glyph](class_textserver.md#class_TextServer_method_font_remove_glyph) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) |
| void | [font_remove_kerning](class_textserver.md#class_TextServer_method_font_remove_kerning) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [font_remove_language_support_override](class_textserver.md#class_TextServer_method_font_remove_language_support_override) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) |
| void | [font_remove_script_support_override](class_textserver.md#class_TextServer_method_font_remove_script_support_override) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) |
| void | [font_remove_size_cache](class_textserver.md#class_TextServer_method_font_remove_size_cache) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [font_remove_texture](class_textserver.md#class_TextServer_method_font_remove_texture) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) |
| void | [font_render_glyph](class_textserver.md#class_TextServer_method_font_render_glyph) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), index: [int](class_int.md#class_int) ) |
| void | [font_render_range](class_textserver.md#class_TextServer_method_font_render_range) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) |
| void | [font_set_allow_system_fallback](class_textserver.md#class_TextServer_method_font_set_allow_system_fallback) ( font_rid: [RID](class_rid.md#class_RID), allow_system_fallback: [bool](class_bool.md#class_bool) ) |
| void | [font_set_antialiasing](class_textserver.md#class_TextServer_method_font_set_antialiasing) ( font_rid: [RID](class_rid.md#class_RID), antialiasing: [FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) ) |
| void | [font_set_ascent](class_textserver.md#class_TextServer_method_font_set_ascent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), ascent: [float](class_float.md#class_float) ) |
| void | [font_set_baseline_offset](class_textserver.md#class_TextServer_method_font_set_baseline_offset) ( font_rid: [RID](class_rid.md#class_RID), baseline_offset: [float](class_float.md#class_float) ) |
| void | [font_set_data](class_textserver.md#class_TextServer_method_font_set_data) ( font_rid: [RID](class_rid.md#class_RID), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [font_set_descent](class_textserver.md#class_TextServer_method_font_set_descent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), descent: [float](class_float.md#class_float) ) |
| void | [font_set_disable_embedded_bitmaps](class_textserver.md#class_TextServer_method_font_set_disable_embedded_bitmaps) ( font_rid: [RID](class_rid.md#class_RID), disable_embedded_bitmaps: [bool](class_bool.md#class_bool) ) |
| void | [font_set_embolden](class_textserver.md#class_TextServer_method_font_set_embolden) ( font_rid: [RID](class_rid.md#class_RID), strength: [float](class_float.md#class_float) ) |
| void | [font_set_face_index](class_textserver.md#class_TextServer_method_font_set_face_index) ( font_rid: [RID](class_rid.md#class_RID), face_index: [int](class_int.md#class_int) ) |
| void | [font_set_fixed_size](class_textserver.md#class_TextServer_method_font_set_fixed_size) ( font_rid: [RID](class_rid.md#class_RID), fixed_size: [int](class_int.md#class_int) ) |
| void | [font_set_fixed_size_scale_mode](class_textserver.md#class_TextServer_method_font_set_fixed_size_scale_mode) ( font_rid: [RID](class_rid.md#class_RID), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) ) |
| void | [font_set_force_autohinter](class_textserver.md#class_TextServer_method_font_set_force_autohinter) ( font_rid: [RID](class_rid.md#class_RID), force_autohinter: [bool](class_bool.md#class_bool) ) |
| void | [font_set_generate_mipmaps](class_textserver.md#class_TextServer_method_font_set_generate_mipmaps) ( font_rid: [RID](class_rid.md#class_RID), generate_mipmaps: [bool](class_bool.md#class_bool) ) |
| void | [font_set_global_oversampling](class_textserver.md#class_TextServer_method_font_set_global_oversampling) ( oversampling: [float](class_float.md#class_float) ) |
| void | [font_set_glyph_advance](class_textserver.md#class_TextServer_method_font_set_glyph_advance) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int), advance: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [font_set_glyph_offset](class_textserver.md#class_TextServer_method_font_set_glyph_offset) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), offset: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [font_set_glyph_size](class_textserver.md#class_TextServer_method_font_set_glyph_size) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), gl_size: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [font_set_glyph_texture_idx](class_textserver.md#class_TextServer_method_font_set_glyph_texture_idx) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), texture_idx: [int](class_int.md#class_int) ) |
| void | [font_set_glyph_uv_rect](class_textserver.md#class_TextServer_method_font_set_glyph_uv_rect) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), uv_rect: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [font_set_hinting](class_textserver.md#class_TextServer_method_font_set_hinting) ( font_rid: [RID](class_rid.md#class_RID), hinting: [Hinting](class_textserver.md#enum_TextServer_Hinting) ) |
| void | [font_set_keep_rounding_remainders](class_textserver.md#class_TextServer_method_font_set_keep_rounding_remainders) ( font_rid: [RID](class_rid.md#class_RID), keep_rounding_remainders: [bool](class_bool.md#class_bool) ) |
| void | [font_set_kerning](class_textserver.md#class_TextServer_method_font_set_kerning) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i), kerning: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [font_set_language_support_override](class_textserver.md#class_TextServer_method_font_set_language_support_override) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) |
| void | [font_set_modulate_color_glyphs](class_textserver.md#class_TextServer_method_font_set_modulate_color_glyphs) ( font_rid: [RID](class_rid.md#class_RID), force_autohinter: [bool](class_bool.md#class_bool) ) |
| void | [font_set_msdf_pixel_range](class_textserver.md#class_TextServer_method_font_set_msdf_pixel_range) ( font_rid: [RID](class_rid.md#class_RID), msdf_pixel_range: [int](class_int.md#class_int) ) |
| void | [font_set_msdf_size](class_textserver.md#class_TextServer_method_font_set_msdf_size) ( font_rid: [RID](class_rid.md#class_RID), msdf_size: [int](class_int.md#class_int) ) |
| void | [font_set_multichannel_signed_distance_field](class_textserver.md#class_TextServer_method_font_set_multichannel_signed_distance_field) ( font_rid: [RID](class_rid.md#class_RID), msdf: [bool](class_bool.md#class_bool) ) |
| void | [font_set_name](class_textserver.md#class_TextServer_method_font_set_name) ( font_rid: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) |
| void | [font_set_opentype_feature_overrides](class_textserver.md#class_TextServer_method_font_set_opentype_feature_overrides) ( font_rid: [RID](class_rid.md#class_RID), overrides: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [font_set_oversampling](class_textserver.md#class_TextServer_method_font_set_oversampling) ( font_rid: [RID](class_rid.md#class_RID), oversampling: [float](class_float.md#class_float) ) |
| void | [font_set_scale](class_textserver.md#class_TextServer_method_font_set_scale) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), scale: [float](class_float.md#class_float) ) |
| void | [font_set_script_support_override](class_textserver.md#class_TextServer_method_font_set_script_support_override) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) |
| void | [font_set_spacing](class_textserver.md#class_TextServer_method_font_set_spacing) ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) |
| void | [font_set_stretch](class_textserver.md#class_TextServer_method_font_set_stretch) ( font_rid: [RID](class_rid.md#class_RID), weight: [int](class_int.md#class_int) ) |
| void | [font_set_style](class_textserver.md#class_TextServer_method_font_set_style) ( font_rid: [RID](class_rid.md#class_RID), style: | bitfield | \[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] ) |
| void | [font_set_style_name](class_textserver.md#class_TextServer_method_font_set_style_name) ( font_rid: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) |
| void | [font_set_subpixel_positioning](class_textserver.md#class_TextServer_method_font_set_subpixel_positioning) ( font_rid: [RID](class_rid.md#class_RID), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) ) |
| void | [font_set_texture_image](class_textserver.md#class_TextServer_method_font_set_texture_image) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), image: [Image](class_image.md#class_Image) ) |
| void | [font_set_texture_offsets](class_textserver.md#class_TextServer_method_font_set_texture_offsets) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), offset: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| void | [font_set_transform](class_textserver.md#class_TextServer_method_font_set_transform) ( font_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [font_set_underline_position](class_textserver.md#class_TextServer_method_font_set_underline_position) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_position: [float](class_float.md#class_float) ) |
| void | [font_set_underline_thickness](class_textserver.md#class_TextServer_method_font_set_underline_thickness) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_thickness: [float](class_float.md#class_float) ) |
| void | [font_set_variation_coordinates](class_textserver.md#class_TextServer_method_font_set_variation_coordinates) ( font_rid: [RID](class_rid.md#class_RID), variation_coordinates: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [font_set_weight](class_textserver.md#class_TextServer_method_font_set_weight) ( font_rid: [RID](class_rid.md#class_RID), weight: [int](class_int.md#class_int) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [font_supported_feature_list](class_textserver.md#class_TextServer_method_font_supported_feature_list) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [font_supported_variation_list](class_textserver.md#class_TextServer_method_font_supported_variation_list) ( font_rid: [RID](class_rid.md#class_RID) ) const |
| [String](class_string.md#class_String) | [format_number](class_textserver.md#class_TextServer_method_format_number) ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) const |
| void | [free_rid](class_textserver.md#class_TextServer_method_free_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| [int](class_int.md#class_int) | [get_features](class_textserver.md#class_TextServer_method_get_features) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_hex_code_box_size](class_textserver.md#class_TextServer_method_get_hex_code_box_size) ( size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_name](class_textserver.md#class_TextServer_method_get_name) ( ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [get_support_data](class_textserver.md#class_TextServer_method_get_support_data) ( ) const |
| [String](class_string.md#class_String) | [get_support_data_filename](class_textserver.md#class_TextServer_method_get_support_data_filename) ( ) const |
| [String](class_string.md#class_String) | [get_support_data_info](class_textserver.md#class_TextServer_method_get_support_data_info) ( ) const |
| [bool](class_bool.md#class_bool) | [has](class_textserver.md#class_TextServer_method_has) ( rid: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [has_feature](class_textserver.md#class_TextServer_method_has_feature) ( feature: [Feature](class_textserver.md#enum_TextServer_Feature) ) const |
| [int](class_int.md#class_int) | [is_confusable](class_textserver.md#class_TextServer_method_is_confusable) ( string: [String](class_string.md#class_String), dict: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) const |
| [bool](class_bool.md#class_bool) | [is_locale_right_to_left](class_textserver.md#class_TextServer_method_is_locale_right_to_left) ( locale: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_locale_using_support_data](class_textserver.md#class_TextServer_method_is_locale_using_support_data) ( locale: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_valid_identifier](class_textserver.md#class_TextServer_method_is_valid_identifier) ( string: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_valid_letter](class_textserver.md#class_TextServer_method_is_valid_letter) ( unicode: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [load_support_data](class_textserver.md#class_TextServer_method_load_support_data) ( filename: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | [name_to_tag](class_textserver.md#class_TextServer_method_name_to_tag) ( name: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [parse_number](class_textserver.md#class_TextServer_method_parse_number) ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) const |
| [Array](class_array.md#class_Array)\[[Vector3i](class_vector3i.md#class_Vector3i)\] | [parse_structured_text](class_textserver.md#class_TextServer_method_parse_structured_text) ( parser_type: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser), args: [Array](class_array.md#class_Array), text: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [percent_sign](class_textserver.md#class_TextServer_method_percent_sign) ( language: [String](class_string.md#class_String) = "" ) const |
| [bool](class_bool.md#class_bool) | [save_support_data](class_textserver.md#class_TextServer_method_save_support_data) ( filename: [String](class_string.md#class_String) ) const |
| [int](class_int.md#class_int) | [shaped_get_run_count](class_textserver.md#class_TextServer_method_shaped_get_run_count) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [shaped_get_run_direction](class_textserver.md#class_TextServer_method_shaped_get_run_direction) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [shaped_get_run_font_rid](class_textserver.md#class_TextServer_method_shaped_get_run_font_rid) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shaped_get_run_font_size](class_textserver.md#class_TextServer_method_shaped_get_run_font_size) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [shaped_get_run_language](class_textserver.md#class_TextServer_method_shaped_get_run_language) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [shaped_get_run_object](class_textserver.md#class_TextServer_method_shaped_get_run_object) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [shaped_get_run_range](class_textserver.md#class_TextServer_method_shaped_get_run_range) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [shaped_get_run_text](class_textserver.md#class_TextServer_method_shaped_get_run_text) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shaped_get_span_count](class_textserver.md#class_TextServer_method_shaped_get_span_count) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Variant](class_variant.md#class_Variant) | [shaped_get_span_embedded_object](class_textserver.md#class_TextServer_method_shaped_get_span_embedded_object) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [shaped_get_span_meta](class_textserver.md#class_TextServer_method_shaped_get_span_meta) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [shaped_get_span_object](class_textserver.md#class_TextServer_method_shaped_get_span_object) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [shaped_get_span_text](class_textserver.md#class_TextServer_method_shaped_get_span_text) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [shaped_get_text](class_textserver.md#class_TextServer_method_shaped_get_text) ( shaped: [RID](class_rid.md#class_RID) ) const |
| void | [shaped_set_span_update_font](class_textserver.md#class_TextServer_method_shaped_set_span_update_font) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) |
| [bool](class_bool.md#class_bool) | [shaped_text_add_object](class_textserver.md#class_TextServer_method_shaped_text_add_object) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, length: [int](class_int.md#class_int) = 1, baseline: [float](class_float.md#class_float) = 0.0 ) |
| [bool](class_bool.md#class_bool) | [shaped_text_add_string](class_textserver.md#class_TextServer_method_shaped_text_add_string) ( shaped: [RID](class_rid.md#class_RID), text: [String](class_string.md#class_String), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary) = {}, language: [String](class_string.md#class_String) = "", meta: [Variant](class_variant.md#class_Variant) = null ) |
| void | [shaped_text_clear](class_textserver.md#class_TextServer_method_shaped_text_clear) ( rid: [RID](class_rid.md#class_RID) ) |
| [int](class_int.md#class_int) | [shaped_text_closest_character_pos](class_textserver.md#class_TextServer_method_shaped_text_closest_character_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) const |
| void | [shaped_text_draw](class_textserver.md#class_TextServer_method_shaped_text_draw) ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float) = -1, clip_r: [float](class_float.md#class_float) = -1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| void | [shaped_text_draw_outline](class_textserver.md#class_TextServer_method_shaped_text_draw_outline) ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float) = -1, clip_r: [float](class_float.md#class_float) = -1, outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) const |
| [RID](class_rid.md#class_RID) | [shaped_text_duplicate](class_textserver.md#class_TextServer_method_shaped_text_duplicate) ( rid: [RID](class_rid.md#class_RID) ) |
| [float](class_float.md#class_float) | [shaped_text_fit_to_width](class_textserver.md#class_TextServer_method_shaped_text_fit_to_width) ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), justification_flags: | bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] = 3 ) |
| [float](class_float.md#class_float) | [shaped_text_get_ascent](class_textserver.md#class_TextServer_method_shaped_text_get_ascent) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [shaped_text_get_carets](class_textserver.md#class_TextServer_method_shaped_text_get_carets) ( shaped: [RID](class_rid.md#class_RID), position: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [shaped_text_get_character_breaks](class_textserver.md#class_TextServer_method_shaped_text_get_character_breaks) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [shaped_text_get_custom_ellipsis](class_textserver.md#class_TextServer_method_shaped_text_get_custom_ellipsis) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [String](class_string.md#class_String) | [shaped_text_get_custom_punctuation](class_textserver.md#class_TextServer_method_shaped_text_get_custom_punctuation) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [shaped_text_get_descent](class_textserver.md#class_TextServer_method_shaped_text_get_descent) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [shaped_text_get_direction](class_textserver.md#class_TextServer_method_shaped_text_get_direction) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [shaped_text_get_dominant_direction_in_range](class_textserver.md#class_TextServer_method_shaped_text_get_dominant_direction_in_range) ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shaped_text_get_ellipsis_glyph_count](class_textserver.md#class_TextServer_method_shaped_text_get_ellipsis_glyph_count) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [shaped_text_get_ellipsis_glyphs](class_textserver.md#class_TextServer_method_shaped_text_get_ellipsis_glyphs) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [shaped_text_get_ellipsis_pos](class_textserver.md#class_TextServer_method_shaped_text_get_ellipsis_pos) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [shaped_text_get_glyph_count](class_textserver.md#class_TextServer_method_shaped_text_get_glyph_count) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [shaped_text_get_glyphs](class_textserver.md#class_TextServer_method_shaped_text_get_glyphs) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [shaped_text_get_grapheme_bounds](class_textserver.md#class_TextServer_method_shaped_text_get_grapheme_bounds) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [shaped_text_get_inferred_direction](class_textserver.md#class_TextServer_method_shaped_text_get_inferred_direction) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [shaped_text_get_line_breaks](class_textserver.md#class_TextServer_method_shaped_text_get_line_breaks) ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), start: [int](class_int.md#class_int) = 0, break_flags: | bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] = 3 ) | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [shaped_text_get_line_breaks_adv](class_textserver.md#class_TextServer_method_shaped_text_get_line_breaks_adv) ( shaped: [RID](class_rid.md#class_RID), width: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), start: [int](class_int.md#class_int) = 0, once: [bool](class_bool.md#class_bool) = true, break_flags: | bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] = 3 ) | const |
| [int](class_int.md#class_int) | [shaped_text_get_object_glyph](class_textserver.md#class_TextServer_method_shaped_text_get_object_glyph) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [shaped_text_get_object_range](class_textserver.md#class_TextServer_method_shaped_text_get_object_range) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [shaped_text_get_object_rect](class_textserver.md#class_TextServer_method_shaped_text_get_object_rect) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) const |
| [Array](class_array.md#class_Array) | [shaped_text_get_objects](class_textserver.md#class_TextServer_method_shaped_text_get_objects) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Orientation](class_textserver.md#enum_TextServer_Orientation) | [shaped_text_get_orientation](class_textserver.md#class_TextServer_method_shaped_text_get_orientation) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [shaped_text_get_parent](class_textserver.md#class_TextServer_method_shaped_text_get_parent) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [shaped_text_get_preserve_control](class_textserver.md#class_TextServer_method_shaped_text_get_preserve_control) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [shaped_text_get_preserve_invalid](class_textserver.md#class_TextServer_method_shaped_text_get_preserve_invalid) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [shaped_text_get_range](class_textserver.md#class_TextServer_method_shaped_text_get_range) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [shaped_text_get_selection](class_textserver.md#class_TextServer_method_shaped_text_get_selection) ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [shaped_text_get_size](class_textserver.md#class_TextServer_method_shaped_text_get_size) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [shaped_text_get_spacing](class_textserver.md#class_TextServer_method_shaped_text_get_spacing) ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) const |
| [int](class_int.md#class_int) | [shaped_text_get_trim_pos](class_textserver.md#class_TextServer_method_shaped_text_get_trim_pos) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [shaped_text_get_underline_position](class_textserver.md#class_TextServer_method_shaped_text_get_underline_position) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [shaped_text_get_underline_thickness](class_textserver.md#class_TextServer_method_shaped_text_get_underline_thickness) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [shaped_text_get_width](class_textserver.md#class_TextServer_method_shaped_text_get_width) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [shaped_text_get_word_breaks](class_textserver.md#class_TextServer_method_shaped_text_get_word_breaks) ( shaped: [RID](class_rid.md#class_RID), grapheme_flags: | bitfield | \[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\] = 264, skip_grapheme_flags: | bitfield | \[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\] = 4 ) | const |
| [bool](class_bool.md#class_bool) | [shaped_text_has_object](class_textserver.md#class_TextServer_method_shaped_text_has_object) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) const |
| [bool](class_bool.md#class_bool) | [shaped_text_has_visible_chars](class_textserver.md#class_TextServer_method_shaped_text_has_visible_chars) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [shaped_text_hit_test_grapheme](class_textserver.md#class_TextServer_method_shaped_text_hit_test_grapheme) ( shaped: [RID](class_rid.md#class_RID), coords: [float](class_float.md#class_float) ) const |
| [int](class_int.md#class_int) | [shaped_text_hit_test_position](class_textserver.md#class_TextServer_method_shaped_text_hit_test_position) ( shaped: [RID](class_rid.md#class_RID), coords: [float](class_float.md#class_float) ) const |
| [bool](class_bool.md#class_bool) | [shaped_text_is_ready](class_textserver.md#class_TextServer_method_shaped_text_is_ready) ( shaped: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [shaped_text_next_character_pos](class_textserver.md#class_TextServer_method_shaped_text_next_character_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shaped_text_next_grapheme_pos](class_textserver.md#class_TextServer_method_shaped_text_next_grapheme_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) const |
| void | [shaped_text_overrun_trim_to_width](class_textserver.md#class_TextServer_method_shaped_text_overrun_trim_to_width) ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float) = 0, overrun_trim_flags: | bitfield | \[[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag)\] = 0 ) |
| [int](class_int.md#class_int) | [shaped_text_prev_character_pos](class_textserver.md#class_TextServer_method_shaped_text_prev_character_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shaped_text_prev_grapheme_pos](class_textserver.md#class_TextServer_method_shaped_text_prev_grapheme_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [shaped_text_resize_object](class_textserver.md#class_TextServer_method_shaped_text_resize_object) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, baseline: [float](class_float.md#class_float) = 0.0 ) |
| void | [shaped_text_set_bidi_override](class_textserver.md#class_TextServer_method_shaped_text_set_bidi_override) ( shaped: [RID](class_rid.md#class_RID), override: [Array](class_array.md#class_Array) ) |
| void | [shaped_text_set_custom_ellipsis](class_textserver.md#class_TextServer_method_shaped_text_set_custom_ellipsis) ( shaped: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) |
| void | [shaped_text_set_custom_punctuation](class_textserver.md#class_TextServer_method_shaped_text_set_custom_punctuation) ( shaped: [RID](class_rid.md#class_RID), punct: [String](class_string.md#class_String) ) |
| void | [shaped_text_set_direction](class_textserver.md#class_TextServer_method_shaped_text_set_direction) ( shaped: [RID](class_rid.md#class_RID), direction: [Direction](class_textserver.md#enum_TextServer_Direction) = 0 ) |
| void | [shaped_text_set_orientation](class_textserver.md#class_TextServer_method_shaped_text_set_orientation) ( shaped: [RID](class_rid.md#class_RID), orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) = 0 ) |
| void | [shaped_text_set_preserve_control](class_textserver.md#class_TextServer_method_shaped_text_set_preserve_control) ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [shaped_text_set_preserve_invalid](class_textserver.md#class_TextServer_method_shaped_text_set_preserve_invalid) ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [shaped_text_set_spacing](class_textserver.md#class_TextServer_method_shaped_text_set_spacing) ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [shaped_text_shape](class_textserver.md#class_TextServer_method_shaped_text_shape) ( shaped: [RID](class_rid.md#class_RID) ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [shaped_text_sort_logical](class_textserver.md#class_TextServer_method_shaped_text_sort_logical) ( shaped: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [shaped_text_substr](class_textserver.md#class_TextServer_method_shaped_text_substr) ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), length: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [shaped_text_tab_align](class_textserver.md#class_TextServer_method_shaped_text_tab_align) ( shaped: [RID](class_rid.md#class_RID), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| [bool](class_bool.md#class_bool) | [spoof_check](class_textserver.md#class_TextServer_method_spoof_check) ( string: [String](class_string.md#class_String) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [string_get_character_breaks](class_textserver.md#class_TextServer_method_string_get_character_breaks) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [string_get_word_breaks](class_textserver.md#class_TextServer_method_string_get_word_breaks) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "", chars_per_line: [int](class_int.md#class_int) = 0 ) const |
| [String](class_string.md#class_String) | [string_to_lower](class_textserver.md#class_TextServer_method_string_to_lower) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) const |
| [String](class_string.md#class_String) | [string_to_title](class_textserver.md#class_TextServer_method_string_to_title) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) const |
| [String](class_string.md#class_String) | [string_to_upper](class_textserver.md#class_TextServer_method_string_to_upper) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) const |
| [String](class_string.md#class_String) | [strip_diacritics](class_textserver.md#class_TextServer_method_strip_diacritics) ( string: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [tag_to_name](class_textserver.md#class_TextServer_method_tag_to_name) ( tag: [int](class_int.md#class_int) ) const |

---

### Enumerations

<span id="enum_TextServer_FontAntialiasing"></span>

enum **FontAntialiasing**: [🔗](class_textserver.md#enum_TextServer_FontAntialiasing)

<span id="class_TextServer_constant_FONT_ANTIALIASING_NONE"></span>

[FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) **FONT_ANTIALIASING_NONE** = `0`

Font glyphs are rasterized as 1-bit bitmaps.

<span id="class_TextServer_constant_FONT_ANTIALIASING_GRAY"></span>

[FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) **FONT_ANTIALIASING_GRAY** = `1`

Font glyphs are rasterized as 8-bit grayscale anti-aliased bitmaps.

<span id="class_TextServer_constant_FONT_ANTIALIASING_LCD"></span>

[FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) **FONT_ANTIALIASING_LCD** = `2`

Font glyphs are rasterized for LCD screens.

LCD subpixel layout is determined by the value of the ProjectSettings.gui/theme/lcd_subpixel_layout setting.

LCD subpixel anti-aliasing mode is suitable only for rendering horizontal, unscaled text in 2D.

---

<span id="enum_TextServer_FontLCDSubpixelLayout"></span>

enum **FontLCDSubpixelLayout**: [🔗](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout)

<span id="class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_NONE"></span>

[FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) **FONT_LCD_SUBPIXEL_LAYOUT_NONE** = `0`

Unknown or unsupported subpixel layout, LCD subpixel antialiasing is disabled.

<span id="class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_HRGB"></span>

[FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) **FONT_LCD_SUBPIXEL_LAYOUT_HRGB** = `1`

Horizontal RGB subpixel layout.

<span id="class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_HBGR"></span>

[FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) **FONT_LCD_SUBPIXEL_LAYOUT_HBGR** = `2`

Horizontal BGR subpixel layout.

<span id="class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_VRGB"></span>

[FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) **FONT_LCD_SUBPIXEL_LAYOUT_VRGB** = `3`

Vertical RGB subpixel layout.

<span id="class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_VBGR"></span>

[FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) **FONT_LCD_SUBPIXEL_LAYOUT_VBGR** = `4`

Vertical BGR subpixel layout.

<span id="class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_MAX"></span>

[FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) **FONT_LCD_SUBPIXEL_LAYOUT_MAX** = `5`

Represents the size of the [FontLCDSubpixelLayout](class_textserver.md#enum_TextServer_FontLCDSubpixelLayout) enum.

---

<span id="enum_TextServer_Direction"></span>

enum **Direction**: [🔗](class_textserver.md#enum_TextServer_Direction)

<span id="class_TextServer_constant_DIRECTION_AUTO"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **DIRECTION_AUTO** = `0`

Text direction is determined based on contents and current locale.

<span id="class_TextServer_constant_DIRECTION_LTR"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **DIRECTION_LTR** = `1`

Text is written from left to right.

<span id="class_TextServer_constant_DIRECTION_RTL"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **DIRECTION_RTL** = `2`

Text is written from right to left.

<span id="class_TextServer_constant_DIRECTION_INHERITED"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **DIRECTION_INHERITED** = `3`

Text writing direction is the same as base string writing direction. Used for BiDi override only.

---

<span id="enum_TextServer_Orientation"></span>

enum **Orientation**: [🔗](class_textserver.md#enum_TextServer_Orientation)

<span id="class_TextServer_constant_ORIENTATION_HORIZONTAL"></span>

[Orientation](class_textserver.md#enum_TextServer_Orientation) **ORIENTATION_HORIZONTAL** = `0`

Text is written horizontally.

<span id="class_TextServer_constant_ORIENTATION_VERTICAL"></span>

[Orientation](class_textserver.md#enum_TextServer_Orientation) **ORIENTATION_VERTICAL** = `1`

Left to right text is written vertically from top to bottom.

Right to left text is written vertically from bottom to top.

---

<span id="enum_TextServer_JustificationFlag"></span>

flags **JustificationFlag**: [🔗](class_textserver.md#enum_TextServer_JustificationFlag)

<span id="class_TextServer_constant_JUSTIFICATION_NONE"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_NONE** = `0`

Do not justify text.

<span id="class_TextServer_constant_JUSTIFICATION_KASHIDA"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_KASHIDA** = `1`

Justify text by adding and removing kashidas.

<span id="class_TextServer_constant_JUSTIFICATION_WORD_BOUND"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_WORD_BOUND** = `2`

Justify text by changing width of the spaces between the words.

<span id="class_TextServer_constant_JUSTIFICATION_TRIM_EDGE_SPACES"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_TRIM_EDGE_SPACES** = `4`

Remove trailing and leading spaces from the justified text.

<span id="class_TextServer_constant_JUSTIFICATION_AFTER_LAST_TAB"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_AFTER_LAST_TAB** = `8`

Only apply justification to the part of the text after the last tab.

<span id="class_TextServer_constant_JUSTIFICATION_CONSTRAIN_ELLIPSIS"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_CONSTRAIN_ELLIPSIS** = `16`

Apply justification to the trimmed line with ellipsis.

<span id="class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_SKIP_LAST_LINE** = `32`

Do not apply justification to the last line of the paragraph.

<span id="class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS** = `64`

Do not apply justification to the last line of the paragraph with visible characters (takes precedence over [JUSTIFICATION_SKIP_LAST_LINE](class_textserver.md#class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE)).

<span id="class_TextServer_constant_JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE"></span>

[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag) **JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE** = `128`

Always apply justification to the paragraphs with a single line ([JUSTIFICATION_SKIP_LAST_LINE](class_textserver.md#class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE) and [JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS](class_textserver.md#class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS) are ignored).

---

<span id="enum_TextServer_AutowrapMode"></span>

enum **AutowrapMode**: [🔗](class_textserver.md#enum_TextServer_AutowrapMode)

<span id="class_TextServer_constant_AUTOWRAP_OFF"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **AUTOWRAP_OFF** = `0`

Autowrap is disabled.

<span id="class_TextServer_constant_AUTOWRAP_ARBITRARY"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **AUTOWRAP_ARBITRARY** = `1`

Wraps the text inside the node's bounding rectangle by allowing to break lines at arbitrary positions, which is useful when very limited space is available.

<span id="class_TextServer_constant_AUTOWRAP_WORD"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **AUTOWRAP_WORD** = `2`

Wraps the text inside the node's bounding rectangle by soft-breaking between words.

<span id="class_TextServer_constant_AUTOWRAP_WORD_SMART"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **AUTOWRAP_WORD_SMART** = `3`

Behaves similarly to [AUTOWRAP_WORD](class_textserver.md#class_TextServer_constant_AUTOWRAP_WORD), but force-breaks a word if that single word does not fit in one line.

---

<span id="enum_TextServer_LineBreakFlag"></span>

flags **LineBreakFlag**: [🔗](class_textserver.md#enum_TextServer_LineBreakFlag)

<span id="class_TextServer_constant_BREAK_NONE"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_NONE** = `0`

Do not break the line.

<span id="class_TextServer_constant_BREAK_MANDATORY"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_MANDATORY** = `1`

Break the line at the line mandatory break characters (e.g. `"\n"`).

<span id="class_TextServer_constant_BREAK_WORD_BOUND"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_WORD_BOUND** = `2`

Break the line between the words.

<span id="class_TextServer_constant_BREAK_GRAPHEME_BOUND"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_GRAPHEME_BOUND** = `4`

Break the line between any unconnected graphemes.

<span id="class_TextServer_constant_BREAK_ADAPTIVE"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_ADAPTIVE** = `8`

Should be used only in conjunction with [BREAK_WORD_BOUND](class_textserver.md#class_TextServer_constant_BREAK_WORD_BOUND), break the line between any unconnected graphemes, if it's impossible to break it between the words.

<span id="class_TextServer_constant_BREAK_TRIM_EDGE_SPACES"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_TRIM_EDGE_SPACES** = `16`

**Deprecated:** Use `BREAK_TRIM_START_EDGE_SPACES | BREAK_TRIM_END_EDGE_SPACES` instead.

Remove edge spaces from the broken line segments.

<span id="class_TextServer_constant_BREAK_TRIM_INDENT"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_TRIM_INDENT** = `32`

Subtract first line indentation width from all lines after the first one.

<span id="class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_TRIM_START_EDGE_SPACES** = `64`

Remove spaces and line break characters from the start of broken line segments.

E.g, after line breaking, the second segment of the following text `test  \n  next`, is `next` if the flag is set, and `  next` if it is not.

<span id="class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES"></span>

[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag) **BREAK_TRIM_END_EDGE_SPACES** = `128`

Remove spaces and line break characters from the end of broken line segments.

E.g, after line breaking, the first segment of the following text `test  \n  next`, is `test` if the flag is set, and `test  \n` if it is not.

---

<span id="enum_TextServer_VisibleCharactersBehavior"></span>

enum **VisibleCharactersBehavior**: [🔗](class_textserver.md#enum_TextServer_VisibleCharactersBehavior)

<span id="class_TextServer_constant_VC_CHARS_BEFORE_SHAPING"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **VC_CHARS_BEFORE_SHAPING** = `0`

Trims text before the shaping. e.g, increasing [Label.visible_characters](class_label.md#class_Label_property_visible_characters) or [RichTextLabel.visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters) value is visually identical to typing the text.

 **Note:** In this mode, trimmed text is not processed at all. It is not accounted for in line breaking and size calculations.

<span id="class_TextServer_constant_VC_CHARS_AFTER_SHAPING"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **VC_CHARS_AFTER_SHAPING** = `1`

Displays glyphs that are mapped to the first [Label.visible_characters](class_label.md#class_Label_property_visible_characters) or [RichTextLabel.visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters) characters from the beginning of the text.

<span id="class_TextServer_constant_VC_GLYPHS_AUTO"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **VC_GLYPHS_AUTO** = `2`

Displays [Label.visible_ratio](class_label.md#class_Label_property_visible_ratio) or [RichTextLabel.visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) glyphs, starting from the left or from the right, depending on [Control.layout_direction](class_control.md#class_Control_property_layout_direction) value.

<span id="class_TextServer_constant_VC_GLYPHS_LTR"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **VC_GLYPHS_LTR** = `3`

Displays [Label.visible_ratio](class_label.md#class_Label_property_visible_ratio) or [RichTextLabel.visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) glyphs, starting from the left.

<span id="class_TextServer_constant_VC_GLYPHS_RTL"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **VC_GLYPHS_RTL** = `4`

Displays [Label.visible_ratio](class_label.md#class_Label_property_visible_ratio) or [RichTextLabel.visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) glyphs, starting from the right.

---

<span id="enum_TextServer_OverrunBehavior"></span>

enum **OverrunBehavior**: [🔗](class_textserver.md#enum_TextServer_OverrunBehavior)

<span id="class_TextServer_constant_OVERRUN_NO_TRIMMING"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_NO_TRIMMING** = `0`

No text trimming is performed.

<span id="class_TextServer_constant_OVERRUN_TRIM_CHAR"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_TRIM_CHAR** = `1`

Trims the text per character.

<span id="class_TextServer_constant_OVERRUN_TRIM_WORD"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_TRIM_WORD** = `2`

Trims the text per word.

<span id="class_TextServer_constant_OVERRUN_TRIM_ELLIPSIS"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_TRIM_ELLIPSIS** = `3`

Trims the text per character and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.

<span id="class_TextServer_constant_OVERRUN_TRIM_WORD_ELLIPSIS"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_TRIM_WORD_ELLIPSIS** = `4`

Trims the text per word and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.

<span id="class_TextServer_constant_OVERRUN_TRIM_ELLIPSIS_FORCE"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_TRIM_ELLIPSIS_FORCE** = `5`

Trims the text per character and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.

<span id="class_TextServer_constant_OVERRUN_TRIM_WORD_ELLIPSIS_FORCE"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **OVERRUN_TRIM_WORD_ELLIPSIS_FORCE** = `6`

Trims the text per word and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.

---

<span id="enum_TextServer_TextOverrunFlag"></span>

flags **TextOverrunFlag**: [🔗](class_textserver.md#enum_TextServer_TextOverrunFlag)

<span id="class_TextServer_constant_OVERRUN_NO_TRIM"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_NO_TRIM** = `0`

No trimming is performed.

<span id="class_TextServer_constant_OVERRUN_TRIM"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_TRIM** = `1`

Trims the text when it exceeds the given width.

<span id="class_TextServer_constant_OVERRUN_TRIM_WORD_ONLY"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_TRIM_WORD_ONLY** = `2`

Trims the text per word instead of per grapheme.

<span id="class_TextServer_constant_OVERRUN_ADD_ELLIPSIS"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_ADD_ELLIPSIS** = `4`

Determines whether an ellipsis should be added at the end of the text.

<span id="class_TextServer_constant_OVERRUN_ENFORCE_ELLIPSIS"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_ENFORCE_ELLIPSIS** = `8`

Determines whether the ellipsis at the end of the text is enforced and may not be hidden.

<span id="class_TextServer_constant_OVERRUN_JUSTIFICATION_AWARE"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_JUSTIFICATION_AWARE** = `16`

Accounts for the text being justified before attempting to trim it (see [JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)).

<span id="class_TextServer_constant_OVERRUN_SHORT_STRING_ELLIPSIS"></span>

[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag) **OVERRUN_SHORT_STRING_ELLIPSIS** = `32`

Determines whether the ellipsis should be added regardless of the string length, otherwise it is added only if the string is 6 characters or longer.

---

<span id="enum_TextServer_GraphemeFlag"></span>

flags **GraphemeFlag**: [🔗](class_textserver.md#enum_TextServer_GraphemeFlag)

<span id="class_TextServer_constant_GRAPHEME_IS_VALID"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_VALID** = `1`

Grapheme is supported by the font, and can be drawn.

<span id="class_TextServer_constant_GRAPHEME_IS_RTL"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_RTL** = `2`

Grapheme is part of right-to-left or bottom-to-top run.

<span id="class_TextServer_constant_GRAPHEME_IS_VIRTUAL"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_VIRTUAL** = `4`

Grapheme is not part of source text, it was added by justification process.

<span id="class_TextServer_constant_GRAPHEME_IS_SPACE"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_SPACE** = `8`

Grapheme is whitespace.

<span id="class_TextServer_constant_GRAPHEME_IS_BREAK_HARD"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_BREAK_HARD** = `16`

Grapheme is mandatory break point (e.g. `"\n"`).

<span id="class_TextServer_constant_GRAPHEME_IS_BREAK_SOFT"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_BREAK_SOFT** = `32`

Grapheme is optional break point (e.g. space).

<span id="class_TextServer_constant_GRAPHEME_IS_TAB"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_TAB** = `64`

Grapheme is the tabulation character.

<span id="class_TextServer_constant_GRAPHEME_IS_ELONGATION"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_ELONGATION** = `128`

Grapheme is kashida.

<span id="class_TextServer_constant_GRAPHEME_IS_PUNCTUATION"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_PUNCTUATION** = `256`

Grapheme is punctuation character.

<span id="class_TextServer_constant_GRAPHEME_IS_UNDERSCORE"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_UNDERSCORE** = `512`

Grapheme is underscore character.

<span id="class_TextServer_constant_GRAPHEME_IS_CONNECTED"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_CONNECTED** = `1024`

Grapheme is connected to the previous grapheme. Breaking line before this grapheme is not safe.

<span id="class_TextServer_constant_GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL** = `2048`

It is safe to insert a U+0640 before this grapheme for elongation.

<span id="class_TextServer_constant_GRAPHEME_IS_EMBEDDED_OBJECT"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_EMBEDDED_OBJECT** = `4096`

Grapheme is an object replacement character for the embedded object.

<span id="class_TextServer_constant_GRAPHEME_IS_SOFT_HYPHEN"></span>

[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag) **GRAPHEME_IS_SOFT_HYPHEN** = `8192`

Grapheme is a soft hyphen.

---

<span id="enum_TextServer_Hinting"></span>

enum **Hinting**: [🔗](class_textserver.md#enum_TextServer_Hinting)

<span id="class_TextServer_constant_HINTING_NONE"></span>

[Hinting](class_textserver.md#enum_TextServer_Hinting) **HINTING_NONE** = `0`

Disables font hinting (smoother but less crisp).

<span id="class_TextServer_constant_HINTING_LIGHT"></span>

[Hinting](class_textserver.md#enum_TextServer_Hinting) **HINTING_LIGHT** = `1`

Use the light font hinting mode.

<span id="class_TextServer_constant_HINTING_NORMAL"></span>

[Hinting](class_textserver.md#enum_TextServer_Hinting) **HINTING_NORMAL** = `2`

Use the default font hinting mode (crisper but less smooth).

 **Note:** This hinting mode changes both horizontal and vertical glyph metrics. If applied to monospace font, some glyphs might have different width.

---

<span id="enum_TextServer_SubpixelPositioning"></span>

enum **SubpixelPositioning**: [🔗](class_textserver.md#enum_TextServer_SubpixelPositioning)

<span id="class_TextServer_constant_SUBPIXEL_POSITIONING_DISABLED"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **SUBPIXEL_POSITIONING_DISABLED** = `0`

Glyph horizontal position is rounded to the whole pixel size, each glyph is rasterized once.

<span id="class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **SUBPIXEL_POSITIONING_AUTO** = `1`

Glyph horizontal position is rounded based on font size.

- To one quarter of the pixel size if font size is smaller or equal to [SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE](class_textserver.md#class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE).

- To one half of the pixel size if font size is smaller or equal to [SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE](class_textserver.md#class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE).

- To the whole pixel size for larger fonts.

<span id="class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **SUBPIXEL_POSITIONING_ONE_HALF** = `2`

Glyph horizontal position is rounded to one half of the pixel size, each glyph is rasterized up to two times.

<span id="class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **SUBPIXEL_POSITIONING_ONE_QUARTER** = `3`

Glyph horizontal position is rounded to one quarter of the pixel size, each glyph is rasterized up to four times.

<span id="class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE** = `20`

Maximum font size which will use "one half of the pixel" subpixel positioning in [SUBPIXEL_POSITIONING_AUTO](class_textserver.md#class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO) mode.

<span id="class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE** = `16`

Maximum font size which will use "one quarter of the pixel" subpixel positioning in [SUBPIXEL_POSITIONING_AUTO](class_textserver.md#class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO) mode.

---

<span id="enum_TextServer_Feature"></span>

enum **Feature**: [🔗](class_textserver.md#enum_TextServer_Feature)

<span id="class_TextServer_constant_FEATURE_SIMPLE_LAYOUT"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_SIMPLE_LAYOUT** = `1`

TextServer supports simple text layouts.

<span id="class_TextServer_constant_FEATURE_BIDI_LAYOUT"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_BIDI_LAYOUT** = `2`

TextServer supports bidirectional text layouts.

<span id="class_TextServer_constant_FEATURE_VERTICAL_LAYOUT"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_VERTICAL_LAYOUT** = `4`

TextServer supports vertical layouts.

<span id="class_TextServer_constant_FEATURE_SHAPING"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_SHAPING** = `8`

TextServer supports complex text shaping.

<span id="class_TextServer_constant_FEATURE_KASHIDA_JUSTIFICATION"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_KASHIDA_JUSTIFICATION** = `16`

TextServer supports justification using kashidas.

<span id="class_TextServer_constant_FEATURE_BREAK_ITERATORS"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_BREAK_ITERATORS** = `32`

TextServer supports complex line/word breaking rules (e.g. dictionary based).

<span id="class_TextServer_constant_FEATURE_FONT_BITMAP"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_FONT_BITMAP** = `64`

TextServer supports loading bitmap fonts.

<span id="class_TextServer_constant_FEATURE_FONT_DYNAMIC"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_FONT_DYNAMIC** = `128`

TextServer supports loading dynamic (TrueType, OpeType, etc.) fonts.

<span id="class_TextServer_constant_FEATURE_FONT_MSDF"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_FONT_MSDF** = `256`

TextServer supports multichannel signed distance field dynamic font rendering.

<span id="class_TextServer_constant_FEATURE_FONT_SYSTEM"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_FONT_SYSTEM** = `512`

TextServer supports loading system fonts.

<span id="class_TextServer_constant_FEATURE_FONT_VARIABLE"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_FONT_VARIABLE** = `1024`

TextServer supports variable fonts.

<span id="class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION** = `2048`

TextServer supports locale dependent and context sensitive case conversion.

<span id="class_TextServer_constant_FEATURE_USE_SUPPORT_DATA"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_USE_SUPPORT_DATA** = `4096`

TextServer require external data file for some features, see [load_support_data()](class_textserver.md#class_TextServer_method_load_support_data).

<span id="class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_UNICODE_IDENTIFIERS** = `8192`

TextServer supports UAX #31 identifier validation, see [is_valid_identifier()](class_textserver.md#class_TextServer_method_is_valid_identifier).

<span id="class_TextServer_constant_FEATURE_UNICODE_SECURITY"></span>

[Feature](class_textserver.md#enum_TextServer_Feature) **FEATURE_UNICODE_SECURITY** = `16384`

TextServer supports Unicode Technical Report #36 and Unicode Technical Standard #39 based spoof detection features.

---

<span id="enum_TextServer_ContourPointTag"></span>

enum **ContourPointTag**: [🔗](class_textserver.md#enum_TextServer_ContourPointTag)

<span id="class_TextServer_constant_CONTOUR_CURVE_TAG_ON"></span>

[ContourPointTag](class_textserver.md#enum_TextServer_ContourPointTag) **CONTOUR_CURVE_TAG_ON** = `1`

Contour point is on the curve.

<span id="class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC"></span>

[ContourPointTag](class_textserver.md#enum_TextServer_ContourPointTag) **CONTOUR_CURVE_TAG_OFF_CONIC** = `0`

Contour point isn't on the curve, but serves as a control point for a conic (quadratic) Bézier arc.

<span id="class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CUBIC"></span>

[ContourPointTag](class_textserver.md#enum_TextServer_ContourPointTag) **CONTOUR_CURVE_TAG_OFF_CUBIC** = `2`

Contour point isn't on the curve, but serves as a control point for a cubic Bézier arc.

---

<span id="enum_TextServer_SpacingType"></span>

enum **SpacingType**: [🔗](class_textserver.md#enum_TextServer_SpacingType)

<span id="class_TextServer_constant_SPACING_GLYPH"></span>

[SpacingType](class_textserver.md#enum_TextServer_SpacingType) **SPACING_GLYPH** = `0`

Spacing for each glyph.

<span id="class_TextServer_constant_SPACING_SPACE"></span>

[SpacingType](class_textserver.md#enum_TextServer_SpacingType) **SPACING_SPACE** = `1`

Spacing for the space character.

<span id="class_TextServer_constant_SPACING_TOP"></span>

[SpacingType](class_textserver.md#enum_TextServer_SpacingType) **SPACING_TOP** = `2`

Spacing at the top of the line.

<span id="class_TextServer_constant_SPACING_BOTTOM"></span>

[SpacingType](class_textserver.md#enum_TextServer_SpacingType) **SPACING_BOTTOM** = `3`

Spacing at the bottom of the line.

<span id="class_TextServer_constant_SPACING_MAX"></span>

[SpacingType](class_textserver.md#enum_TextServer_SpacingType) **SPACING_MAX** = `4`

Represents the size of the [SpacingType](class_textserver.md#enum_TextServer_SpacingType) enum.

---

<span id="enum_TextServer_FontStyle"></span>

flags **FontStyle**: [🔗](class_textserver.md#enum_TextServer_FontStyle)

<span id="class_TextServer_constant_FONT_BOLD"></span>

[FontStyle](class_textserver.md#enum_TextServer_FontStyle) **FONT_BOLD** = `1`

Font is bold.

<span id="class_TextServer_constant_FONT_ITALIC"></span>

[FontStyle](class_textserver.md#enum_TextServer_FontStyle) **FONT_ITALIC** = `2`

Font is italic or oblique.

<span id="class_TextServer_constant_FONT_FIXED_WIDTH"></span>

[FontStyle](class_textserver.md#enum_TextServer_FontStyle) **FONT_FIXED_WIDTH** = `4`

Font has fixed-width characters (also known as monospace).

---

<span id="enum_TextServer_StructuredTextParser"></span>

enum **StructuredTextParser**: [🔗](class_textserver.md#enum_TextServer_StructuredTextParser)

<span id="class_TextServer_constant_STRUCTURED_TEXT_DEFAULT"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_DEFAULT** = `0`

Use default Unicode BiDi algorithm.

<span id="class_TextServer_constant_STRUCTURED_TEXT_URI"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_URI** = `1`

BiDi override for URI.

<span id="class_TextServer_constant_STRUCTURED_TEXT_FILE"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_FILE** = `2`

BiDi override for file path.

<span id="class_TextServer_constant_STRUCTURED_TEXT_EMAIL"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_EMAIL** = `3`

BiDi override for email.

<span id="class_TextServer_constant_STRUCTURED_TEXT_LIST"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_LIST** = `4`

BiDi override for lists. Structured text options: list separator [String](class_string.md#class_String).

<span id="class_TextServer_constant_STRUCTURED_TEXT_GDSCRIPT"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_GDSCRIPT** = `5`

BiDi override for GDScript.

<span id="class_TextServer_constant_STRUCTURED_TEXT_CUSTOM"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **STRUCTURED_TEXT_CUSTOM** = `6`

User defined structured text BiDi override function.

---

<span id="enum_TextServer_FixedSizeScaleMode"></span>

enum **FixedSizeScaleMode**: [🔗](class_textserver.md#enum_TextServer_FixedSizeScaleMode)

<span id="class_TextServer_constant_FIXED_SIZE_SCALE_DISABLE"></span>

[FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) **FIXED_SIZE_SCALE_DISABLE** = `0`

Bitmap font is not scaled.

<span id="class_TextServer_constant_FIXED_SIZE_SCALE_INTEGER_ONLY"></span>

[FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) **FIXED_SIZE_SCALE_INTEGER_ONLY** = `1`

Bitmap font is scaled to the closest integer multiple of the font's fixed size. This is the recommended option for pixel art fonts.

<span id="class_TextServer_constant_FIXED_SIZE_SCALE_ENABLED"></span>

[FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) **FIXED_SIZE_SCALE_ENABLED** = `2`

Bitmap font is scaled to an arbitrary (fractional) size. This is the recommended option for non-pixel art fonts.

---

### Method Descriptions

<span id="class_TextServer_method_create_font"></span>

[RID](class_rid.md#class_RID) **create_font** ( ) [🔗](class_textserver.md#class_TextServer_method_create_font)

Creates a new, empty font cache entry resource. To free the resulting resource, use the [free_rid()](class_textserver.md#class_TextServer_method_free_rid) method.

---

<span id="class_TextServer_method_create_font_linked_variation"></span>

[RID](class_rid.md#class_RID) **create_font_linked_variation** ( font_rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_create_font_linked_variation)

Creates a new variation existing font which is reusing the same glyph cache and font data. To free the resulting resource, use the [free_rid()](class_textserver.md#class_TextServer_method_free_rid) method.

---

<span id="class_TextServer_method_create_shaped_text"></span>

[RID](class_rid.md#class_RID) **create_shaped_text** ( direction: [Direction](class_textserver.md#enum_TextServer_Direction) = 0, orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) = 0 ) [🔗](class_textserver.md#class_TextServer_method_create_shaped_text)

Creates a new buffer for complex text layout, with the given `direction` and `orientation`. To free the resulting buffer, use [free_rid()](class_textserver.md#class_TextServer_method_free_rid) method.

 **Note:** Direction is ignored if server does not support [FEATURE_BIDI_LAYOUT](class_textserver.md#class_TextServer_constant_FEATURE_BIDI_LAYOUT) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

 **Note:** Orientation is ignored if server does not support [FEATURE_VERTICAL_LAYOUT](class_textserver.md#class_TextServer_constant_FEATURE_VERTICAL_LAYOUT) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

---

<span id="class_TextServer_method_draw_hex_code_box"></span>

void **draw_hex_code_box** ( canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) *const* [🔗](class_textserver.md#class_TextServer_method_draw_hex_code_box)

Draws box displaying character hexadecimal code. Used for replacing missing characters.

---

<span id="class_TextServer_method_font_clear_glyphs"></span>

void **font_clear_glyphs** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_textserver.md#class_TextServer_method_font_clear_glyphs)

Removes all rendered glyph information from the cache entry.

 **Note:** This function will not remove textures associated with the glyphs, use [font_remove_texture()](class_textserver.md#class_TextServer_method_font_remove_texture) to remove them manually.

---

<span id="class_TextServer_method_font_clear_kerning_map"></span>

void **font_clear_kerning_map** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_clear_kerning_map)

Removes all kerning overrides.

---

<span id="class_TextServer_method_font_clear_size_cache"></span>

void **font_clear_size_cache** ( font_rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_font_clear_size_cache)

Removes all font sizes from the cache entry.

---

<span id="class_TextServer_method_font_clear_system_fallback_cache"></span>

void **font_clear_system_fallback_cache** ( ) [🔗](class_textserver.md#class_TextServer_method_font_clear_system_fallback_cache)

Frees all automatically loaded system fonts.

---

<span id="class_TextServer_method_font_clear_textures"></span>

void **font_clear_textures** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_textserver.md#class_TextServer_method_font_clear_textures)

Removes all textures from font cache entry.

 **Note:** This function will not remove glyphs associated with the texture, use [font_remove_glyph()](class_textserver.md#class_TextServer_method_font_remove_glyph) to remove them manually.

---

<span id="class_TextServer_method_font_draw_glyph"></span>

void **font_draw_glyph** ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textserver.md#class_TextServer_method_font_draw_glyph)

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

 **Note:** Glyph index is specific to the font, use glyphs indices returned by [shaped_text_get_glyphs()](class_textserver.md#class_TextServer_method_shaped_text_get_glyphs) or [font_get_glyph_index()](class_textserver.md#class_TextServer_method_font_get_glyph_index).

 **Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

<span id="class_TextServer_method_font_draw_glyph_outline"></span>

void **font_draw_glyph_outline** ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), outline_size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textserver.md#class_TextServer_method_font_draw_glyph_outline)

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

 **Note:** Glyph index is specific to the font, use glyphs indices returned by [shaped_text_get_glyphs()](class_textserver.md#class_TextServer_method_shaped_text_get_glyphs) or [font_get_glyph_index()](class_textserver.md#class_TextServer_method_font_get_glyph_index).

 **Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

<span id="class_TextServer_method_font_get_antialiasing"></span>

[FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) **font_get_antialiasing** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_antialiasing)

Returns font anti-aliasing mode.

---

<span id="class_TextServer_method_font_get_ascent"></span>

[float](class_float.md#class_float) **font_get_ascent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_ascent)

Returns the font ascent (number of pixels above the baseline).

---

<span id="class_TextServer_method_font_get_baseline_offset"></span>

[float](class_float.md#class_float) **font_get_baseline_offset** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_baseline_offset)

Returns extra baseline offset (as a fraction of font height).

---

<span id="class_TextServer_method_font_get_char_from_glyph_index"></span>

[int](class_int.md#class_int) **font_get_char_from_glyph_index** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_char_from_glyph_index)

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid. See [font_get_glyph_index()](class_textserver.md#class_TextServer_method_font_get_glyph_index).

---

<span id="class_TextServer_method_font_get_descent"></span>

[float](class_float.md#class_float) **font_get_descent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_descent)

Returns the font descent (number of pixels below the baseline).

---

<span id="class_TextServer_method_font_get_disable_embedded_bitmaps"></span>

[bool](class_bool.md#class_bool) **font_get_disable_embedded_bitmaps** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_disable_embedded_bitmaps)

Returns whether the font's embedded bitmap loading is disabled.

---

<span id="class_TextServer_method_font_get_embolden"></span>

[float](class_float.md#class_float) **font_get_embolden** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_embolden)

Returns font embolden strength.

---

<span id="class_TextServer_method_font_get_face_count"></span>

[int](class_int.md#class_int) **font_get_face_count** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_face_count)

Returns number of faces in the TrueType / OpenType collection.

---

<span id="class_TextServer_method_font_get_face_index"></span>

[int](class_int.md#class_int) **font_get_face_index** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_face_index)

Returns an active face index in the TrueType / OpenType collection.

---

<span id="class_TextServer_method_font_get_fixed_size"></span>

[int](class_int.md#class_int) **font_get_fixed_size** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_fixed_size)

Returns bitmap font fixed size.

---

<span id="class_TextServer_method_font_get_fixed_size_scale_mode"></span>

[FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) **font_get_fixed_size_scale_mode** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_fixed_size_scale_mode)

Returns bitmap font scaling mode.

---

<span id="class_TextServer_method_font_get_generate_mipmaps"></span>

[bool](class_bool.md#class_bool) **font_get_generate_mipmaps** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_generate_mipmaps)

Returns `true` if font texture mipmap generation is enabled.

---

<span id="class_TextServer_method_font_get_global_oversampling"></span>

[float](class_float.md#class_float) **font_get_global_oversampling** ( ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_global_oversampling)

**Deprecated:** Use [Viewport](class_viewport.md#class_Viewport) oversampling, or the `oversampling` argument of the `draw_*` methods instead.

This method does nothing and always returns `1.0`.

---

<span id="class_TextServer_method_font_get_glyph_advance"></span>

[Vector2](class_vector2.md#class_Vector2) **font_get_glyph_advance** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_advance)

Returns glyph advance (offset of the next glyph).

 **Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---

<span id="class_TextServer_method_font_get_glyph_contours"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **font_get_glyph_contours** ( font: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_contours)

Returns outline contours of the glyph as a [Dictionary](class_dictionary.md#class_Dictionary) with the following contents:

 `points`         - [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), containing outline points. `x` and `y` are point coordinates. `z` is the type of the point, using the [ContourPointTag](class_textserver.md#enum_TextServer_ContourPointTag) values.

 `contours`       - [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), containing indices the end points of each contour.

 `orientation`    - [bool](class_bool.md#class_bool), contour orientation. If `true`, clockwise contours must be filled.

- Two successive [CONTOUR_CURVE_TAG_ON](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_ON) points indicate a line segment.

- One [CONTOUR_CURVE_TAG_OFF_CONIC](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC) point between two [CONTOUR_CURVE_TAG_ON](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_ON) points indicates a single conic (quadratic) Bézier arc.

- Two [CONTOUR_CURVE_TAG_OFF_CUBIC](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CUBIC) points between two [CONTOUR_CURVE_TAG_ON](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_ON) points indicate a single cubic Bézier arc.

- Two successive [CONTOUR_CURVE_TAG_OFF_CONIC](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC) points indicate two successive conic (quadratic) Bézier arcs with a virtual [CONTOUR_CURVE_TAG_ON](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_ON) point at their middle.

- Each contour is closed. The last point of a contour uses the first point of a contour as its next point, and vice versa. The first point can be [CONTOUR_CURVE_TAG_OFF_CONIC](class_textserver.md#class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC) point.

---

<span id="class_TextServer_method_font_get_glyph_index"></span>

[int](class_int.md#class_int) **font_get_glyph_index** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), char: [int](class_int.md#class_int), variation_selector: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_index)

Returns the glyph index of a `char`, optionally modified by the `variation_selector`. See [font_get_char_from_glyph_index()](class_textserver.md#class_TextServer_method_font_get_char_from_glyph_index).

---

<span id="class_TextServer_method_font_get_glyph_list"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **font_get_glyph_list** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_list)

Returns list of rendered glyphs in the cache entry.

---

<span id="class_TextServer_method_font_get_glyph_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **font_get_glyph_offset** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_offset)

Returns glyph offset from the baseline.

---

<span id="class_TextServer_method_font_get_glyph_size"></span>

[Vector2](class_vector2.md#class_Vector2) **font_get_glyph_size** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_size)

Returns size of the glyph.

---

<span id="class_TextServer_method_font_get_glyph_texture_idx"></span>

[int](class_int.md#class_int) **font_get_glyph_texture_idx** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_texture_idx)

Returns index of the cache texture containing the glyph.

---

<span id="class_TextServer_method_font_get_glyph_texture_rid"></span>

[RID](class_rid.md#class_RID) **font_get_glyph_texture_rid** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_texture_rid)

Returns resource ID of the cache texture containing the glyph.

 **Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

<span id="class_TextServer_method_font_get_glyph_texture_size"></span>

[Vector2](class_vector2.md#class_Vector2) **font_get_glyph_texture_size** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_texture_size)

Returns size of the cache texture containing the glyph.

 **Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

<span id="class_TextServer_method_font_get_glyph_uv_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **font_get_glyph_uv_rect** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_glyph_uv_rect)

Returns rectangle in the cache texture containing the glyph.

---

<span id="class_TextServer_method_font_get_hinting"></span>

[Hinting](class_textserver.md#enum_TextServer_Hinting) **font_get_hinting** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_hinting)

Returns the font hinting mode. Used by dynamic fonts only.

---

<span id="class_TextServer_method_font_get_keep_rounding_remainders"></span>

[bool](class_bool.md#class_bool) **font_get_keep_rounding_remainders** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_keep_rounding_remainders)

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

<span id="class_TextServer_method_font_get_kerning"></span>

[Vector2](class_vector2.md#class_Vector2) **font_get_kerning** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_kerning)

Returns kerning for the pair of glyphs.

---

<span id="class_TextServer_method_font_get_kerning_list"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **font_get_kerning_list** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_kerning_list)

Returns list of the kerning overrides.

---

<span id="class_TextServer_method_font_get_language_support_override"></span>

[bool](class_bool.md#class_bool) **font_get_language_support_override** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_font_get_language_support_override)

Returns `true` if support override is enabled for the `language`.

---

<span id="class_TextServer_method_font_get_language_support_overrides"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **font_get_language_support_overrides** ( font_rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_font_get_language_support_overrides)

Returns list of language support overrides.

---

<span id="class_TextServer_method_font_get_msdf_pixel_range"></span>

[int](class_int.md#class_int) **font_get_msdf_pixel_range** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_msdf_pixel_range)

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

---

<span id="class_TextServer_method_font_get_msdf_size"></span>

[int](class_int.md#class_int) **font_get_msdf_size** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_msdf_size)

Returns source font size used to generate MSDF textures.

---

<span id="class_TextServer_method_font_get_name"></span>

[String](class_string.md#class_String) **font_get_name** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_name)

Returns font family name.

---

<span id="class_TextServer_method_font_get_opentype_feature_overrides"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **font_get_opentype_feature_overrides** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_opentype_feature_overrides)

Returns font OpenType feature set override.

---

<span id="class_TextServer_method_font_get_ot_name_strings"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **font_get_ot_name_strings** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_ot_name_strings)

Returns [Dictionary](class_dictionary.md#class_Dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---

<span id="class_TextServer_method_font_get_oversampling"></span>

[float](class_float.md#class_float) **font_get_oversampling** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_oversampling)

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class_Viewport_property_oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

<span id="class_TextServer_method_font_get_scale"></span>

[float](class_float.md#class_float) **font_get_scale** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_scale)

Returns scaling factor of the color bitmap font.

---

<span id="class_TextServer_method_font_get_script_support_override"></span>

[bool](class_bool.md#class_bool) **font_get_script_support_override** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_font_get_script_support_override)

Returns `true` if support override is enabled for the `script`.

---

<span id="class_TextServer_method_font_get_script_support_overrides"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **font_get_script_support_overrides** ( font_rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_font_get_script_support_overrides)

Returns list of script support overrides.

---

<span id="class_TextServer_method_font_get_size_cache_info"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **font_get_size_cache_info** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_size_cache_info)

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

---

<span id="class_TextServer_method_font_get_size_cache_list"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **font_get_size_cache_list** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_size_cache_list)

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class_Vector2i) with font size and outline size.

---

<span id="class_TextServer_method_font_get_spacing"></span>

[int](class_int.md#class_int) **font_get_spacing** ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_spacing)

Returns the spacing for `spacing` in pixels (not relative to the font size).

---

<span id="class_TextServer_method_font_get_stretch"></span>

[int](class_int.md#class_int) **font_get_stretch** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_stretch)

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

<span id="class_TextServer_method_font_get_style"></span>

*BitField*\[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] **font_get_style** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_style)

Returns font style flags.

---

<span id="class_TextServer_method_font_get_style_name"></span>

[String](class_string.md#class_String) **font_get_style_name** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_style_name)

Returns font style name.

---

<span id="class_TextServer_method_font_get_subpixel_positioning"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **font_get_subpixel_positioning** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_subpixel_positioning)

Returns font subpixel glyph positioning mode.

---

<span id="class_TextServer_method_font_get_supported_chars"></span>

[String](class_string.md#class_String) **font_get_supported_chars** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_supported_chars)

Returns a string containing all the characters available in the font.

---

<span id="class_TextServer_method_font_get_supported_glyphs"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **font_get_supported_glyphs** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_supported_glyphs)

Returns an array containing all glyph indices in the font.

---

<span id="class_TextServer_method_font_get_texture_count"></span>

[int](class_int.md#class_int) **font_get_texture_count** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_texture_count)

Returns number of textures used by font cache entry.

---

<span id="class_TextServer_method_font_get_texture_image"></span>

[Image](class_image.md#class_Image) **font_get_texture_image** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_texture_image)

Returns font cache texture image data.

---

<span id="class_TextServer_method_font_get_texture_offsets"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **font_get_texture_offsets** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_texture_offsets)

Returns array containing glyph packing data.

---

<span id="class_TextServer_method_font_get_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **font_get_transform** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_transform)

Returns 2D transform applied to the font outlines.

---

<span id="class_TextServer_method_font_get_underline_position"></span>

[float](class_float.md#class_float) **font_get_underline_position** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_underline_position)

Returns pixel offset of the underline below the baseline.

---

<span id="class_TextServer_method_font_get_underline_thickness"></span>

[float](class_float.md#class_float) **font_get_underline_thickness** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_underline_thickness)

Returns thickness of the underline in pixels.

---

<span id="class_TextServer_method_font_get_variation_coordinates"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **font_get_variation_coordinates** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_variation_coordinates)

Returns variation coordinates for the specified font cache entry. See [font_supported_variation_list()](class_textserver.md#class_TextServer_method_font_supported_variation_list) for more info.

---

<span id="class_TextServer_method_font_get_weight"></span>

[int](class_int.md#class_int) **font_get_weight** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_get_weight)

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

<span id="class_TextServer_method_font_has_char"></span>

[bool](class_bool.md#class_bool) **font_has_char** ( font_rid: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_has_char)

Returns `true` if a Unicode `char` is available in the font.

---

<span id="class_TextServer_method_font_is_allow_system_fallback"></span>

[bool](class_bool.md#class_bool) **font_is_allow_system_fallback** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_is_allow_system_fallback)

Returns `true` if system fonts can be automatically used as fallbacks.

---

<span id="class_TextServer_method_font_is_force_autohinter"></span>

[bool](class_bool.md#class_bool) **font_is_force_autohinter** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_is_force_autohinter)

Returns `true` if auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only.

---

<span id="class_TextServer_method_font_is_language_supported"></span>

[bool](class_bool.md#class_bool) **font_is_language_supported** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_is_language_supported)

Returns `true` if the font supports the given language (as a ISO 639 code).

---

<span id="class_TextServer_method_font_is_modulate_color_glyphs"></span>

[bool](class_bool.md#class_bool) **font_is_modulate_color_glyphs** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_is_modulate_color_glyphs)

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

---

<span id="class_TextServer_method_font_is_multichannel_signed_distance_field"></span>

[bool](class_bool.md#class_bool) **font_is_multichannel_signed_distance_field** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_is_multichannel_signed_distance_field)

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---

<span id="class_TextServer_method_font_is_script_supported"></span>

[bool](class_bool.md#class_bool) **font_is_script_supported** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_is_script_supported)

Returns `true` if the font supports the given script (as a ISO 15924 code).

---

<span id="class_TextServer_method_font_remove_glyph"></span>

void **font_remove_glyph** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_remove_glyph)

Removes specified rendered glyph information from the cache entry.

 **Note:** This function will not remove textures associated with the glyphs, use [font_remove_texture()](class_textserver.md#class_TextServer_method_font_remove_texture) to remove them manually.

---

<span id="class_TextServer_method_font_remove_kerning"></span>

void **font_remove_kerning** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_textserver.md#class_TextServer_method_font_remove_kerning)

Removes kerning override for the pair of glyphs.

---

<span id="class_TextServer_method_font_remove_language_support_override"></span>

void **font_remove_language_support_override** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_font_remove_language_support_override)

Remove language support override.

---

<span id="class_TextServer_method_font_remove_script_support_override"></span>

void **font_remove_script_support_override** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_font_remove_script_support_override)

Removes script support override.

---

<span id="class_TextServer_method_font_remove_size_cache"></span>

void **font_remove_size_cache** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_textserver.md#class_TextServer_method_font_remove_size_cache)

Removes specified font size from the cache entry.

---

<span id="class_TextServer_method_font_remove_texture"></span>

void **font_remove_texture** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_remove_texture)

Removes specified texture from the cache entry.

 **Note:** This function will not remove glyphs associated with the texture, remove them manually, using [font_remove_glyph()](class_textserver.md#class_TextServer_method_font_remove_glyph).

---

<span id="class_TextServer_method_font_render_glyph"></span>

void **font_render_glyph** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), index: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_render_glyph)

Renders specified glyph to the font cache texture.

---

<span id="class_TextServer_method_font_render_range"></span>

void **font_render_range** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_render_range)

Renders the range of characters to the font cache texture.

---

<span id="class_TextServer_method_font_set_allow_system_fallback"></span>

void **font_set_allow_system_fallback** ( font_rid: [RID](class_rid.md#class_RID), allow_system_fallback: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_allow_system_fallback)

If set to `true`, system fonts can be automatically used as fallbacks.

---

<span id="class_TextServer_method_font_set_antialiasing"></span>

void **font_set_antialiasing** ( font_rid: [RID](class_rid.md#class_RID), antialiasing: [FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) ) [🔗](class_textserver.md#class_TextServer_method_font_set_antialiasing)

Sets font anti-aliasing mode.

---

<span id="class_TextServer_method_font_set_ascent"></span>

void **font_set_ascent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), ascent: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_ascent)

Sets the font ascent (number of pixels above the baseline).

---

<span id="class_TextServer_method_font_set_baseline_offset"></span>

void **font_set_baseline_offset** ( font_rid: [RID](class_rid.md#class_RID), baseline_offset: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_baseline_offset)

Sets extra baseline offset (as a fraction of font height).

---

<span id="class_TextServer_method_font_set_data"></span>

void **font_set_data** ( font_rid: [RID](class_rid.md#class_RID), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_textserver.md#class_TextServer_method_font_set_data)

Sets font source data, e.g contents of the dynamic font source file.

---

<span id="class_TextServer_method_font_set_descent"></span>

void **font_set_descent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), descent: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_descent)

Sets the font descent (number of pixels below the baseline).

---

<span id="class_TextServer_method_font_set_disable_embedded_bitmaps"></span>

void **font_set_disable_embedded_bitmaps** ( font_rid: [RID](class_rid.md#class_RID), disable_embedded_bitmaps: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_disable_embedded_bitmaps)

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---

<span id="class_TextServer_method_font_set_embolden"></span>

void **font_set_embolden** ( font_rid: [RID](class_rid.md#class_RID), strength: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_embolden)

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---

<span id="class_TextServer_method_font_set_face_index"></span>

void **font_set_face_index** ( font_rid: [RID](class_rid.md#class_RID), face_index: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_face_index)

Sets an active face index in the TrueType / OpenType collection.

---

<span id="class_TextServer_method_font_set_fixed_size"></span>

void **font_set_fixed_size** ( font_rid: [RID](class_rid.md#class_RID), fixed_size: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_fixed_size)

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

---

<span id="class_TextServer_method_font_set_fixed_size_scale_mode"></span>

void **font_set_fixed_size_scale_mode** ( font_rid: [RID](class_rid.md#class_RID), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) ) [🔗](class_textserver.md#class_TextServer_method_font_set_fixed_size_scale_mode)

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

---

<span id="class_TextServer_method_font_set_force_autohinter"></span>

void **font_set_force_autohinter** ( font_rid: [RID](class_rid.md#class_RID), force_autohinter: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_force_autohinter)

If set to `true` auto-hinting is preferred over font built-in hinting.

---

<span id="class_TextServer_method_font_set_generate_mipmaps"></span>

void **font_set_generate_mipmaps** ( font_rid: [RID](class_rid.md#class_RID), generate_mipmaps: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_generate_mipmaps)

If set to `true` font texture mipmap generation is enabled.

---

<span id="class_TextServer_method_font_set_global_oversampling"></span>

void **font_set_global_oversampling** ( oversampling: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_global_oversampling)

**Deprecated:** Use [Viewport](class_viewport.md#class_Viewport) oversampling, or the `oversampling` argument of the `draw_*` methods instead.

This method does nothing.

---

<span id="class_TextServer_method_font_set_glyph_advance"></span>

void **font_set_glyph_advance** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int), advance: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_textserver.md#class_TextServer_method_font_set_glyph_advance)

Sets glyph advance (offset of the next glyph).

 **Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---

<span id="class_TextServer_method_font_set_glyph_offset"></span>

void **font_set_glyph_offset** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), offset: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_textserver.md#class_TextServer_method_font_set_glyph_offset)

Sets glyph offset from the baseline.

---

<span id="class_TextServer_method_font_set_glyph_size"></span>

void **font_set_glyph_size** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), gl_size: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_textserver.md#class_TextServer_method_font_set_glyph_size)

Sets size of the glyph.

---

<span id="class_TextServer_method_font_set_glyph_texture_idx"></span>

void **font_set_glyph_texture_idx** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), texture_idx: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_glyph_texture_idx)

Sets index of the cache texture containing the glyph.

---

<span id="class_TextServer_method_font_set_glyph_uv_rect"></span>

void **font_set_glyph_uv_rect** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), uv_rect: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_textserver.md#class_TextServer_method_font_set_glyph_uv_rect)

Sets rectangle in the cache texture containing the glyph.

---

<span id="class_TextServer_method_font_set_hinting"></span>

void **font_set_hinting** ( font_rid: [RID](class_rid.md#class_RID), hinting: [Hinting](class_textserver.md#enum_TextServer_Hinting) ) [🔗](class_textserver.md#class_TextServer_method_font_set_hinting)

Sets font hinting mode. Used by dynamic fonts only.

---

<span id="class_TextServer_method_font_set_keep_rounding_remainders"></span>

void **font_set_keep_rounding_remainders** ( font_rid: [RID](class_rid.md#class_RID), keep_rounding_remainders: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_keep_rounding_remainders)

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

<span id="class_TextServer_method_font_set_kerning"></span>

void **font_set_kerning** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i), kerning: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_textserver.md#class_TextServer_method_font_set_kerning)

Sets kerning for the pair of glyphs.

---

<span id="class_TextServer_method_font_set_language_support_override"></span>

void **font_set_language_support_override** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_language_support_override)

Adds override for [font_is_language_supported()](class_textserver.md#class_TextServer_method_font_is_language_supported).

---

<span id="class_TextServer_method_font_set_modulate_color_glyphs"></span>

void **font_set_modulate_color_glyphs** ( font_rid: [RID](class_rid.md#class_RID), force_autohinter: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_modulate_color_glyphs)

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---

<span id="class_TextServer_method_font_set_msdf_pixel_range"></span>

void **font_set_msdf_pixel_range** ( font_rid: [RID](class_rid.md#class_RID), msdf_pixel_range: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_msdf_pixel_range)

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

---

<span id="class_TextServer_method_font_set_msdf_size"></span>

void **font_set_msdf_size** ( font_rid: [RID](class_rid.md#class_RID), msdf_size: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_msdf_size)

Sets source font size used to generate MSDF textures.

---

<span id="class_TextServer_method_font_set_multichannel_signed_distance_field"></span>

void **font_set_multichannel_signed_distance_field** ( font_rid: [RID](class_rid.md#class_RID), msdf: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_multichannel_signed_distance_field)

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

 **Note:** MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.

---

<span id="class_TextServer_method_font_set_name"></span>

void **font_set_name** ( font_rid: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_font_set_name)

Sets the font family name.

---

<span id="class_TextServer_method_font_set_opentype_feature_overrides"></span>

void **font_set_opentype_feature_overrides** ( font_rid: [RID](class_rid.md#class_RID), overrides: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_textserver.md#class_TextServer_method_font_set_opentype_feature_overrides)

Sets font OpenType feature set override.

---

<span id="class_TextServer_method_font_set_oversampling"></span>

void **font_set_oversampling** ( font_rid: [RID](class_rid.md#class_RID), oversampling: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_oversampling)

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class_Viewport_property_oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

<span id="class_TextServer_method_font_set_scale"></span>

void **font_set_scale** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), scale: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_scale)

Sets scaling factor of the color bitmap font.

---

<span id="class_TextServer_method_font_set_script_support_override"></span>

void **font_set_script_support_override** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_font_set_script_support_override)

Adds override for [font_is_script_supported()](class_textserver.md#class_TextServer_method_font_is_script_supported).

---

<span id="class_TextServer_method_font_set_spacing"></span>

void **font_set_spacing** ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_spacing)

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---

<span id="class_TextServer_method_font_set_stretch"></span>

void **font_set_stretch** ( font_rid: [RID](class_rid.md#class_RID), weight: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_stretch)

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

 **Note:** This value is used for font matching only and will not affect font rendering. Use [font_set_face_index()](class_textserver.md#class_TextServer_method_font_set_face_index), [font_set_variation_coordinates()](class_textserver.md#class_TextServer_method_font_set_variation_coordinates), or [font_set_transform()](class_textserver.md#class_TextServer_method_font_set_transform) instead.

---

<span id="class_TextServer_method_font_set_style"></span>

void **font_set_style** ( font_rid: [RID](class_rid.md#class_RID), style: *BitField*\[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] ) [🔗](class_textserver.md#class_TextServer_method_font_set_style)

Sets the font style flags.

 **Note:** This value is used for font matching only and will not affect font rendering. Use [font_set_face_index()](class_textserver.md#class_TextServer_method_font_set_face_index), [font_set_variation_coordinates()](class_textserver.md#class_TextServer_method_font_set_variation_coordinates), [font_set_embolden()](class_textserver.md#class_TextServer_method_font_set_embolden), or [font_set_transform()](class_textserver.md#class_TextServer_method_font_set_transform) instead.

---

<span id="class_TextServer_method_font_set_style_name"></span>

void **font_set_style_name** ( font_rid: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_font_set_style_name)

Sets the font style name.

---

<span id="class_TextServer_method_font_set_subpixel_positioning"></span>

void **font_set_subpixel_positioning** ( font_rid: [RID](class_rid.md#class_RID), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) ) [🔗](class_textserver.md#class_TextServer_method_font_set_subpixel_positioning)

Sets font subpixel glyph positioning mode.

---

<span id="class_TextServer_method_font_set_texture_image"></span>

void **font_set_texture_image** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), image: [Image](class_image.md#class_Image) ) [🔗](class_textserver.md#class_TextServer_method_font_set_texture_image)

Sets font cache texture image data.

---

<span id="class_TextServer_method_font_set_texture_offsets"></span>

void **font_set_texture_offsets** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), offset: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_textserver.md#class_TextServer_method_font_set_texture_offsets)

Sets array containing glyph packing data.

---

<span id="class_TextServer_method_font_set_transform"></span>

void **font_set_transform** ( font_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_textserver.md#class_TextServer_method_font_set_transform)

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

For example, to simulate italic typeface by slanting, apply the following transform `Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)`.

---

<span id="class_TextServer_method_font_set_underline_position"></span>

void **font_set_underline_position** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_position: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_underline_position)

Sets pixel offset of the underline below the baseline.

---

<span id="class_TextServer_method_font_set_underline_thickness"></span>

void **font_set_underline_thickness** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_thickness: [float](class_float.md#class_float) ) [🔗](class_textserver.md#class_TextServer_method_font_set_underline_thickness)

Sets thickness of the underline in pixels.

---

<span id="class_TextServer_method_font_set_variation_coordinates"></span>

void **font_set_variation_coordinates** ( font_rid: [RID](class_rid.md#class_RID), variation_coordinates: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_textserver.md#class_TextServer_method_font_set_variation_coordinates)

Sets variation coordinates for the specified font cache entry. See [font_supported_variation_list()](class_textserver.md#class_TextServer_method_font_supported_variation_list) for more info.

---

<span id="class_TextServer_method_font_set_weight"></span>

void **font_set_weight** ( font_rid: [RID](class_rid.md#class_RID), weight: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_font_set_weight)

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

 **Note:** This value is used for font matching only and will not affect font rendering. Use [font_set_face_index()](class_textserver.md#class_TextServer_method_font_set_face_index), [font_set_variation_coordinates()](class_textserver.md#class_TextServer_method_font_set_variation_coordinates), or [font_set_embolden()](class_textserver.md#class_TextServer_method_font_set_embolden) instead.

---

<span id="class_TextServer_method_font_supported_feature_list"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **font_supported_feature_list** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_supported_feature_list)

Returns the dictionary of the supported OpenType features.

---

<span id="class_TextServer_method_font_supported_variation_list"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **font_supported_variation_list** ( font_rid: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_font_supported_variation_list)

Returns the dictionary of the supported OpenType variation coordinates.

---

<span id="class_TextServer_method_format_number"></span>

[String](class_string.md#class_String) **format_number** ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_format_number)

**Deprecated:** Use [TranslationServer.format_number()](class_translationserver.md#class_TranslationServer_method_format_number) instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

---

<span id="class_TextServer_method_free_rid"></span>

void **free_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_free_rid)

Frees an object created by this **TextServer**.

---

<span id="class_TextServer_method_get_features"></span>

[int](class_int.md#class_int) **get_features** ( ) *const* [🔗](class_textserver.md#class_TextServer_method_get_features)

Returns text server features, see [Feature](class_textserver.md#enum_TextServer_Feature).

---

<span id="class_TextServer_method_get_hex_code_box_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_hex_code_box_size** ( size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_get_hex_code_box_size)

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

---

<span id="class_TextServer_method_get_name"></span>

[String](class_string.md#class_String) **get_name** ( ) *const* [🔗](class_textserver.md#class_TextServer_method_get_name)

Returns the name of the server interface.

---

<span id="class_TextServer_method_get_support_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_support_data** ( ) *const* [🔗](class_textserver.md#class_TextServer_method_get_support_data)

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

---

<span id="class_TextServer_method_get_support_data_filename"></span>

[String](class_string.md#class_String) **get_support_data_filename** ( ) *const* [🔗](class_textserver.md#class_TextServer_method_get_support_data_filename)

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

---

<span id="class_TextServer_method_get_support_data_info"></span>

[String](class_string.md#class_String) **get_support_data_info** ( ) *const* [🔗](class_textserver.md#class_TextServer_method_get_support_data_info)

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

---

<span id="class_TextServer_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_has)

Returns `true` if `rid` is valid resource owned by this text server.

---

<span id="class_TextServer_method_has_feature"></span>

[bool](class_bool.md#class_bool) **has_feature** ( feature: [Feature](class_textserver.md#enum_TextServer_Feature) ) *const* [🔗](class_textserver.md#class_TextServer_method_has_feature)

Returns `true` if the server supports a feature.

---

<span id="class_TextServer_method_is_confusable"></span>

[int](class_int.md#class_int) **is_confusable** ( string: [String](class_string.md#class_String), dict: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *const* [🔗](class_textserver.md#class_TextServer_method_is_confusable)

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

 **Note:** This method doesn't detect invisible characters, for spoof detection use it in combination with [spoof_check()](class_textserver.md#class_TextServer_method_spoof_check).

 **Note:** Always returns `-1` if the server does not support the [FEATURE_UNICODE_SECURITY](class_textserver.md#class_TextServer_constant_FEATURE_UNICODE_SECURITY) feature.

---

<span id="class_TextServer_method_is_locale_right_to_left"></span>

[bool](class_bool.md#class_bool) **is_locale_right_to_left** ( locale: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_is_locale_right_to_left)

Returns `true` if locale is right-to-left.

---

<span id="class_TextServer_method_is_locale_using_support_data"></span>

[bool](class_bool.md#class_bool) **is_locale_using_support_data** ( locale: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_is_locale_using_support_data)

Returns `true` if the locale requires text server support data for line/word breaking.

---

<span id="class_TextServer_method_is_valid_identifier"></span>

[bool](class_bool.md#class_bool) **is_valid_identifier** ( string: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_is_valid_identifier)

Returns `true` if `string` is a valid identifier.

If the text server supports the [FEATURE_UNICODE_IDENTIFIERS](class_textserver.md#class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS) feature, a valid identifier must:

- Conform to normalization form C.

- Begin with a Unicode character of class XID_Start or `"_"`.

- May contain Unicode characters of class XID_Continue in the other positions.

- Use UAX #31 recommended scripts only (mixed scripts are allowed).

If the [FEATURE_UNICODE_IDENTIFIERS](class_textserver.md#class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS) feature is not supported, a valid identifier must:

- Begin with a Unicode character of class XID_Start or `"_"`.

- May contain Unicode characters of class XID_Continue in the other positions.

---

<span id="class_TextServer_method_is_valid_letter"></span>

[bool](class_bool.md#class_bool) **is_valid_letter** ( unicode: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_is_valid_letter)

Returns `true` if the given code point is a valid letter, i.e. it belongs to the Unicode category "L".

---

<span id="class_TextServer_method_load_support_data"></span>

[bool](class_bool.md#class_bool) **load_support_data** ( filename: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_load_support_data)

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

 **Note:** This function should be called before any other TextServer functions used, otherwise it won't have any effect.

---

<span id="class_TextServer_method_name_to_tag"></span>

[int](class_int.md#class_int) **name_to_tag** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_name_to_tag)

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

---

<span id="class_TextServer_method_parse_number"></span>

[String](class_string.md#class_String) **parse_number** ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_parse_number)

**Deprecated:** Use [TranslationServer.parse_number()](class_translationserver.md#class_TranslationServer_method_parse_number) instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

---

<span id="class_TextServer_method_parse_structured_text"></span>

[Array](class_array.md#class_Array)\[[Vector3i](class_vector3i.md#class_Vector3i)\] **parse_structured_text** ( parser_type: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser), args: [Array](class_array.md#class_Array), text: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_parse_structured_text)

Default implementation of the BiDi algorithm override function.

---

<span id="class_TextServer_method_percent_sign"></span>

[String](class_string.md#class_String) **percent_sign** ( language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_percent_sign)

**Deprecated:** Use [TranslationServer.get_percent_sign()](class_translationserver.md#class_TranslationServer_method_get_percent_sign) instead.

Returns the percent sign used in the given `language`.

If `language` is an empty string, the active locale will be used.

---

<span id="class_TextServer_method_save_support_data"></span>

[bool](class_bool.md#class_bool) **save_support_data** ( filename: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_save_support_data)

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

 **Note:** This function is used by during project export, to include TextServer database.

---

<span id="class_TextServer_method_shaped_get_run_count"></span>

[int](class_int.md#class_int) **shaped_get_run_count** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_count)

Returns the number of uniform text runs in the buffer.

---

<span id="class_TextServer_method_shaped_get_run_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **shaped_get_run_direction** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_direction)

Returns the direction of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_run_font_rid"></span>

[RID](class_rid.md#class_RID) **shaped_get_run_font_rid** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_font_rid)

Returns the font RID of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_run_font_size"></span>

[int](class_int.md#class_int) **shaped_get_run_font_size** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_font_size)

Returns the font size of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_run_language"></span>

[String](class_string.md#class_String) **shaped_get_run_language** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_language)

Returns the language of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_run_object"></span>

[Variant](class_variant.md#class_Variant) **shaped_get_run_object** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_object)

Returns the embedded object of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_run_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **shaped_get_run_range** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_range)

Returns the source text range of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_run_text"></span>

[String](class_string.md#class_String) **shaped_get_run_text** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_run_text)

Returns the source text of the `index` text run (in visual order).

---

<span id="class_TextServer_method_shaped_get_span_count"></span>

[int](class_int.md#class_int) **shaped_get_span_count** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_span_count)

Returns number of text spans added using [shaped_text_add_string()](class_textserver.md#class_TextServer_method_shaped_text_add_string) or [shaped_text_add_object()](class_textserver.md#class_TextServer_method_shaped_text_add_object).

---

<span id="class_TextServer_method_shaped_get_span_embedded_object"></span>

[Variant](class_variant.md#class_Variant) **shaped_get_span_embedded_object** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_span_embedded_object)

Returns text embedded object key.

---

<span id="class_TextServer_method_shaped_get_span_meta"></span>

[Variant](class_variant.md#class_Variant) **shaped_get_span_meta** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_span_meta)

Returns text span metadata.

---

<span id="class_TextServer_method_shaped_get_span_object"></span>

[Variant](class_variant.md#class_Variant) **shaped_get_span_object** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_span_object)

Returns the text span embedded object key.

---

<span id="class_TextServer_method_shaped_get_span_text"></span>

[String](class_string.md#class_String) **shaped_get_span_text** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_span_text)

Returns the text span source text.

---

<span id="class_TextServer_method_shaped_get_text"></span>

[String](class_string.md#class_String) **shaped_get_text** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_get_text)

Returns the text buffer source text, including object replacement characters.

---

<span id="class_TextServer_method_shaped_set_span_update_font"></span>

void **shaped_set_span_update_font** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) [🔗](class_textserver.md#class_TextServer_method_shaped_set_span_update_font)

Changes text span font, font size, and OpenType features, without changing the text.

---

<span id="class_TextServer_method_shaped_text_add_object"></span>

[bool](class_bool.md#class_bool) **shaped_text_add_object** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, length: [int](class_int.md#class_int) = 1, baseline: [float](class_float.md#class_float) = 0.0 ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_add_object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

<span id="class_TextServer_method_shaped_text_add_string"></span>

[bool](class_bool.md#class_bool) **shaped_text_add_string** ( shaped: [RID](class_rid.md#class_RID), text: [String](class_string.md#class_String), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary) = {}, language: [String](class_string.md#class_String) = "", meta: [Variant](class_variant.md#class_Variant) = null ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_add_string)

Adds text span and font to draw it to the text buffer.

---

<span id="class_TextServer_method_shaped_text_clear"></span>

void **shaped_text_clear** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_clear)

Clears text buffer (removes text and inline objects).

---

<span id="class_TextServer_method_shaped_text_closest_character_pos"></span>

[int](class_int.md#class_int) **shaped_text_closest_character_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_closest_character_pos)

Returns composite character position closest to the `pos`.

---

<span id="class_TextServer_method_shaped_text_draw"></span>

void **shaped_text_draw** ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float) = -1, clip_r: [float](class_float.md#class_float) = -1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_draw)

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

 `clip_l` and `clip_r` are offsets relative to `pos`, going to the right in horizontal layout and downward in vertical layout. If `clip_l` is not negative, glyphs starting before the offset are clipped. If `clip_r` is not negative, glyphs ending after the offset are clipped.

---

<span id="class_TextServer_method_shaped_text_draw_outline"></span>

void **shaped_text_draw_outline** ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float) = -1, clip_r: [float](class_float.md#class_float) = -1, outline_size: [int](class_int.md#class_int) = 1, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class_float) = 0.0 ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_draw_outline)

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

 `clip_l` and `clip_r` are offsets relative to `pos`, going to the right in horizontal layout and downward in vertical layout. If `clip_l` is not negative, glyphs starting before the offset are clipped. If `clip_r` is not negative, glyphs ending after the offset are clipped.

---

<span id="class_TextServer_method_shaped_text_duplicate"></span>

[RID](class_rid.md#class_RID) **shaped_text_duplicate** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_duplicate)

Duplicates shaped text buffer.

---

<span id="class_TextServer_method_shaped_text_fit_to_width"></span>

[float](class_float.md#class_float) **shaped_text_fit_to_width** ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), justification_flags: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] = 3 ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_fit_to_width)

Adjusts text width to fit to specified width, returns new text width.

---

<span id="class_TextServer_method_shaped_text_get_ascent"></span>

[float](class_float.md#class_float) **shaped_text_get_ascent** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_ascent)

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

 **Note:** Overall ascent can be higher than font ascent, if some glyphs are displaced from the baseline.

---

<span id="class_TextServer_method_shaped_text_get_carets"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **shaped_text_get_carets** ( shaped: [RID](class_rid.md#class_RID), position: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_carets)

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

---

<span id="class_TextServer_method_shaped_text_get_character_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **shaped_text_get_character_breaks** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_character_breaks)

Returns array of the composite character boundaries.

---

<span id="class_TextServer_method_shaped_text_get_custom_ellipsis"></span>

[int](class_int.md#class_int) **shaped_text_get_custom_ellipsis** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_custom_ellipsis)

Returns ellipsis character used for text clipping.

---

<span id="class_TextServer_method_shaped_text_get_custom_punctuation"></span>

[String](class_string.md#class_String) **shaped_text_get_custom_punctuation** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_custom_punctuation)

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

<span id="class_TextServer_method_shaped_text_get_descent"></span>

[float](class_float.md#class_float) **shaped_text_get_descent** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_descent)

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

 **Note:** Overall descent can be higher than font descent, if some glyphs are displaced from the baseline.

---

<span id="class_TextServer_method_shaped_text_get_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **shaped_text_get_direction** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_direction)

Returns direction of the text.

---

<span id="class_TextServer_method_shaped_text_get_dominant_direction_in_range"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **shaped_text_get_dominant_direction_in_range** ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_dominant_direction_in_range)

Returns dominant direction of in the range of text.

---

<span id="class_TextServer_method_shaped_text_get_ellipsis_glyph_count"></span>

[int](class_int.md#class_int) **shaped_text_get_ellipsis_glyph_count** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_ellipsis_glyph_count)

Returns number of glyphs in the ellipsis.

---

<span id="class_TextServer_method_shaped_text_get_ellipsis_glyphs"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **shaped_text_get_ellipsis_glyphs** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_ellipsis_glyphs)

Returns array of the glyphs in the ellipsis.

---

<span id="class_TextServer_method_shaped_text_get_ellipsis_pos"></span>

[int](class_int.md#class_int) **shaped_text_get_ellipsis_pos** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_ellipsis_pos)

Returns position of the ellipsis.

---

<span id="class_TextServer_method_shaped_text_get_glyph_count"></span>

[int](class_int.md#class_int) **shaped_text_get_glyph_count** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_glyph_count)

Returns number of glyphs in the buffer.

---

<span id="class_TextServer_method_shaped_text_get_glyphs"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **shaped_text_get_glyphs** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_glyphs)

Returns an array of glyphs in the visual order.

---

<span id="class_TextServer_method_shaped_text_get_grapheme_bounds"></span>

[Vector2](class_vector2.md#class_Vector2) **shaped_text_get_grapheme_bounds** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_grapheme_bounds)

Returns composite character's bounds as offsets from the start of the line.

---

<span id="class_TextServer_method_shaped_text_get_inferred_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **shaped_text_get_inferred_direction** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_inferred_direction)

Returns direction of the text, inferred by the BiDi algorithm.

---

<span id="class_TextServer_method_shaped_text_get_line_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **shaped_text_get_line_breaks** ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), start: [int](class_int.md#class_int) = 0, break_flags: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] = 3 ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_line_breaks)

Breaks text to the lines and returns character ranges for each line.

---

<span id="class_TextServer_method_shaped_text_get_line_breaks_adv"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **shaped_text_get_line_breaks_adv** ( shaped: [RID](class_rid.md#class_RID), width: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), start: [int](class_int.md#class_int) = 0, once: [bool](class_bool.md#class_bool) = true, break_flags: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] = 3 ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_line_breaks_adv)

Breaks text to the lines and columns. Returns character ranges for each segment.

---

<span id="class_TextServer_method_shaped_text_get_object_glyph"></span>

[int](class_int.md#class_int) **shaped_text_get_object_glyph** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_object_glyph)

Returns the glyph index of the inline object.

---

<span id="class_TextServer_method_shaped_text_get_object_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **shaped_text_get_object_range** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_object_range)

Returns the character range of the inline object.

---

<span id="class_TextServer_method_shaped_text_get_object_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **shaped_text_get_object_rect** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_object_rect)

Returns bounding rectangle of the inline object.

---

<span id="class_TextServer_method_shaped_text_get_objects"></span>

[Array](class_array.md#class_Array) **shaped_text_get_objects** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_objects)

Returns array of inline objects.

---

<span id="class_TextServer_method_shaped_text_get_orientation"></span>

[Orientation](class_textserver.md#enum_TextServer_Orientation) **shaped_text_get_orientation** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_orientation)

Returns text orientation.

---

<span id="class_TextServer_method_shaped_text_get_parent"></span>

[RID](class_rid.md#class_RID) **shaped_text_get_parent** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_parent)

Returns the parent buffer from which the substring originates.

---

<span id="class_TextServer_method_shaped_text_get_preserve_control"></span>

[bool](class_bool.md#class_bool) **shaped_text_get_preserve_control** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_preserve_control)

Returns `true` if text buffer is configured to display control characters.

---

<span id="class_TextServer_method_shaped_text_get_preserve_invalid"></span>

[bool](class_bool.md#class_bool) **shaped_text_get_preserve_invalid** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_preserve_invalid)

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

 **Note:** If set to `false`, nothing is displayed in place of invalid characters.

---

<span id="class_TextServer_method_shaped_text_get_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **shaped_text_get_range** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_range)

Returns substring buffer character range in the parent buffer.

---

<span id="class_TextServer_method_shaped_text_get_selection"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **shaped_text_get_selection** ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_selection)

Returns selection rectangles for the specified character range.

---

<span id="class_TextServer_method_shaped_text_get_size"></span>

[Vector2](class_vector2.md#class_Vector2) **shaped_text_get_size** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_size)

Returns size of the text.

---

<span id="class_TextServer_method_shaped_text_get_spacing"></span>

[int](class_int.md#class_int) **shaped_text_get_spacing** ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_spacing)

Returns extra spacing added between glyphs or lines in pixels.

---

<span id="class_TextServer_method_shaped_text_get_trim_pos"></span>

[int](class_int.md#class_int) **shaped_text_get_trim_pos** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_trim_pos)

Returns the position of the overrun trim.

---

<span id="class_TextServer_method_shaped_text_get_underline_position"></span>

[float](class_float.md#class_float) **shaped_text_get_underline_position** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_underline_position)

Returns pixel offset of the underline below the baseline.

---

<span id="class_TextServer_method_shaped_text_get_underline_thickness"></span>

[float](class_float.md#class_float) **shaped_text_get_underline_thickness** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_underline_thickness)

Returns thickness of the underline.

---

<span id="class_TextServer_method_shaped_text_get_width"></span>

[float](class_float.md#class_float) **shaped_text_get_width** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_width)

Returns width (for horizontal layout) or height (for vertical) of the text.

---

<span id="class_TextServer_method_shaped_text_get_word_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **shaped_text_get_word_breaks** ( shaped: [RID](class_rid.md#class_RID), grapheme_flags: *BitField*\[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\] = 264, skip_grapheme_flags: *BitField*\[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\] = 4 ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_get_word_breaks)

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

---

<span id="class_TextServer_method_shaped_text_has_object"></span>

[bool](class_bool.md#class_bool) **shaped_text_has_object** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_has_object)

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---

<span id="class_TextServer_method_shaped_text_has_visible_chars"></span>

[bool](class_bool.md#class_bool) **shaped_text_has_visible_chars** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_has_visible_chars)

Returns `true` if text buffer contains any visible characters.

---

<span id="class_TextServer_method_shaped_text_hit_test_grapheme"></span>

[int](class_int.md#class_int) **shaped_text_hit_test_grapheme** ( shaped: [RID](class_rid.md#class_RID), coords: [float](class_float.md#class_float) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_hit_test_grapheme)

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

---

<span id="class_TextServer_method_shaped_text_hit_test_position"></span>

[int](class_int.md#class_int) **shaped_text_hit_test_position** ( shaped: [RID](class_rid.md#class_RID), coords: [float](class_float.md#class_float) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_hit_test_position)

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---

<span id="class_TextServer_method_shaped_text_is_ready"></span>

[bool](class_bool.md#class_bool) **shaped_text_is_ready** ( shaped: [RID](class_rid.md#class_RID) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_is_ready)

Returns `true` if buffer is successfully shaped.

---

<span id="class_TextServer_method_shaped_text_next_character_pos"></span>

[int](class_int.md#class_int) **shaped_text_next_character_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_next_character_pos)

Returns composite character end position closest to the `pos`.

---

<span id="class_TextServer_method_shaped_text_next_grapheme_pos"></span>

[int](class_int.md#class_int) **shaped_text_next_grapheme_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_next_grapheme_pos)

Returns grapheme end position closest to the `pos`.

---

<span id="class_TextServer_method_shaped_text_overrun_trim_to_width"></span>

void **shaped_text_overrun_trim_to_width** ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float) = 0, overrun_trim_flags: *BitField*\[[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag)\] = 0 ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_overrun_trim_to_width)

Trims text if it exceeds the given width.

---

<span id="class_TextServer_method_shaped_text_prev_character_pos"></span>

[int](class_int.md#class_int) **shaped_text_prev_character_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_prev_character_pos)

Returns composite character start position closest to the `pos`.

---

<span id="class_TextServer_method_shaped_text_prev_grapheme_pos"></span>

[int](class_int.md#class_int) **shaped_text_prev_grapheme_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_prev_grapheme_pos)

Returns grapheme start position closest to the `pos`.

---

<span id="class_TextServer_method_shaped_text_resize_object"></span>

[bool](class_bool.md#class_bool) **shaped_text_resize_object** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment = 5, baseline: [float](class_float.md#class_float) = 0.0 ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_resize_object)

Sets new size and alignment of embedded object.

---

<span id="class_TextServer_method_shaped_text_set_bidi_override"></span>

void **shaped_text_set_bidi_override** ( shaped: [RID](class_rid.md#class_RID), override: [Array](class_array.md#class_Array) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_bidi_override)

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---

<span id="class_TextServer_method_shaped_text_set_custom_ellipsis"></span>

void **shaped_text_set_custom_ellipsis** ( shaped: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_custom_ellipsis)

Sets ellipsis character used for text clipping.

---

<span id="class_TextServer_method_shaped_text_set_custom_punctuation"></span>

void **shaped_text_set_custom_punctuation** ( shaped: [RID](class_rid.md#class_RID), punct: [String](class_string.md#class_String) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_custom_punctuation)

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

<span id="class_TextServer_method_shaped_text_set_direction"></span>

void **shaped_text_set_direction** ( shaped: [RID](class_rid.md#class_RID), direction: [Direction](class_textserver.md#enum_TextServer_Direction) = 0 ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_direction)

Sets desired text direction. If set to [DIRECTION_AUTO](class_textserver.md#class_TextServer_constant_DIRECTION_AUTO), direction will be detected based on the buffer contents and current locale.

 **Note:** Direction is ignored if server does not support [FEATURE_BIDI_LAYOUT](class_textserver.md#class_TextServer_constant_FEATURE_BIDI_LAYOUT) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

---

<span id="class_TextServer_method_shaped_text_set_orientation"></span>

void **shaped_text_set_orientation** ( shaped: [RID](class_rid.md#class_RID), orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) = 0 ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_orientation)

Sets desired text orientation.

 **Note:** Orientation is ignored if server does not support [FEATURE_VERTICAL_LAYOUT](class_textserver.md#class_TextServer_constant_FEATURE_VERTICAL_LAYOUT) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

---

<span id="class_TextServer_method_shaped_text_set_preserve_control"></span>

void **shaped_text_set_preserve_control** ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_preserve_control)

If set to `true` text buffer will display control characters.

---

<span id="class_TextServer_method_shaped_text_set_preserve_invalid"></span>

void **shaped_text_set_preserve_invalid** ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_preserve_invalid)

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

---

<span id="class_TextServer_method_shaped_text_set_spacing"></span>

void **shaped_text_set_spacing** ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_set_spacing)

Sets extra spacing added between glyphs or lines in pixels.

---

<span id="class_TextServer_method_shaped_text_shape"></span>

[bool](class_bool.md#class_bool) **shaped_text_shape** ( shaped: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_shape)

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

 **Note:** It is not necessary to call this function manually, buffer will be shaped automatically as soon as any of its output data is requested.

---

<span id="class_TextServer_method_shaped_text_sort_logical"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **shaped_text_sort_logical** ( shaped: [RID](class_rid.md#class_RID) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_sort_logical)

Returns text glyphs in the logical order.

---

<span id="class_TextServer_method_shaped_text_substr"></span>

[RID](class_rid.md#class_RID) **shaped_text_substr** ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), length: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_shaped_text_substr)

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

---

<span id="class_TextServer_method_shaped_text_tab_align"></span>

[float](class_float.md#class_float) **shaped_text_tab_align** ( shaped: [RID](class_rid.md#class_RID), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_textserver.md#class_TextServer_method_shaped_text_tab_align)

Aligns shaped text to the given tab-stops.

---

<span id="class_TextServer_method_spoof_check"></span>

[bool](class_bool.md#class_bool) **spoof_check** ( string: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_spoof_check)

Returns `true` if `string` is likely to be an attempt at confusing the reader.

 **Note:** Always returns `false` if the server does not support the [FEATURE_UNICODE_SECURITY](class_textserver.md#class_TextServer_constant_FEATURE_UNICODE_SECURITY) feature.

---

<span id="class_TextServer_method_string_get_character_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **string_get_character_breaks** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_string_get_character_breaks)

Returns array of the composite character boundaries.

::

    var ts = TextServerManager.get_primary_interface()
    print(ts.string_get_character_breaks("Test ❤️‍🔥 Test")) # Prints [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14]

---

<span id="class_TextServer_method_string_get_word_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **string_get_word_breaks** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "", chars_per_line: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textserver.md#class_TextServer_method_string_get_word_breaks)

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

When `chars_per_line` is greater than zero, line break boundaries are returned instead.

::

    var ts = TextServerManager.get_primary_interface()
    # Corresponds to the substrings "The", "Godot", "Engine", and "4".
    print(ts.string_get_word_breaks("The Godot Engine, 4")) # Prints [0, 3, 4, 9, 10, 16, 18, 19]
    # Corresponds to the substrings "The", "Godot", "Engin", and "e, 4".
    print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 5)) # Prints [0, 3, 4, 9, 10, 15, 15, 19]
    # Corresponds to the substrings "The Godot" and "Engine, 4".
    print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 10)) # Prints [0, 9, 10, 19]

---

<span id="class_TextServer_method_string_to_lower"></span>

[String](class_string.md#class_String) **string_to_lower** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_string_to_lower)

Returns the string converted to `lowercase`.

 **Note:** Casing is locale dependent and context sensitive if server support [FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION](class_textserver.md#class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

 **Note:** The result may be longer or shorter than the original.

---

<span id="class_TextServer_method_string_to_title"></span>

[String](class_string.md#class_String) **string_to_title** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_string_to_title)

Returns the string converted to `Title Case`.

 **Note:** Casing is locale dependent and context sensitive if server support [FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION](class_textserver.md#class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

 **Note:** The result may be longer or shorter than the original.

---

<span id="class_TextServer_method_string_to_upper"></span>

[String](class_string.md#class_String) **string_to_upper** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) = "" ) *const* [🔗](class_textserver.md#class_TextServer_method_string_to_upper)

Returns the string converted to `UPPERCASE`.

 **Note:** Casing is locale dependent and context sensitive if server support [FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION](class_textserver.md#class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION) feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced)).

 **Note:** The result may be longer or shorter than the original.

---

<span id="class_TextServer_method_strip_diacritics"></span>

[String](class_string.md#class_String) **strip_diacritics** ( string: [String](class_string.md#class_String) ) *const* [🔗](class_textserver.md#class_TextServer_method_strip_diacritics)

Strips diacritics from the string.

 **Note:** The result may be longer or shorter than the original.

---

<span id="class_TextServer_method_tag_to_name"></span>

[String](class_string.md#class_String) **tag_to_name** ( tag: [int](class_int.md#class_int) ) *const* [🔗](class_textserver.md#class_TextServer_method_tag_to_name)

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.
