<span id="class_TextServerExtension"></span>

## TextServerExtension

**Inherits:** [TextServer](class_textserver.md#class_TextServer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced), [TextServerDummy](class_textserverdummy.md#class_TextServerDummy), [TextServerFallback](class_textserverfallback.md#class_TextServerFallback)

Base class for custom [TextServer](class_textserver.md#class_TextServer) implementations (plugins).

### Description

External [TextServer](class_textserver.md#class_TextServer) implementations should inherit from this class.

### Methods


| void | [_cleanup](class_textserverextension.md#class_TextServerExtension_private_method__cleanup) ( ) virtual |
| --- | --- |
| [RID](class_rid.md#class_RID) | [_create_font](class_textserverextension.md#class_TextServerExtension_private_method__create_font) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_create_font_linked_variation](class_textserverextension.md#class_TextServerExtension_private_method__create_font_linked_variation) ( font_rid: [RID](class_rid.md#class_RID) ) virtual |
| [RID](class_rid.md#class_RID) | [_create_shaped_text](class_textserverextension.md#class_TextServerExtension_private_method__create_shaped_text) ( direction: [Direction](class_textserver.md#enum_TextServer_Direction), orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) ) | virtual | required |
| void | [_draw_hex_code_box](class_textserverextension.md#class_TextServerExtension_private_method__draw_hex_code_box) ( canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) | virtual | const |
| void | [_font_clear_glyphs](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_glyphs) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | required |
| void | [_font_clear_kerning_map](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_kerning_map) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) virtual |
| void | [_font_clear_size_cache](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_size_cache) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_font_clear_system_fallback_cache](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_system_fallback_cache) ( ) virtual |
| void | [_font_clear_textures](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_textures) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | required |
| void | [_font_draw_glyph](class_textserverextension.md#class_TextServerExtension_private_method__font_draw_glyph) ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) | virtual | required | const |
| void | [_font_draw_glyph_outline](class_textserverextension.md#class_TextServerExtension_private_method__font_draw_glyph_outline) ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), outline_size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) | virtual | required | const |
| [FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) | [_font_get_antialiasing](class_textserverextension.md#class_TextServerExtension_private_method__font_get_antialiasing) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_font_get_ascent](class_textserverextension.md#class_TextServerExtension_private_method__font_get_ascent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_font_get_baseline_offset](class_textserverextension.md#class_TextServerExtension_private_method__font_get_baseline_offset) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_char_from_glyph_index](class_textserverextension.md#class_TextServerExtension_private_method__font_get_char_from_glyph_index) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_index: [int](class_int.md#class_int) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_font_get_descent](class_textserverextension.md#class_TextServerExtension_private_method__font_get_descent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_font_get_disable_embedded_bitmaps](class_textserverextension.md#class_TextServerExtension_private_method__font_get_disable_embedded_bitmaps) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_font_get_embolden](class_textserverextension.md#class_TextServerExtension_private_method__font_get_embolden) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_face_count](class_textserverextension.md#class_TextServerExtension_private_method__font_get_face_count) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_face_index](class_textserverextension.md#class_TextServerExtension_private_method__font_get_face_index) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_fixed_size](class_textserverextension.md#class_TextServerExtension_private_method__font_get_fixed_size) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) | [_font_get_fixed_size_scale_mode](class_textserverextension.md#class_TextServerExtension_private_method__font_get_fixed_size_scale_mode) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_font_get_generate_mipmaps](class_textserverextension.md#class_TextServerExtension_private_method__font_get_generate_mipmaps) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_font_get_global_oversampling](class_textserverextension.md#class_TextServerExtension_private_method__font_get_global_oversampling) ( ) | virtual | const |
| [Vector2](class_vector2.md#class_Vector2) | [_font_get_glyph_advance](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_advance) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_font_get_glyph_contours](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_contours) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_glyph_index](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_index) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), char: [int](class_int.md#class_int), variation_selector: [int](class_int.md#class_int) ) | virtual | required | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_font_get_glyph_list](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_list) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | required | const |
| [Vector2](class_vector2.md#class_Vector2) | [_font_get_glyph_offset](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_offset) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector2](class_vector2.md#class_Vector2) | [_font_get_glyph_size](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_size) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_font_get_glyph_texture_idx](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_texture_idx) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_font_get_glyph_texture_rid](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_texture_rid) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector2](class_vector2.md#class_Vector2) | [_font_get_glyph_texture_size](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_texture_size) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [Rect2](class_rect2.md#class_Rect2) | [_font_get_glyph_uv_rect](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_uv_rect) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required | const |
| [Hinting](class_textserver.md#enum_TextServer_Hinting) | [_font_get_hinting](class_textserverextension.md#class_TextServerExtension_private_method__font_get_hinting) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_get_keep_rounding_remainders](class_textserverextension.md#class_TextServerExtension_private_method__font_get_keep_rounding_remainders) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Vector2](class_vector2.md#class_Vector2) | [_font_get_kerning](class_textserverextension.md#class_TextServerExtension_private_method__font_get_kerning) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [_font_get_kerning_list](class_textserverextension.md#class_TextServerExtension_private_method__font_get_kerning_list) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_get_language_support_override](class_textserverextension.md#class_TextServerExtension_private_method__font_get_language_support_override) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_font_get_language_support_overrides](class_textserverextension.md#class_TextServerExtension_private_method__font_get_language_support_overrides) ( font_rid: [RID](class_rid.md#class_RID) ) virtual |
| [int](class_int.md#class_int) | [_font_get_msdf_pixel_range](class_textserverextension.md#class_TextServerExtension_private_method__font_get_msdf_pixel_range) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_msdf_size](class_textserverextension.md#class_TextServerExtension_private_method__font_get_msdf_size) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [String](class_string.md#class_String) | [_font_get_name](class_textserverextension.md#class_TextServerExtension_private_method__font_get_name) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_font_get_opentype_feature_overrides](class_textserverextension.md#class_TextServerExtension_private_method__font_get_opentype_feature_overrides) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_font_get_ot_name_strings](class_textserverextension.md#class_TextServerExtension_private_method__font_get_ot_name_strings) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_font_get_oversampling](class_textserverextension.md#class_TextServerExtension_private_method__font_get_oversampling) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_font_get_scale](class_textserverextension.md#class_TextServerExtension_private_method__font_get_scale) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_font_get_script_support_override](class_textserverextension.md#class_TextServerExtension_private_method__font_get_script_support_override) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_font_get_script_support_overrides](class_textserverextension.md#class_TextServerExtension_private_method__font_get_script_support_overrides) ( font_rid: [RID](class_rid.md#class_RID) ) virtual |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_font_get_size_cache_info](class_textserverextension.md#class_TextServerExtension_private_method__font_get_size_cache_info) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [_font_get_size_cache_list](class_textserverextension.md#class_TextServerExtension_private_method__font_get_size_cache_list) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_font_get_spacing](class_textserverextension.md#class_TextServerExtension_private_method__font_get_spacing) ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_stretch](class_textserverextension.md#class_TextServerExtension_private_method__font_get_stretch) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| bitfield | \[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] | [_font_get_style](class_textserverextension.md#class_TextServerExtension_private_method__font_get_style) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [String](class_string.md#class_String) | [_font_get_style_name](class_textserverextension.md#class_TextServerExtension_private_method__font_get_style_name) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) | [_font_get_subpixel_positioning](class_textserverextension.md#class_TextServerExtension_private_method__font_get_subpixel_positioning) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [String](class_string.md#class_String) | [_font_get_supported_chars](class_textserverextension.md#class_TextServerExtension_private_method__font_get_supported_chars) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_font_get_supported_glyphs](class_textserverextension.md#class_TextServerExtension_private_method__font_get_supported_glyphs) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_font_get_texture_count](class_textserverextension.md#class_TextServerExtension_private_method__font_get_texture_count) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | required | const |
| [Image](class_image.md#class_Image) | [_font_get_texture_image](class_textserverextension.md#class_TextServerExtension_private_method__font_get_texture_image) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) | virtual | required | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_font_get_texture_offsets](class_textserverextension.md#class_TextServerExtension_private_method__font_get_texture_offsets) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) | virtual | const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [_font_get_transform](class_textserverextension.md#class_TextServerExtension_private_method__font_get_transform) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_font_get_underline_position](class_textserverextension.md#class_TextServerExtension_private_method__font_get_underline_position) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_font_get_underline_thickness](class_textserverextension.md#class_TextServerExtension_private_method__font_get_underline_thickness) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_font_get_variation_coordinates](class_textserverextension.md#class_TextServerExtension_private_method__font_get_variation_coordinates) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_font_get_weight](class_textserverextension.md#class_TextServerExtension_private_method__font_get_weight) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_has_char](class_textserverextension.md#class_TextServerExtension_private_method__font_has_char) ( font_rid: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_font_is_allow_system_fallback](class_textserverextension.md#class_TextServerExtension_private_method__font_is_allow_system_fallback) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_is_force_autohinter](class_textserverextension.md#class_TextServerExtension_private_method__font_is_force_autohinter) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_is_language_supported](class_textserverextension.md#class_TextServerExtension_private_method__font_is_language_supported) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_is_modulate_color_glyphs](class_textserverextension.md#class_TextServerExtension_private_method__font_is_modulate_color_glyphs) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_is_multichannel_signed_distance_field](class_textserverextension.md#class_TextServerExtension_private_method__font_is_multichannel_signed_distance_field) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_font_is_script_supported](class_textserverextension.md#class_TextServerExtension_private_method__font_is_script_supported) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) | virtual | const |
| void | [_font_remove_glyph](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_glyph) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) | virtual | required |
| void | [_font_remove_kerning](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_kerning) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) virtual |
| void | [_font_remove_language_support_override](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_language_support_override) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) virtual |
| void | [_font_remove_script_support_override](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_script_support_override) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) virtual |
| void | [_font_remove_size_cache](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_size_cache) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | required |
| void | [_font_remove_texture](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_texture) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) | virtual | required |
| void | [_font_render_glyph](class_textserverextension.md#class_TextServerExtension_private_method__font_render_glyph) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), index: [int](class_int.md#class_int) ) virtual |
| void | [_font_render_range](class_textserverextension.md#class_TextServerExtension_private_method__font_render_range) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_allow_system_fallback](class_textserverextension.md#class_TextServerExtension_private_method__font_set_allow_system_fallback) ( font_rid: [RID](class_rid.md#class_RID), allow_system_fallback: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_antialiasing](class_textserverextension.md#class_TextServerExtension_private_method__font_set_antialiasing) ( font_rid: [RID](class_rid.md#class_RID), antialiasing: [FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) ) virtual |
| void | [_font_set_ascent](class_textserverextension.md#class_TextServerExtension_private_method__font_set_ascent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), ascent: [float](class_float.md#class_float) ) | virtual | required |
| void | [_font_set_baseline_offset](class_textserverextension.md#class_TextServerExtension_private_method__font_set_baseline_offset) ( font_rid: [RID](class_rid.md#class_RID), baseline_offset: [float](class_float.md#class_float) ) virtual |
| void | [_font_set_data](class_textserverextension.md#class_TextServerExtension_private_method__font_set_data) ( font_rid: [RID](class_rid.md#class_RID), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) virtual |
| void | [_font_set_data_ptr](class_textserverextension.md#class_TextServerExtension_private_method__font_set_data_ptr) ( font_rid: [RID](class_rid.md#class_RID), data_ptr: `const uint8_t*`, data_size: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_descent](class_textserverextension.md#class_TextServerExtension_private_method__font_set_descent) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), descent: [float](class_float.md#class_float) ) | virtual | required |
| void | [_font_set_disable_embedded_bitmaps](class_textserverextension.md#class_TextServerExtension_private_method__font_set_disable_embedded_bitmaps) ( font_rid: [RID](class_rid.md#class_RID), disable_embedded_bitmaps: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_embolden](class_textserverextension.md#class_TextServerExtension_private_method__font_set_embolden) ( font_rid: [RID](class_rid.md#class_RID), strength: [float](class_float.md#class_float) ) virtual |
| void | [_font_set_face_index](class_textserverextension.md#class_TextServerExtension_private_method__font_set_face_index) ( font_rid: [RID](class_rid.md#class_RID), face_index: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_fixed_size](class_textserverextension.md#class_TextServerExtension_private_method__font_set_fixed_size) ( font_rid: [RID](class_rid.md#class_RID), fixed_size: [int](class_int.md#class_int) ) | virtual | required |
| void | [_font_set_fixed_size_scale_mode](class_textserverextension.md#class_TextServerExtension_private_method__font_set_fixed_size_scale_mode) ( font_rid: [RID](class_rid.md#class_RID), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) ) | virtual | required |
| void | [_font_set_force_autohinter](class_textserverextension.md#class_TextServerExtension_private_method__font_set_force_autohinter) ( font_rid: [RID](class_rid.md#class_RID), force_autohinter: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_generate_mipmaps](class_textserverextension.md#class_TextServerExtension_private_method__font_set_generate_mipmaps) ( font_rid: [RID](class_rid.md#class_RID), generate_mipmaps: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_global_oversampling](class_textserverextension.md#class_TextServerExtension_private_method__font_set_global_oversampling) ( oversampling: [float](class_float.md#class_float) ) virtual |
| void | [_font_set_glyph_advance](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_advance) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int), advance: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_font_set_glyph_offset](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_offset) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), offset: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_font_set_glyph_size](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_size) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), gl_size: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_font_set_glyph_texture_idx](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_texture_idx) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), texture_idx: [int](class_int.md#class_int) ) | virtual | required |
| void | [_font_set_glyph_uv_rect](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_uv_rect) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), uv_rect: [Rect2](class_rect2.md#class_Rect2) ) | virtual | required |
| void | [_font_set_hinting](class_textserverextension.md#class_TextServerExtension_private_method__font_set_hinting) ( font_rid: [RID](class_rid.md#class_RID), hinting: [Hinting](class_textserver.md#enum_TextServer_Hinting) ) virtual |
| void | [_font_set_keep_rounding_remainders](class_textserverextension.md#class_TextServerExtension_private_method__font_set_keep_rounding_remainders) ( font_rid: [RID](class_rid.md#class_RID), keep_rounding_remainders: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_kerning](class_textserverextension.md#class_TextServerExtension_private_method__font_set_kerning) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i), kerning: [Vector2](class_vector2.md#class_Vector2) ) virtual |
| void | [_font_set_language_support_override](class_textserverextension.md#class_TextServerExtension_private_method__font_set_language_support_override) ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_modulate_color_glyphs](class_textserverextension.md#class_TextServerExtension_private_method__font_set_modulate_color_glyphs) ( font_rid: [RID](class_rid.md#class_RID), modulate: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_msdf_pixel_range](class_textserverextension.md#class_TextServerExtension_private_method__font_set_msdf_pixel_range) ( font_rid: [RID](class_rid.md#class_RID), msdf_pixel_range: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_msdf_size](class_textserverextension.md#class_TextServerExtension_private_method__font_set_msdf_size) ( font_rid: [RID](class_rid.md#class_RID), msdf_size: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_multichannel_signed_distance_field](class_textserverextension.md#class_TextServerExtension_private_method__font_set_multichannel_signed_distance_field) ( font_rid: [RID](class_rid.md#class_RID), msdf: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_name](class_textserverextension.md#class_TextServerExtension_private_method__font_set_name) ( font_rid: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) virtual |
| void | [_font_set_opentype_feature_overrides](class_textserverextension.md#class_TextServerExtension_private_method__font_set_opentype_feature_overrides) ( font_rid: [RID](class_rid.md#class_RID), overrides: [Dictionary](class_dictionary.md#class_Dictionary) ) virtual |
| void | [_font_set_oversampling](class_textserverextension.md#class_TextServerExtension_private_method__font_set_oversampling) ( font_rid: [RID](class_rid.md#class_RID), oversampling: [float](class_float.md#class_float) ) virtual |
| void | [_font_set_scale](class_textserverextension.md#class_TextServerExtension_private_method__font_set_scale) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), scale: [float](class_float.md#class_float) ) | virtual | required |
| void | [_font_set_script_support_override](class_textserverextension.md#class_TextServerExtension_private_method__font_set_script_support_override) ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) virtual |
| void | [_font_set_spacing](class_textserverextension.md#class_TextServerExtension_private_method__font_set_spacing) ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_stretch](class_textserverextension.md#class_TextServerExtension_private_method__font_set_stretch) ( font_rid: [RID](class_rid.md#class_RID), stretch: [int](class_int.md#class_int) ) virtual |
| void | [_font_set_style](class_textserverextension.md#class_TextServerExtension_private_method__font_set_style) ( font_rid: [RID](class_rid.md#class_RID), style: | bitfield | \[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] ) | virtual |
| void | [_font_set_style_name](class_textserverextension.md#class_TextServerExtension_private_method__font_set_style_name) ( font_rid: [RID](class_rid.md#class_RID), name_style: [String](class_string.md#class_String) ) virtual |
| void | [_font_set_subpixel_positioning](class_textserverextension.md#class_TextServerExtension_private_method__font_set_subpixel_positioning) ( font_rid: [RID](class_rid.md#class_RID), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) ) virtual |
| void | [_font_set_texture_image](class_textserverextension.md#class_TextServerExtension_private_method__font_set_texture_image) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), image: [Image](class_image.md#class_Image) ) | virtual | required |
| void | [_font_set_texture_offsets](class_textserverextension.md#class_TextServerExtension_private_method__font_set_texture_offsets) ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), offset: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) virtual |
| void | [_font_set_transform](class_textserverextension.md#class_TextServerExtension_private_method__font_set_transform) ( font_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) virtual |
| void | [_font_set_underline_position](class_textserverextension.md#class_TextServerExtension_private_method__font_set_underline_position) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_position: [float](class_float.md#class_float) ) | virtual | required |
| void | [_font_set_underline_thickness](class_textserverextension.md#class_TextServerExtension_private_method__font_set_underline_thickness) ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_thickness: [float](class_float.md#class_float) ) | virtual | required |
| void | [_font_set_variation_coordinates](class_textserverextension.md#class_TextServerExtension_private_method__font_set_variation_coordinates) ( font_rid: [RID](class_rid.md#class_RID), variation_coordinates: [Dictionary](class_dictionary.md#class_Dictionary) ) virtual |
| void | [_font_set_weight](class_textserverextension.md#class_TextServerExtension_private_method__font_set_weight) ( font_rid: [RID](class_rid.md#class_RID), weight: [int](class_int.md#class_int) ) virtual |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_font_supported_feature_list](class_textserverextension.md#class_TextServerExtension_private_method__font_supported_feature_list) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_font_supported_variation_list](class_textserverextension.md#class_TextServerExtension_private_method__font_supported_variation_list) ( font_rid: [RID](class_rid.md#class_RID) ) | virtual | const |
| [String](class_string.md#class_String) | [_format_number](class_textserverextension.md#class_TextServerExtension_private_method__format_number) ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) | virtual | const |
| void | [_free_rid](class_textserverextension.md#class_TextServerExtension_private_method__free_rid) ( rid: [RID](class_rid.md#class_RID) ) | virtual | required |
| [int](class_int.md#class_int) | [_get_features](class_textserverextension.md#class_TextServerExtension_private_method__get_features) ( ) | virtual | required | const |
| [Vector2](class_vector2.md#class_Vector2) | [_get_hex_code_box_size](class_textserverextension.md#class_TextServerExtension_private_method__get_hex_code_box_size) ( size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_name](class_textserverextension.md#class_TextServerExtension_private_method__get_name) ( ) | virtual | required | const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [_get_support_data](class_textserverextension.md#class_TextServerExtension_private_method__get_support_data) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_support_data_filename](class_textserverextension.md#class_TextServerExtension_private_method__get_support_data_filename) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_support_data_info](class_textserverextension.md#class_TextServerExtension_private_method__get_support_data_info) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_has](class_textserverextension.md#class_TextServerExtension_private_method__has) ( rid: [RID](class_rid.md#class_RID) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_has_feature](class_textserverextension.md#class_TextServerExtension_private_method__has_feature) ( feature: [Feature](class_textserver.md#enum_TextServer_Feature) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_is_confusable](class_textserverextension.md#class_TextServerExtension_private_method__is_confusable) ( string: [String](class_string.md#class_String), dict: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_locale_right_to_left](class_textserverextension.md#class_TextServerExtension_private_method__is_locale_right_to_left) ( locale: [String](class_string.md#class_String) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_locale_using_support_data](class_textserverextension.md#class_TextServerExtension_private_method__is_locale_using_support_data) ( locale: [String](class_string.md#class_String) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_valid_identifier](class_textserverextension.md#class_TextServerExtension_private_method__is_valid_identifier) ( string: [String](class_string.md#class_String) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_valid_letter](class_textserverextension.md#class_TextServerExtension_private_method__is_valid_letter) ( unicode: [int](class_int.md#class_int) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_load_support_data](class_textserverextension.md#class_TextServerExtension_private_method__load_support_data) ( filename: [String](class_string.md#class_String) ) virtual |
| [int](class_int.md#class_int) | [_name_to_tag](class_textserverextension.md#class_TextServerExtension_private_method__name_to_tag) ( name: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_parse_number](class_textserverextension.md#class_TextServerExtension_private_method__parse_number) ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Vector3i](class_vector3i.md#class_Vector3i)\] | [_parse_structured_text](class_textserverextension.md#class_TextServerExtension_private_method__parse_structured_text) ( parser_type: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser), args: [Array](class_array.md#class_Array), text: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_percent_sign](class_textserverextension.md#class_TextServerExtension_private_method__percent_sign) ( language: [String](class_string.md#class_String) ) | virtual | const |
| void | [_reference_oversampling_level](class_textserverextension.md#class_TextServerExtension_private_method__reference_oversampling_level) ( oversampling: [float](class_float.md#class_float) ) virtual |
| [bool](class_bool.md#class_bool) | [_save_support_data](class_textserverextension.md#class_TextServerExtension_private_method__save_support_data) ( filename: [String](class_string.md#class_String) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_get_run_count](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_count) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [_shaped_get_run_direction](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_direction) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [RID](class_rid.md#class_RID) | [_shaped_get_run_font_rid](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_font_rid) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_get_run_font_size](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_font_size) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_shaped_get_run_language](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_language) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [Variant](class_variant.md#class_Variant) | [_shaped_get_run_object](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_object) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [_shaped_get_run_range](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_range) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_shaped_get_run_text](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_text) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_get_span_count](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_count) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_shaped_get_span_embedded_object](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_embedded_object) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_shaped_get_span_meta](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_meta) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_shaped_get_span_object](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_object) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_shaped_get_span_text](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_text) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_shaped_get_text](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_text) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_shaped_set_span_update_font](class_textserverextension.md#class_TextServerExtension_private_method__shaped_set_span_update_font) ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_shaped_text_add_object](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_add_object) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment, length: [int](class_int.md#class_int), baseline: [float](class_float.md#class_float) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_shaped_text_add_string](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_add_string) ( shaped: [RID](class_rid.md#class_RID), text: [String](class_string.md#class_String), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary), language: [String](class_string.md#class_String), meta: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_shaped_text_clear](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_clear) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required |
| [int](class_int.md#class_int) | [_shaped_text_closest_character_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_closest_character_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) | virtual | const |
| void | [_shaped_text_draw](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_draw) ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float), clip_r: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) | virtual | const |
| void | [_shaped_text_draw_outline](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_draw_outline) ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float), clip_r: [float](class_float.md#class_float), outline_size: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) | virtual | const |
| [RID](class_rid.md#class_RID) | [_shaped_text_duplicate](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_duplicate) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required |
| [float](class_float.md#class_float) | [_shaped_text_fit_to_width](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_fit_to_width) ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), justification_flags: | bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] ) | virtual |
| [float](class_float.md#class_float) | [_shaped_text_get_ascent](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ascent) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_shaped_text_get_carets](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_carets) ( shaped: [RID](class_rid.md#class_RID), position: [int](class_int.md#class_int), caret: `CaretInfo*` ) | virtual | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_shaped_text_get_character_breaks](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_character_breaks) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_get_custom_ellipsis](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_custom_ellipsis) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [String](class_string.md#class_String) | [_shaped_text_get_custom_punctuation](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_custom_punctuation) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [float](class_float.md#class_float) | [_shaped_text_get_descent](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_descent) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [_shaped_text_get_direction](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_direction) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_get_dominant_direction_in_range](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_dominant_direction_in_range) ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_get_ellipsis_glyph_count](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyph_count) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| `const Glyph*` | [_shaped_text_get_ellipsis_glyphs](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyphs) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_shaped_text_get_ellipsis_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ellipsis_pos) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_shaped_text_get_glyph_count](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_glyph_count) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| `const Glyph*` | [_shaped_text_get_glyphs](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_glyphs) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Vector2](class_vector2.md#class_Vector2) | [_shaped_text_get_grapheme_bounds](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_grapheme_bounds) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) | virtual | const |
| [Direction](class_textserver.md#enum_TextServer_Direction) | [_shaped_text_get_inferred_direction](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_inferred_direction) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_shaped_text_get_line_breaks](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_line_breaks) ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), start: [int](class_int.md#class_int), break_flags: | bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] ) | virtual | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_shaped_text_get_line_breaks_adv](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_line_breaks_adv) ( shaped: [RID](class_rid.md#class_RID), width: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), start: [int](class_int.md#class_int), once: [bool](class_bool.md#class_bool), break_flags: | bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_get_object_glyph](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_object_glyph) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) | virtual | required | const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [_shaped_text_get_object_range](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_object_range) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) | virtual | required | const |
| [Rect2](class_rect2.md#class_Rect2) | [_shaped_text_get_object_rect](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_object_rect) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) | virtual | required | const |
| [Array](class_array.md#class_Array) | [_shaped_text_get_objects](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_objects) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Orientation](class_textserver.md#enum_TextServer_Orientation) | [_shaped_text_get_orientation](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_orientation) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [RID](class_rid.md#class_RID) | [_shaped_text_get_parent](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_parent) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_shaped_text_get_preserve_control](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_preserve_control) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_shaped_text_get_preserve_invalid](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_preserve_invalid) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [_shaped_text_get_range](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_range) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [_shaped_text_get_selection](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_selection) ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) | virtual | const |
| [Vector2](class_vector2.md#class_Vector2) | [_shaped_text_get_size](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_size) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_shaped_text_get_spacing](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_spacing) ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_get_trim_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_trim_pos) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_shaped_text_get_underline_position](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_underline_position) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_shaped_text_get_underline_thickness](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_underline_thickness) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_shaped_text_get_width](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_width) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_shaped_text_get_word_breaks](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_word_breaks) ( shaped: [RID](class_rid.md#class_RID), grapheme_flags: | bitfield | \[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\], skip_grapheme_flags: | bitfield | \[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\] ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_shaped_text_has_object](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_has_object) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_shaped_text_hit_test_grapheme](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_hit_test_grapheme) ( shaped: [RID](class_rid.md#class_RID), coord: [float](class_float.md#class_float) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_hit_test_position](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_hit_test_position) ( shaped: [RID](class_rid.md#class_RID), coord: [float](class_float.md#class_float) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_shaped_text_is_ready](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_is_ready) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_shaped_text_next_character_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_next_character_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_next_grapheme_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_next_grapheme_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) | virtual | const |
| void | [_shaped_text_overrun_trim_to_width](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_overrun_trim_to_width) ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), trim_flags: | bitfield | \[[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag)\] ) | virtual |
| [int](class_int.md#class_int) | [_shaped_text_prev_character_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_prev_character_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_shaped_text_prev_grapheme_pos](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_prev_grapheme_pos) ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_shaped_text_resize_object](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_resize_object) ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment, baseline: [float](class_float.md#class_float) ) | virtual | required |
| void | [_shaped_text_set_bidi_override](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_bidi_override) ( shaped: [RID](class_rid.md#class_RID), override: [Array](class_array.md#class_Array) ) virtual |
| void | [_shaped_text_set_custom_ellipsis](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_custom_ellipsis) ( shaped: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) virtual |
| void | [_shaped_text_set_custom_punctuation](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_custom_punctuation) ( shaped: [RID](class_rid.md#class_RID), punct: [String](class_string.md#class_String) ) virtual |
| void | [_shaped_text_set_direction](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_direction) ( shaped: [RID](class_rid.md#class_RID), direction: [Direction](class_textserver.md#enum_TextServer_Direction) ) virtual |
| void | [_shaped_text_set_orientation](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_orientation) ( shaped: [RID](class_rid.md#class_RID), orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) ) virtual |
| void | [_shaped_text_set_preserve_control](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_preserve_control) ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) virtual |
| void | [_shaped_text_set_preserve_invalid](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_preserve_invalid) ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) virtual |
| void | [_shaped_text_set_spacing](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_spacing) ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) virtual |
| [bool](class_bool.md#class_bool) | [_shaped_text_shape](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_shape) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required |
| `const Glyph*` | [_shaped_text_sort_logical](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_sort_logical) ( shaped: [RID](class_rid.md#class_RID) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_shaped_text_substr](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_substr) ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), length: [int](class_int.md#class_int) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_shaped_text_tab_align](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_tab_align) ( shaped: [RID](class_rid.md#class_RID), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) virtual |
| [bool](class_bool.md#class_bool) | [_shaped_text_update_breaks](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_update_breaks) ( shaped: [RID](class_rid.md#class_RID) ) virtual |
| [bool](class_bool.md#class_bool) | [_shaped_text_update_justification_ops](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_update_justification_ops) ( shaped: [RID](class_rid.md#class_RID) ) virtual |
| [bool](class_bool.md#class_bool) | [_spoof_check](class_textserverextension.md#class_TextServerExtension_private_method__spoof_check) ( string: [String](class_string.md#class_String) ) | virtual | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_string_get_character_breaks](class_textserverextension.md#class_TextServerExtension_private_method__string_get_character_breaks) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) | virtual | const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_string_get_word_breaks](class_textserverextension.md#class_TextServerExtension_private_method__string_get_word_breaks) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String), chars_per_line: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_string_to_lower](class_textserverextension.md#class_TextServerExtension_private_method__string_to_lower) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_string_to_title](class_textserverextension.md#class_TextServerExtension_private_method__string_to_title) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_string_to_upper](class_textserverextension.md#class_TextServerExtension_private_method__string_to_upper) ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_strip_diacritics](class_textserverextension.md#class_TextServerExtension_private_method__strip_diacritics) ( string: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_tag_to_name](class_textserverextension.md#class_TextServerExtension_private_method__tag_to_name) ( tag: [int](class_int.md#class_int) ) | virtual | const |
| void | [_unreference_oversampling_level](class_textserverextension.md#class_TextServerExtension_private_method__unreference_oversampling_level) ( oversampling: [float](class_float.md#class_float) ) virtual |

---

### Method Descriptions

<span id="class_TextServerExtension_private_method__cleanup"></span>

void **_cleanup** ( ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__cleanup)

This method is called before text server is unregistered.

---

<span id="class_TextServerExtension_private_method__create_font"></span>

[RID](class_rid.md#class_RID) **_create_font** ( ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__create_font)

Creates a new, empty font cache entry resource.

---

<span id="class_TextServerExtension_private_method__create_font_linked_variation"></span>

[RID](class_rid.md#class_RID) **_create_font_linked_variation** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__create_font_linked_variation)

Optional, implement if font supports extra spacing or baseline offset.

Creates a new variation existing font which is reusing the same glyph cache and font data.

---

<span id="class_TextServerExtension_private_method__create_shaped_text"></span>

[RID](class_rid.md#class_RID) **_create_shaped_text** ( direction: [Direction](class_textserver.md#enum_TextServer_Direction), orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__create_shaped_text)

Creates a new buffer for complex text layout, with the given `direction` and `orientation`.

---

<span id="class_TextServerExtension_private_method__draw_hex_code_box"></span>

void **_draw_hex_code_box** ( canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__draw_hex_code_box)

Draws box displaying character hexadecimal code.

---

<span id="class_TextServerExtension_private_method__font_clear_glyphs"></span>

void **_font_clear_glyphs** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_glyphs)

Removes all rendered glyph information from the cache entry.

---

<span id="class_TextServerExtension_private_method__font_clear_kerning_map"></span>

void **_font_clear_kerning_map** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_kerning_map)

Removes all kerning overrides.

---

<span id="class_TextServerExtension_private_method__font_clear_size_cache"></span>

void **_font_clear_size_cache** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_size_cache)

Removes all font sizes from the cache entry.

---

<span id="class_TextServerExtension_private_method__font_clear_system_fallback_cache"></span>

void **_font_clear_system_fallback_cache** ( ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_system_fallback_cache)

Frees all automatically loaded system fonts.

---

<span id="class_TextServerExtension_private_method__font_clear_textures"></span>

void **_font_clear_textures** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_clear_textures)

Removes all textures from font cache entry.

---

<span id="class_TextServerExtension_private_method__font_draw_glyph"></span>

void **_font_draw_glyph** ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_draw_glyph)

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextServerExtension_private_method__font_draw_glyph_outline"></span>

void **_font_draw_glyph_outline** ( font_rid: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), outline_size: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_draw_glyph_outline)

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextServerExtension_private_method__font_get_antialiasing"></span>

[FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) **_font_get_antialiasing** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_antialiasing)

Returns font anti-aliasing mode.

---

<span id="class_TextServerExtension_private_method__font_get_ascent"></span>

[float](class_float.md#class_float) **_font_get_ascent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_ascent)

Returns the font ascent (number of pixels above the baseline).

---

<span id="class_TextServerExtension_private_method__font_get_baseline_offset"></span>

[float](class_float.md#class_float) **_font_get_baseline_offset** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_baseline_offset)

Returns extra baseline offset (as a fraction of font height).

---

<span id="class_TextServerExtension_private_method__font_get_char_from_glyph_index"></span>

[int](class_int.md#class_int) **_font_get_char_from_glyph_index** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_char_from_glyph_index)

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid.

---

<span id="class_TextServerExtension_private_method__font_get_descent"></span>

[float](class_float.md#class_float) **_font_get_descent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_descent)

Returns the font descent (number of pixels below the baseline).

---

<span id="class_TextServerExtension_private_method__font_get_disable_embedded_bitmaps"></span>

[bool](class_bool.md#class_bool) **_font_get_disable_embedded_bitmaps** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_disable_embedded_bitmaps)

Returns whether the font's embedded bitmap loading is disabled.

---

<span id="class_TextServerExtension_private_method__font_get_embolden"></span>

[float](class_float.md#class_float) **_font_get_embolden** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_embolden)

Returns font embolden strength.

---

<span id="class_TextServerExtension_private_method__font_get_face_count"></span>

[int](class_int.md#class_int) **_font_get_face_count** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_face_count)

Returns number of faces in the TrueType / OpenType collection.

---

<span id="class_TextServerExtension_private_method__font_get_face_index"></span>

[int](class_int.md#class_int) **_font_get_face_index** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_face_index)

Returns an active face index in the TrueType / OpenType collection.

---

<span id="class_TextServerExtension_private_method__font_get_fixed_size"></span>

[int](class_int.md#class_int) **_font_get_fixed_size** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_fixed_size)

Returns bitmap font fixed size.

---

<span id="class_TextServerExtension_private_method__font_get_fixed_size_scale_mode"></span>

[FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) **_font_get_fixed_size_scale_mode** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_fixed_size_scale_mode)

Returns bitmap font scaling mode.

---

<span id="class_TextServerExtension_private_method__font_get_generate_mipmaps"></span>

[bool](class_bool.md#class_bool) **_font_get_generate_mipmaps** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_generate_mipmaps)

Returns `true` if font texture mipmap generation is enabled.

---

<span id="class_TextServerExtension_private_method__font_get_global_oversampling"></span>

[float](class_float.md#class_float) **_font_get_global_oversampling** ( ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_global_oversampling)

Returns the font oversampling factor, shared by all fonts in the TextServer.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_advance"></span>

[Vector2](class_vector2.md#class_Vector2) **_font_get_glyph_advance** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_advance)

Returns glyph advance (offset of the next glyph).

---

<span id="class_TextServerExtension_private_method__font_get_glyph_contours"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_font_get_glyph_contours** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_contours)

Returns outline contours of the glyph.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_index"></span>

[int](class_int.md#class_int) **_font_get_glyph_index** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), char: [int](class_int.md#class_int), variation_selector: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_index)

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_list"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_font_get_glyph_list** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_list)

Returns list of rendered glyphs in the cache entry.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **_font_get_glyph_offset** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_offset)

Returns glyph offset from the baseline.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_font_get_glyph_size** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_size)

Returns size of the glyph.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_texture_idx"></span>

[int](class_int.md#class_int) **_font_get_glyph_texture_idx** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_texture_idx)

Returns index of the cache texture containing the glyph.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_texture_rid"></span>

[RID](class_rid.md#class_RID) **_font_get_glyph_texture_rid** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_texture_rid)

Returns resource ID of the cache texture containing the glyph.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_texture_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_font_get_glyph_texture_size** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_texture_size)

Returns size of the cache texture containing the glyph.

---

<span id="class_TextServerExtension_private_method__font_get_glyph_uv_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **_font_get_glyph_uv_rect** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_glyph_uv_rect)

Returns rectangle in the cache texture containing the glyph.

---

<span id="class_TextServerExtension_private_method__font_get_hinting"></span>

[Hinting](class_textserver.md#enum_TextServer_Hinting) **_font_get_hinting** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_hinting)

Returns the font hinting mode. Used by dynamic fonts only.

---

<span id="class_TextServerExtension_private_method__font_get_keep_rounding_remainders"></span>

[bool](class_bool.md#class_bool) **_font_get_keep_rounding_remainders** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_keep_rounding_remainders)

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

<span id="class_TextServerExtension_private_method__font_get_kerning"></span>

[Vector2](class_vector2.md#class_Vector2) **_font_get_kerning** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_kerning)

Returns kerning for the pair of glyphs.

---

<span id="class_TextServerExtension_private_method__font_get_kerning_list"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **_font_get_kerning_list** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_kerning_list)

Returns list of the kerning overrides.

---

<span id="class_TextServerExtension_private_method__font_get_language_support_override"></span>

[bool](class_bool.md#class_bool) **_font_get_language_support_override** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_language_support_override)

Returns `true` if support override is enabled for the `language`.

---

<span id="class_TextServerExtension_private_method__font_get_language_support_overrides"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_font_get_language_support_overrides** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_language_support_overrides)

Returns list of language support overrides.

---

<span id="class_TextServerExtension_private_method__font_get_msdf_pixel_range"></span>

[int](class_int.md#class_int) **_font_get_msdf_pixel_range** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_msdf_pixel_range)

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

---

<span id="class_TextServerExtension_private_method__font_get_msdf_size"></span>

[int](class_int.md#class_int) **_font_get_msdf_size** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_msdf_size)

Returns source font size used to generate MSDF textures.

---

<span id="class_TextServerExtension_private_method__font_get_name"></span>

[String](class_string.md#class_String) **_font_get_name** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_name)

Returns font family name.

---

<span id="class_TextServerExtension_private_method__font_get_opentype_feature_overrides"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_font_get_opentype_feature_overrides** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_opentype_feature_overrides)

Returns font OpenType feature set override.

---

<span id="class_TextServerExtension_private_method__font_get_ot_name_strings"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_font_get_ot_name_strings** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_ot_name_strings)

Returns [Dictionary](class_dictionary.md#class_Dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---

<span id="class_TextServerExtension_private_method__font_get_oversampling"></span>

[float](class_float.md#class_float) **_font_get_oversampling** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_oversampling)

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class_Viewport_property_oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

<span id="class_TextServerExtension_private_method__font_get_scale"></span>

[float](class_float.md#class_float) **_font_get_scale** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_scale)

Returns scaling factor of the color bitmap font.

---

<span id="class_TextServerExtension_private_method__font_get_script_support_override"></span>

[bool](class_bool.md#class_bool) **_font_get_script_support_override** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_script_support_override)

Returns `true` if support override is enabled for the `script`.

---

<span id="class_TextServerExtension_private_method__font_get_script_support_overrides"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_font_get_script_support_overrides** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_script_support_overrides)

Returns list of script support overrides.

---

<span id="class_TextServerExtension_private_method__font_get_size_cache_info"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_font_get_size_cache_info** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_size_cache_info)

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

---

<span id="class_TextServerExtension_private_method__font_get_size_cache_list"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **_font_get_size_cache_list** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_size_cache_list)

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class_Vector2i) with font size and outline size.

---

<span id="class_TextServerExtension_private_method__font_get_spacing"></span>

[int](class_int.md#class_int) **_font_get_spacing** ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_spacing)

Returns the spacing for `spacing` in pixels (not relative to the font size).

---

<span id="class_TextServerExtension_private_method__font_get_stretch"></span>

[int](class_int.md#class_int) **_font_get_stretch** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_stretch)

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

<span id="class_TextServerExtension_private_method__font_get_style"></span>

*BitField*\[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] **_font_get_style** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_style)

Returns font style flags.

---

<span id="class_TextServerExtension_private_method__font_get_style_name"></span>

[String](class_string.md#class_String) **_font_get_style_name** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_style_name)

Returns font style name.

---

<span id="class_TextServerExtension_private_method__font_get_subpixel_positioning"></span>

[SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) **_font_get_subpixel_positioning** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_subpixel_positioning)

Returns font subpixel glyph positioning mode.

---

<span id="class_TextServerExtension_private_method__font_get_supported_chars"></span>

[String](class_string.md#class_String) **_font_get_supported_chars** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_supported_chars)

Returns a string containing all the characters available in the font.

---

<span id="class_TextServerExtension_private_method__font_get_supported_glyphs"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_font_get_supported_glyphs** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_supported_glyphs)

Returns an array containing all glyph indices in the font.

---

<span id="class_TextServerExtension_private_method__font_get_texture_count"></span>

[int](class_int.md#class_int) **_font_get_texture_count** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_texture_count)

Returns number of textures used by font cache entry.

---

<span id="class_TextServerExtension_private_method__font_get_texture_image"></span>

[Image](class_image.md#class_Image) **_font_get_texture_image** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_texture_image)

Returns font cache texture image data.

---

<span id="class_TextServerExtension_private_method__font_get_texture_offsets"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_font_get_texture_offsets** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_texture_offsets)

Returns array containing glyph packing data.

---

<span id="class_TextServerExtension_private_method__font_get_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **_font_get_transform** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_transform)

Returns 2D transform applied to the font outlines.

---

<span id="class_TextServerExtension_private_method__font_get_underline_position"></span>

[float](class_float.md#class_float) **_font_get_underline_position** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_underline_position)

Returns pixel offset of the underline below the baseline.

---

<span id="class_TextServerExtension_private_method__font_get_underline_thickness"></span>

[float](class_float.md#class_float) **_font_get_underline_thickness** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_underline_thickness)

Returns thickness of the underline in pixels.

---

<span id="class_TextServerExtension_private_method__font_get_variation_coordinates"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_font_get_variation_coordinates** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_variation_coordinates)

Returns variation coordinates for the specified font cache entry.

---

<span id="class_TextServerExtension_private_method__font_get_weight"></span>

[int](class_int.md#class_int) **_font_get_weight** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_get_weight)

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

<span id="class_TextServerExtension_private_method__font_has_char"></span>

[bool](class_bool.md#class_bool) **_font_has_char** ( font_rid: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_has_char)

Returns `true` if a Unicode `char` is available in the font.

---

<span id="class_TextServerExtension_private_method__font_is_allow_system_fallback"></span>

[bool](class_bool.md#class_bool) **_font_is_allow_system_fallback** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_is_allow_system_fallback)

Returns `true` if system fonts can be automatically used as fallbacks.

---

<span id="class_TextServerExtension_private_method__font_is_force_autohinter"></span>

[bool](class_bool.md#class_bool) **_font_is_force_autohinter** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_is_force_autohinter)

Returns `true` if auto-hinting is supported and preferred over font built-in hinting.

---

<span id="class_TextServerExtension_private_method__font_is_language_supported"></span>

[bool](class_bool.md#class_bool) **_font_is_language_supported** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_is_language_supported)

Returns `true` if the font supports the given language (as a ISO 639 code).

---

<span id="class_TextServerExtension_private_method__font_is_modulate_color_glyphs"></span>

[bool](class_bool.md#class_bool) **_font_is_modulate_color_glyphs** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_is_modulate_color_glyphs)

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

---

<span id="class_TextServerExtension_private_method__font_is_multichannel_signed_distance_field"></span>

[bool](class_bool.md#class_bool) **_font_is_multichannel_signed_distance_field** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_is_multichannel_signed_distance_field)

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---

<span id="class_TextServerExtension_private_method__font_is_script_supported"></span>

[bool](class_bool.md#class_bool) **_font_is_script_supported** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_is_script_supported)

Returns `true` if the font supports the given script (as a ISO 15924 code).

---

<span id="class_TextServerExtension_private_method__font_remove_glyph"></span>

void **_font_remove_glyph** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_glyph)

Removes specified rendered glyph information from the cache entry.

---

<span id="class_TextServerExtension_private_method__font_remove_kerning"></span>

void **_font_remove_kerning** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_kerning)

Removes kerning override for the pair of glyphs.

---

<span id="class_TextServerExtension_private_method__font_remove_language_support_override"></span>

void **_font_remove_language_support_override** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_language_support_override)

Remove language support override.

---

<span id="class_TextServerExtension_private_method__font_remove_script_support_override"></span>

void **_font_remove_script_support_override** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_script_support_override)

Removes script support override.

---

<span id="class_TextServerExtension_private_method__font_remove_size_cache"></span>

void **_font_remove_size_cache** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_size_cache)

Removes specified font size from the cache entry.

---

<span id="class_TextServerExtension_private_method__font_remove_texture"></span>

void **_font_remove_texture** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_remove_texture)

Removes specified texture from the cache entry.

---

<span id="class_TextServerExtension_private_method__font_render_glyph"></span>

void **_font_render_glyph** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_render_glyph)

Renders specified glyph to the font cache texture.

---

<span id="class_TextServerExtension_private_method__font_render_range"></span>

void **_font_render_range** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_render_range)

Renders the range of characters to the font cache texture.

---

<span id="class_TextServerExtension_private_method__font_set_allow_system_fallback"></span>

void **_font_set_allow_system_fallback** ( font_rid: [RID](class_rid.md#class_RID), allow_system_fallback: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_allow_system_fallback)

If set to `true`, system fonts can be automatically used as fallbacks.

---

<span id="class_TextServerExtension_private_method__font_set_antialiasing"></span>

void **_font_set_antialiasing** ( font_rid: [RID](class_rid.md#class_RID), antialiasing: [FontAntialiasing](class_textserver.md#enum_TextServer_FontAntialiasing) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_antialiasing)

Sets font anti-aliasing mode.

---

<span id="class_TextServerExtension_private_method__font_set_ascent"></span>

void **_font_set_ascent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), ascent: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_ascent)

Sets the font ascent (number of pixels above the baseline).

---

<span id="class_TextServerExtension_private_method__font_set_baseline_offset"></span>

void **_font_set_baseline_offset** ( font_rid: [RID](class_rid.md#class_RID), baseline_offset: [float](class_float.md#class_float) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_baseline_offset)

Sets extra baseline offset (as a fraction of font height).

---

<span id="class_TextServerExtension_private_method__font_set_data"></span>

void **_font_set_data** ( font_rid: [RID](class_rid.md#class_RID), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_data)

Sets font source data, e.g contents of the dynamic font source file.

---

<span id="class_TextServerExtension_private_method__font_set_data_ptr"></span>

void **_font_set_data_ptr** ( font_rid: [RID](class_rid.md#class_RID), data_ptr: `const uint8_t*`, data_size: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_data_ptr)

Sets pointer to the font source data, e.g contents of the dynamic font source file.

---

<span id="class_TextServerExtension_private_method__font_set_descent"></span>

void **_font_set_descent** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), descent: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_descent)

Sets the font descent (number of pixels below the baseline).

---

<span id="class_TextServerExtension_private_method__font_set_disable_embedded_bitmaps"></span>

void **_font_set_disable_embedded_bitmaps** ( font_rid: [RID](class_rid.md#class_RID), disable_embedded_bitmaps: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_disable_embedded_bitmaps)

If set to `true`, embedded font bitmap loading is disabled.

---

<span id="class_TextServerExtension_private_method__font_set_embolden"></span>

void **_font_set_embolden** ( font_rid: [RID](class_rid.md#class_RID), strength: [float](class_float.md#class_float) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_embolden)

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---

<span id="class_TextServerExtension_private_method__font_set_face_index"></span>

void **_font_set_face_index** ( font_rid: [RID](class_rid.md#class_RID), face_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_face_index)

Sets an active face index in the TrueType / OpenType collection.

---

<span id="class_TextServerExtension_private_method__font_set_fixed_size"></span>

void **_font_set_fixed_size** ( font_rid: [RID](class_rid.md#class_RID), fixed_size: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_fixed_size)

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

---

<span id="class_TextServerExtension_private_method__font_set_fixed_size_scale_mode"></span>

void **_font_set_fixed_size_scale_mode** ( font_rid: [RID](class_rid.md#class_RID), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum_TextServer_FixedSizeScaleMode) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_fixed_size_scale_mode)

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

---

<span id="class_TextServerExtension_private_method__font_set_force_autohinter"></span>

void **_font_set_force_autohinter** ( font_rid: [RID](class_rid.md#class_RID), force_autohinter: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_force_autohinter)

If set to `true` auto-hinting is preferred over font built-in hinting.

---

<span id="class_TextServerExtension_private_method__font_set_generate_mipmaps"></span>

void **_font_set_generate_mipmaps** ( font_rid: [RID](class_rid.md#class_RID), generate_mipmaps: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_generate_mipmaps)

If set to `true` font texture mipmap generation is enabled.

---

<span id="class_TextServerExtension_private_method__font_set_global_oversampling"></span>

void **_font_set_global_oversampling** ( oversampling: [float](class_float.md#class_float) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_global_oversampling)

Sets oversampling factor, shared by all font in the TextServer.

---

<span id="class_TextServerExtension_private_method__font_set_glyph_advance"></span>

void **_font_set_glyph_advance** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph: [int](class_int.md#class_int), advance: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_advance)

Sets glyph advance (offset of the next glyph).

---

<span id="class_TextServerExtension_private_method__font_set_glyph_offset"></span>

void **_font_set_glyph_offset** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), offset: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_offset)

Sets glyph offset from the baseline.

---

<span id="class_TextServerExtension_private_method__font_set_glyph_size"></span>

void **_font_set_glyph_size** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), gl_size: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_size)

Sets size of the glyph.

---

<span id="class_TextServerExtension_private_method__font_set_glyph_texture_idx"></span>

void **_font_set_glyph_texture_idx** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), texture_idx: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_texture_idx)

Sets index of the cache texture containing the glyph.

---

<span id="class_TextServerExtension_private_method__font_set_glyph_uv_rect"></span>

void **_font_set_glyph_uv_rect** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), glyph: [int](class_int.md#class_int), uv_rect: [Rect2](class_rect2.md#class_Rect2) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_glyph_uv_rect)

Sets rectangle in the cache texture containing the glyph.

---

<span id="class_TextServerExtension_private_method__font_set_hinting"></span>

void **_font_set_hinting** ( font_rid: [RID](class_rid.md#class_RID), hinting: [Hinting](class_textserver.md#enum_TextServer_Hinting) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_hinting)

Sets font hinting mode. Used by dynamic fonts only.

---

<span id="class_TextServerExtension_private_method__font_set_keep_rounding_remainders"></span>

void **_font_set_keep_rounding_remainders** ( font_rid: [RID](class_rid.md#class_RID), keep_rounding_remainders: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_keep_rounding_remainders)

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

<span id="class_TextServerExtension_private_method__font_set_kerning"></span>

void **_font_set_kerning** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), glyph_pair: [Vector2i](class_vector2i.md#class_Vector2i), kerning: [Vector2](class_vector2.md#class_Vector2) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_kerning)

Sets kerning for the pair of glyphs.

---

<span id="class_TextServerExtension_private_method__font_set_language_support_override"></span>

void **_font_set_language_support_override** ( font_rid: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_language_support_override)

Adds override for [_font_is_language_supported()](class_textserverextension.md#class_TextServerExtension_private_method__font_is_language_supported).

---

<span id="class_TextServerExtension_private_method__font_set_modulate_color_glyphs"></span>

void **_font_set_modulate_color_glyphs** ( font_rid: [RID](class_rid.md#class_RID), modulate: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_modulate_color_glyphs)

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---

<span id="class_TextServerExtension_private_method__font_set_msdf_pixel_range"></span>

void **_font_set_msdf_pixel_range** ( font_rid: [RID](class_rid.md#class_RID), msdf_pixel_range: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_msdf_pixel_range)

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

---

<span id="class_TextServerExtension_private_method__font_set_msdf_size"></span>

void **_font_set_msdf_size** ( font_rid: [RID](class_rid.md#class_RID), msdf_size: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_msdf_size)

Sets source font size used to generate MSDF textures.

---

<span id="class_TextServerExtension_private_method__font_set_multichannel_signed_distance_field"></span>

void **_font_set_multichannel_signed_distance_field** ( font_rid: [RID](class_rid.md#class_RID), msdf: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_multichannel_signed_distance_field)

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

---

<span id="class_TextServerExtension_private_method__font_set_name"></span>

void **_font_set_name** ( font_rid: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_name)

Sets the font family name.

---

<span id="class_TextServerExtension_private_method__font_set_opentype_feature_overrides"></span>

void **_font_set_opentype_feature_overrides** ( font_rid: [RID](class_rid.md#class_RID), overrides: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_opentype_feature_overrides)

Sets font OpenType feature set override.

---

<span id="class_TextServerExtension_private_method__font_set_oversampling"></span>

void **_font_set_oversampling** ( font_rid: [RID](class_rid.md#class_RID), oversampling: [float](class_float.md#class_float) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_oversampling)

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class_Viewport_property_oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

<span id="class_TextServerExtension_private_method__font_set_scale"></span>

void **_font_set_scale** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), scale: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_scale)

Sets scaling factor of the color bitmap font.

---

<span id="class_TextServerExtension_private_method__font_set_script_support_override"></span>

void **_font_set_script_support_override** ( font_rid: [RID](class_rid.md#class_RID), script: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_script_support_override)

Adds override for [_font_is_script_supported()](class_textserverextension.md#class_TextServerExtension_private_method__font_is_script_supported).

---

<span id="class_TextServerExtension_private_method__font_set_spacing"></span>

void **_font_set_spacing** ( font_rid: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_spacing)

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---

<span id="class_TextServerExtension_private_method__font_set_stretch"></span>

void **_font_set_stretch** ( font_rid: [RID](class_rid.md#class_RID), stretch: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_stretch)

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

<span id="class_TextServerExtension_private_method__font_set_style"></span>

void **_font_set_style** ( font_rid: [RID](class_rid.md#class_RID), style: *BitField*\[[FontStyle](class_textserver.md#enum_TextServer_FontStyle)\] ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_style)

Sets the font style flags.

---

<span id="class_TextServerExtension_private_method__font_set_style_name"></span>

void **_font_set_style_name** ( font_rid: [RID](class_rid.md#class_RID), name_style: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_style_name)

Sets the font style name.

---

<span id="class_TextServerExtension_private_method__font_set_subpixel_positioning"></span>

void **_font_set_subpixel_positioning** ( font_rid: [RID](class_rid.md#class_RID), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum_TextServer_SubpixelPositioning) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_subpixel_positioning)

Sets font subpixel glyph positioning mode.

---

<span id="class_TextServerExtension_private_method__font_set_texture_image"></span>

void **_font_set_texture_image** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), image: [Image](class_image.md#class_Image) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_texture_image)

Sets font cache texture image data.

---

<span id="class_TextServerExtension_private_method__font_set_texture_offsets"></span>

void **_font_set_texture_offsets** ( font_rid: [RID](class_rid.md#class_RID), size: [Vector2i](class_vector2i.md#class_Vector2i), texture_index: [int](class_int.md#class_int), offset: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_texture_offsets)

Sets array containing glyph packing data.

---

<span id="class_TextServerExtension_private_method__font_set_transform"></span>

void **_font_set_transform** ( font_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_transform)

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

---

<span id="class_TextServerExtension_private_method__font_set_underline_position"></span>

void **_font_set_underline_position** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_position: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_underline_position)

Sets pixel offset of the underline below the baseline.

---

<span id="class_TextServerExtension_private_method__font_set_underline_thickness"></span>

void **_font_set_underline_thickness** ( font_rid: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), underline_thickness: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_underline_thickness)

Sets thickness of the underline in pixels.

---

<span id="class_TextServerExtension_private_method__font_set_variation_coordinates"></span>

void **_font_set_variation_coordinates** ( font_rid: [RID](class_rid.md#class_RID), variation_coordinates: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_variation_coordinates)

Sets variation coordinates for the specified font cache entry.

---

<span id="class_TextServerExtension_private_method__font_set_weight"></span>

void **_font_set_weight** ( font_rid: [RID](class_rid.md#class_RID), weight: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_set_weight)

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

<span id="class_TextServerExtension_private_method__font_supported_feature_list"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_font_supported_feature_list** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_supported_feature_list)

Returns the dictionary of the supported OpenType features.

---

<span id="class_TextServerExtension_private_method__font_supported_variation_list"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_font_supported_variation_list** ( font_rid: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__font_supported_variation_list)

Returns the dictionary of the supported OpenType variation coordinates.

---

<span id="class_TextServerExtension_private_method__format_number"></span>

[String](class_string.md#class_String) **_format_number** ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__format_number)

**Deprecated:** Use [TranslationServer.format_number()](class_translationserver.md#class_TranslationServer_method_format_number) instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

---

<span id="class_TextServerExtension_private_method__free_rid"></span>

void **_free_rid** ( rid: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__free_rid)

Frees an object created by this [TextServer](class_textserver.md#class_TextServer).

---

<span id="class_TextServerExtension_private_method__get_features"></span>

[int](class_int.md#class_int) **_get_features** ( ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__get_features)

Returns text server features, see [Feature](class_textserver.md#enum_TextServer_Feature).

---

<span id="class_TextServerExtension_private_method__get_hex_code_box_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_get_hex_code_box_size** ( size: [int](class_int.md#class_int), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__get_hex_code_box_size)

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

---

<span id="class_TextServerExtension_private_method__get_name"></span>

[String](class_string.md#class_String) **_get_name** ( ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__get_name)

Returns the name of the server interface.

---

<span id="class_TextServerExtension_private_method__get_support_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **_get_support_data** ( ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__get_support_data)

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

---

<span id="class_TextServerExtension_private_method__get_support_data_filename"></span>

[String](class_string.md#class_String) **_get_support_data_filename** ( ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__get_support_data_filename)

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

---

<span id="class_TextServerExtension_private_method__get_support_data_info"></span>

[String](class_string.md#class_String) **_get_support_data_info** ( ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__get_support_data_info)

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

---

<span id="class_TextServerExtension_private_method__has"></span>

[bool](class_bool.md#class_bool) **_has** ( rid: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__has)

Returns `true` if `rid` is valid resource owned by this text server.

---

<span id="class_TextServerExtension_private_method__has_feature"></span>

[bool](class_bool.md#class_bool) **_has_feature** ( feature: [Feature](class_textserver.md#enum_TextServer_Feature) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__has_feature)

Returns `true` if the server supports a feature.

---

<span id="class_TextServerExtension_private_method__is_confusable"></span>

[int](class_int.md#class_int) **_is_confusable** ( string: [String](class_string.md#class_String), dict: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__is_confusable)

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

---

<span id="class_TextServerExtension_private_method__is_locale_right_to_left"></span>

[bool](class_bool.md#class_bool) **_is_locale_right_to_left** ( locale: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__is_locale_right_to_left)

Returns `true` if locale is right-to-left.

---

<span id="class_TextServerExtension_private_method__is_locale_using_support_data"></span>

[bool](class_bool.md#class_bool) **_is_locale_using_support_data** ( locale: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__is_locale_using_support_data)

Returns `true` if the locale requires text server support data for line/word breaking.

---

<span id="class_TextServerExtension_private_method__is_valid_identifier"></span>

[bool](class_bool.md#class_bool) **_is_valid_identifier** ( string: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__is_valid_identifier)

Returns `true` if `string` is a valid identifier.

---

<span id="class_TextServerExtension_private_method__is_valid_letter"></span>

[bool](class_bool.md#class_bool) **_is_valid_letter** ( unicode: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__is_valid_letter)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_TextServerExtension_private_method__load_support_data"></span>

[bool](class_bool.md#class_bool) **_load_support_data** ( filename: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__load_support_data)

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

---

<span id="class_TextServerExtension_private_method__name_to_tag"></span>

[int](class_int.md#class_int) **_name_to_tag** ( name: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__name_to_tag)

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

---

<span id="class_TextServerExtension_private_method__parse_number"></span>

[String](class_string.md#class_String) **_parse_number** ( number: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__parse_number)

**Deprecated:** Use [TranslationServer.parse_number()](class_translationserver.md#class_TranslationServer_method_parse_number) instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

---

<span id="class_TextServerExtension_private_method__parse_structured_text"></span>

[Array](class_array.md#class_Array)\[[Vector3i](class_vector3i.md#class_Vector3i)\] **_parse_structured_text** ( parser_type: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser), args: [Array](class_array.md#class_Array), text: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__parse_structured_text)

Default implementation of the BiDi algorithm override function.

---

<span id="class_TextServerExtension_private_method__percent_sign"></span>

[String](class_string.md#class_String) **_percent_sign** ( language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__percent_sign)

**Deprecated:** Use [TranslationServer.get_percent_sign()](class_translationserver.md#class_TranslationServer_method_get_percent_sign) instead.

Returns percent sign used in the given `language`.

---

<span id="class_TextServerExtension_private_method__reference_oversampling_level"></span>

void **_reference_oversampling_level** ( oversampling: [float](class_float.md#class_float) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__reference_oversampling_level)

Increases the reference count of the specified oversampling level. This method is called by [Viewport](class_viewport.md#class_Viewport), and should not be used directly.

---

<span id="class_TextServerExtension_private_method__save_support_data"></span>

[bool](class_bool.md#class_bool) **_save_support_data** ( filename: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__save_support_data)

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

---

<span id="class_TextServerExtension_private_method__shaped_get_run_count"></span>

[int](class_int.md#class_int) **_shaped_get_run_count** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_count)

Returns the number of uniform text runs in the buffer.

---

<span id="class_TextServerExtension_private_method__shaped_get_run_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **_shaped_get_run_direction** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_direction)

Returns the direction of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_run_font_rid"></span>

[RID](class_rid.md#class_RID) **_shaped_get_run_font_rid** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_font_rid)

Returns the font RID of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_run_font_size"></span>

[int](class_int.md#class_int) **_shaped_get_run_font_size** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_font_size)

Returns the font size of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_run_language"></span>

[String](class_string.md#class_String) **_shaped_get_run_language** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_language)

Returns the language of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_run_object"></span>

[Variant](class_variant.md#class_Variant) **_shaped_get_run_object** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_object)

Returns the embedded object of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_run_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **_shaped_get_run_range** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_range)

Returns the source text range of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_run_text"></span>

[String](class_string.md#class_String) **_shaped_get_run_text** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_run_text)

Returns the source text of the `index` text run (in visual order).

---

<span id="class_TextServerExtension_private_method__shaped_get_span_count"></span>

[int](class_int.md#class_int) **_shaped_get_span_count** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_count)

Returns number of text spans added using [_shaped_text_add_string()](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_add_string) or [_shaped_text_add_object()](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_add_object).

---

<span id="class_TextServerExtension_private_method__shaped_get_span_embedded_object"></span>

[Variant](class_variant.md#class_Variant) **_shaped_get_span_embedded_object** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_embedded_object)

Returns text embedded object key.

---

<span id="class_TextServerExtension_private_method__shaped_get_span_meta"></span>

[Variant](class_variant.md#class_Variant) **_shaped_get_span_meta** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_meta)

Returns text span metadata.

---

<span id="class_TextServerExtension_private_method__shaped_get_span_object"></span>

[Variant](class_variant.md#class_Variant) **_shaped_get_span_object** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_object)

Returns the text span embedded object key.

---

<span id="class_TextServerExtension_private_method__shaped_get_span_text"></span>

[String](class_string.md#class_String) **_shaped_get_span_text** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_span_text)

Returns the text span source text.

---

<span id="class_TextServerExtension_private_method__shaped_get_text"></span>

[String](class_string.md#class_String) **_shaped_get_text** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_get_text)

Returns the text buffer source text, including object replacement characters.

---

<span id="class_TextServerExtension_private_method__shaped_set_span_update_font"></span>

void **_shaped_set_span_update_font** ( shaped: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_set_span_update_font)

Changes text span font, font size, and OpenType features, without changing the text.

---

<span id="class_TextServerExtension_private_method__shaped_text_add_object"></span>

[bool](class_bool.md#class_bool) **_shaped_text_add_object** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment, length: [int](class_int.md#class_int), baseline: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_add_object)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

<span id="class_TextServerExtension_private_method__shaped_text_add_string"></span>

[bool](class_bool.md#class_bool) **_shaped_text_add_string** ( shaped: [RID](class_rid.md#class_RID), text: [String](class_string.md#class_String), fonts: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], size: [int](class_int.md#class_int), opentype_features: [Dictionary](class_dictionary.md#class_Dictionary), language: [String](class_string.md#class_String), meta: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_add_string)

Adds text span and font to draw it to the text buffer.

---

<span id="class_TextServerExtension_private_method__shaped_text_clear"></span>

void **_shaped_text_clear** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_clear)

Clears text buffer (removes text and inline objects).

---

<span id="class_TextServerExtension_private_method__shaped_text_closest_character_pos"></span>

[int](class_int.md#class_int) **_shaped_text_closest_character_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_closest_character_pos)

Returns composite character position closest to the `pos`.

---

<span id="class_TextServerExtension_private_method__shaped_text_draw"></span>

void **_shaped_text_draw** ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float), clip_r: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_draw)

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextServerExtension_private_method__shaped_text_draw_outline"></span>

void **_shaped_text_draw_outline** ( shaped: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), clip_l: [float](class_float.md#class_float), clip_r: [float](class_float.md#class_float), outline_size: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), oversampling: [float](class_float.md#class_float) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_draw_outline)

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

<span id="class_TextServerExtension_private_method__shaped_text_duplicate"></span>

[RID](class_rid.md#class_RID) **_shaped_text_duplicate** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_duplicate)

Duplicates shaped text buffer.

---

<span id="class_TextServerExtension_private_method__shaped_text_fit_to_width"></span>

[float](class_float.md#class_float) **_shaped_text_fit_to_width** ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), justification_flags: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_fit_to_width)

Adjusts text width to fit to specified width, returns new text width.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_ascent"></span>

[float](class_float.md#class_float) **_shaped_text_get_ascent** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ascent)

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---

<span id="class_TextServerExtension_private_method__shaped_text_get_carets"></span>

void **_shaped_text_get_carets** ( shaped: [RID](class_rid.md#class_RID), position: [int](class_int.md#class_int), caret: `CaretInfo*` ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_carets)

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_character_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_shaped_text_get_character_breaks** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_character_breaks)

Returns array of the composite character boundaries.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_custom_ellipsis"></span>

[int](class_int.md#class_int) **_shaped_text_get_custom_ellipsis** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_custom_ellipsis)

Returns ellipsis character used for text clipping.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_custom_punctuation"></span>

[String](class_string.md#class_String) **_shaped_text_get_custom_punctuation** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_custom_punctuation)

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_descent"></span>

[float](class_float.md#class_float) **_shaped_text_get_descent** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_descent)

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---

<span id="class_TextServerExtension_private_method__shaped_text_get_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **_shaped_text_get_direction** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_direction)

Returns direction of the text.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_dominant_direction_in_range"></span>

[int](class_int.md#class_int) **_shaped_text_get_dominant_direction_in_range** ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_dominant_direction_in_range)

Returns dominant direction of in the range of text.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyph_count"></span>

[int](class_int.md#class_int) **_shaped_text_get_ellipsis_glyph_count** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyph_count)

Returns number of glyphs in the ellipsis.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyphs"></span>

`const Glyph*` **_shaped_text_get_ellipsis_glyphs** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyphs)

Returns array of the glyphs in the ellipsis.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_ellipsis_pos"></span>

[int](class_int.md#class_int) **_shaped_text_get_ellipsis_pos** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_ellipsis_pos)

Returns position of the ellipsis.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_glyph_count"></span>

[int](class_int.md#class_int) **_shaped_text_get_glyph_count** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_glyph_count)

Returns number of glyphs in the buffer.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_glyphs"></span>

`const Glyph*` **_shaped_text_get_glyphs** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_glyphs)

Returns an array of glyphs in the visual order.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_grapheme_bounds"></span>

[Vector2](class_vector2.md#class_Vector2) **_shaped_text_get_grapheme_bounds** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_grapheme_bounds)

Returns composite character's bounds as offsets from the start of the line.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_inferred_direction"></span>

[Direction](class_textserver.md#enum_TextServer_Direction) **_shaped_text_get_inferred_direction** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_inferred_direction)

Returns direction of the text, inferred by the BiDi algorithm.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_line_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_shaped_text_get_line_breaks** ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), start: [int](class_int.md#class_int), break_flags: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_line_breaks)

Breaks text to the lines and returns character ranges for each line.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_line_breaks_adv"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_shaped_text_get_line_breaks_adv** ( shaped: [RID](class_rid.md#class_RID), width: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), start: [int](class_int.md#class_int), once: [bool](class_bool.md#class_bool), break_flags: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_line_breaks_adv)

Breaks text to the lines and columns. Returns character ranges for each segment.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_object_glyph"></span>

[int](class_int.md#class_int) **_shaped_text_get_object_glyph** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_object_glyph)

Returns the glyph index of the inline object.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_object_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **_shaped_text_get_object_range** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_object_range)

Returns the character range of the inline object.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_object_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **_shaped_text_get_object_rect** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_object_rect)

Returns bounding rectangle of the inline object.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_objects"></span>

[Array](class_array.md#class_Array) **_shaped_text_get_objects** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_objects)

Returns array of inline objects.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_orientation"></span>

[Orientation](class_textserver.md#enum_TextServer_Orientation) **_shaped_text_get_orientation** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_orientation)

Returns text orientation.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_parent"></span>

[RID](class_rid.md#class_RID) **_shaped_text_get_parent** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_parent)

Returns the parent buffer from which the substring originates.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_preserve_control"></span>

[bool](class_bool.md#class_bool) **_shaped_text_get_preserve_control** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_preserve_control)

Returns `true` if text buffer is configured to display control characters.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_preserve_invalid"></span>

[bool](class_bool.md#class_bool) **_shaped_text_get_preserve_invalid** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_preserve_invalid)

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **_shaped_text_get_range** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_range)

Returns substring buffer character range in the parent buffer.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_selection"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **_shaped_text_get_selection** ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), end: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_selection)

Returns selection rectangles for the specified character range.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_shaped_text_get_size** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_size)

Returns size of the text.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_spacing"></span>

[int](class_int.md#class_int) **_shaped_text_get_spacing** ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_spacing)

Returns extra spacing added between glyphs or lines in pixels.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_trim_pos"></span>

[int](class_int.md#class_int) **_shaped_text_get_trim_pos** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_trim_pos)

Returns the position of the overrun trim.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_underline_position"></span>

[float](class_float.md#class_float) **_shaped_text_get_underline_position** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_underline_position)

Returns pixel offset of the underline below the baseline.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_underline_thickness"></span>

[float](class_float.md#class_float) **_shaped_text_get_underline_thickness** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_underline_thickness)

Returns thickness of the underline.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_width"></span>

[float](class_float.md#class_float) **_shaped_text_get_width** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_width)

Returns width (for horizontal layout) or height (for vertical) of the text.

---

<span id="class_TextServerExtension_private_method__shaped_text_get_word_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_shaped_text_get_word_breaks** ( shaped: [RID](class_rid.md#class_RID), grapheme_flags: *BitField*\[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\], skip_grapheme_flags: *BitField*\[[GraphemeFlag](class_textserver.md#enum_TextServer_GraphemeFlag)\] ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_get_word_breaks)

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

---

<span id="class_TextServerExtension_private_method__shaped_text_has_object"></span>

[bool](class_bool.md#class_bool) **_shaped_text_has_object** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_has_object)

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---

<span id="class_TextServerExtension_private_method__shaped_text_hit_test_grapheme"></span>

[int](class_int.md#class_int) **_shaped_text_hit_test_grapheme** ( shaped: [RID](class_rid.md#class_RID), coord: [float](class_float.md#class_float) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_hit_test_grapheme)

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

---

<span id="class_TextServerExtension_private_method__shaped_text_hit_test_position"></span>

[int](class_int.md#class_int) **_shaped_text_hit_test_position** ( shaped: [RID](class_rid.md#class_RID), coord: [float](class_float.md#class_float) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_hit_test_position)

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---

<span id="class_TextServerExtension_private_method__shaped_text_is_ready"></span>

[bool](class_bool.md#class_bool) **_shaped_text_is_ready** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_is_ready)

Returns `true` if buffer is successfully shaped.

---

<span id="class_TextServerExtension_private_method__shaped_text_next_character_pos"></span>

[int](class_int.md#class_int) **_shaped_text_next_character_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_next_character_pos)

Returns composite character end position closest to the `pos`.

---

<span id="class_TextServerExtension_private_method__shaped_text_next_grapheme_pos"></span>

[int](class_int.md#class_int) **_shaped_text_next_grapheme_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_next_grapheme_pos)

Returns grapheme end position closest to the `pos`.

---

<span id="class_TextServerExtension_private_method__shaped_text_overrun_trim_to_width"></span>

void **_shaped_text_overrun_trim_to_width** ( shaped: [RID](class_rid.md#class_RID), width: [float](class_float.md#class_float), trim_flags: *BitField*\[[TextOverrunFlag](class_textserver.md#enum_TextServer_TextOverrunFlag)\] ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_overrun_trim_to_width)

Trims text if it exceeds the given width.

---

<span id="class_TextServerExtension_private_method__shaped_text_prev_character_pos"></span>

[int](class_int.md#class_int) **_shaped_text_prev_character_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_prev_character_pos)

Returns composite character start position closest to the `pos`.

---

<span id="class_TextServerExtension_private_method__shaped_text_prev_grapheme_pos"></span>

[int](class_int.md#class_int) **_shaped_text_prev_grapheme_pos** ( shaped: [RID](class_rid.md#class_RID), pos: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_prev_grapheme_pos)

Returns grapheme start position closest to the `pos`.

---

<span id="class_TextServerExtension_private_method__shaped_text_resize_object"></span>

[bool](class_bool.md#class_bool) **_shaped_text_resize_object** ( shaped: [RID](class_rid.md#class_RID), key: [Variant](class_variant.md#class_Variant), size: [Vector2](class_vector2.md#class_Vector2), inline_align: InlineAlignment, baseline: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_resize_object)

Sets new size and alignment of embedded object.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_bidi_override"></span>

void **_shaped_text_set_bidi_override** ( shaped: [RID](class_rid.md#class_RID), override: [Array](class_array.md#class_Array) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_bidi_override)

Overrides BiDi for the structured text.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_custom_ellipsis"></span>

void **_shaped_text_set_custom_ellipsis** ( shaped: [RID](class_rid.md#class_RID), char: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_custom_ellipsis)

Sets ellipsis character used for text clipping.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_custom_punctuation"></span>

void **_shaped_text_set_custom_punctuation** ( shaped: [RID](class_rid.md#class_RID), punct: [String](class_string.md#class_String) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_custom_punctuation)

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_direction"></span>

void **_shaped_text_set_direction** ( shaped: [RID](class_rid.md#class_RID), direction: [Direction](class_textserver.md#enum_TextServer_Direction) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_direction)

Sets desired text direction. If set to [TextServer.DIRECTION_AUTO](class_textserver.md#class_TextServer_constant_DIRECTION_AUTO), direction will be detected based on the buffer contents and current locale.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_orientation"></span>

void **_shaped_text_set_orientation** ( shaped: [RID](class_rid.md#class_RID), orientation: [Orientation](class_textserver.md#enum_TextServer_Orientation) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_orientation)

Sets desired text orientation.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_preserve_control"></span>

void **_shaped_text_set_preserve_control** ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_preserve_control)

If set to `true` text buffer will display control characters.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_preserve_invalid"></span>

void **_shaped_text_set_preserve_invalid** ( shaped: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_preserve_invalid)

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

---

<span id="class_TextServerExtension_private_method__shaped_text_set_spacing"></span>

void **_shaped_text_set_spacing** ( shaped: [RID](class_rid.md#class_RID), spacing: [SpacingType](class_textserver.md#enum_TextServer_SpacingType), value: [int](class_int.md#class_int) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_set_spacing)

Sets extra spacing added between glyphs or lines in pixels.

---

<span id="class_TextServerExtension_private_method__shaped_text_shape"></span>

[bool](class_bool.md#class_bool) **_shaped_text_shape** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_shape)

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

---

<span id="class_TextServerExtension_private_method__shaped_text_sort_logical"></span>

`const Glyph*` **_shaped_text_sort_logical** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_sort_logical)

Returns text glyphs in the logical order.

---

<span id="class_TextServerExtension_private_method__shaped_text_substr"></span>

[RID](class_rid.md#class_RID) **_shaped_text_substr** ( shaped: [RID](class_rid.md#class_RID), start: [int](class_int.md#class_int), length: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_substr)

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

---

<span id="class_TextServerExtension_private_method__shaped_text_tab_align"></span>

[float](class_float.md#class_float) **_shaped_text_tab_align** ( shaped: [RID](class_rid.md#class_RID), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_tab_align)

Aligns shaped text to the given tab-stops.

---

<span id="class_TextServerExtension_private_method__shaped_text_update_breaks"></span>

[bool](class_bool.md#class_bool) **_shaped_text_update_breaks** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_update_breaks)

Updates break points in the shaped text. This method is called by default implementation of text breaking functions.

---

<span id="class_TextServerExtension_private_method__shaped_text_update_justification_ops"></span>

[bool](class_bool.md#class_bool) **_shaped_text_update_justification_ops** ( shaped: [RID](class_rid.md#class_RID) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__shaped_text_update_justification_ops)

Updates justification points in the shaped text. This method is called by default implementation of text justification functions.

---

<span id="class_TextServerExtension_private_method__spoof_check"></span>

[bool](class_bool.md#class_bool) **_spoof_check** ( string: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__spoof_check)

Returns `true` if `string` is likely to be an attempt at confusing the reader.

---

<span id="class_TextServerExtension_private_method__string_get_character_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_string_get_character_breaks** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__string_get_character_breaks)

Returns array of the composite character boundaries.

---

<span id="class_TextServerExtension_private_method__string_get_word_breaks"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_string_get_word_breaks** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String), chars_per_line: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__string_get_word_breaks)

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

---

<span id="class_TextServerExtension_private_method__string_to_lower"></span>

[String](class_string.md#class_String) **_string_to_lower** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__string_to_lower)

Returns the string converted to `lowercase`.

---

<span id="class_TextServerExtension_private_method__string_to_title"></span>

[String](class_string.md#class_String) **_string_to_title** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__string_to_title)

Returns the string converted to `Title Case`.

---

<span id="class_TextServerExtension_private_method__string_to_upper"></span>

[String](class_string.md#class_String) **_string_to_upper** ( string: [String](class_string.md#class_String), language: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__string_to_upper)

Returns the string converted to `UPPERCASE`.

---

<span id="class_TextServerExtension_private_method__strip_diacritics"></span>

[String](class_string.md#class_String) **_strip_diacritics** ( string: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__strip_diacritics)

Strips diacritics from the string.

---

<span id="class_TextServerExtension_private_method__tag_to_name"></span>

[String](class_string.md#class_String) **_tag_to_name** ( tag: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__tag_to_name)

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.

---

<span id="class_TextServerExtension_private_method__unreference_oversampling_level"></span>

void **_unreference_oversampling_level** ( oversampling: [float](class_float.md#class_float) ) *virtual* [🔗](class_textserverextension.md#class_TextServerExtension_private_method__unreference_oversampling_level)

Decreases the reference count of the specified oversampling level, and frees the font cache for oversampling level when the reference count reaches zero. This method is called by [Viewport](class_viewport.md#class_Viewport), and should not be used directly.
