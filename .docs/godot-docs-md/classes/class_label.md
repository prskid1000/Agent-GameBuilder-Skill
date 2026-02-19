.. meta::
	:keywords: text

<span id="class_Label"></span>

## Label

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control for displaying plain text.

### Description

A control for displaying plain text. It gives you control over the horizontal and vertical alignment and can wrap the text inside the node's bounding rectangle. It doesn't support bold, italics, or other rich text formatting. For that, use [RichTextLabel](class_richtextlabel.md#class_RichTextLabel) instead.

 **Note:** A single Label node is not designed to display huge amounts of text. To display large amounts of text in a single node, consider using [RichTextLabel](class_richtextlabel.md#class_RichTextLabel) instead as it supports features like an integrated scroll bar and threading. [RichTextLabel](class_richtextlabel.md#class_RichTextLabel) generally performs better when displaying large amounts of text (several pages or more).

### Tutorials

- 2D Dodge The Creeps Demo

### Properties


| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [autowrap_mode](class_label.md#class_Label_property_autowrap_mode) | `0` |
| --- | --- | --- |
| bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] | [autowrap_trim_flags](class_label.md#class_Label_property_autowrap_trim_flags) | `192` |
| [bool](class_bool.md#class_bool) | [clip_text](class_label.md#class_Label_property_clip_text) | `false` |
| [String](class_string.md#class_String) | [ellipsis_char](class_label.md#class_Label_property_ellipsis_char) | `"…"` |
| HorizontalAlignment | [horizontal_alignment](class_label.md#class_Label_property_horizontal_alignment) | `0` |
| bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] | [justification_flags](class_label.md#class_Label_property_justification_flags) | `163` |
| [LabelSettings](class_labelsettings.md#class_LabelSettings) | [label_settings](class_label.md#class_Label_property_label_settings) |
| [String](class_string.md#class_String) | [language](class_label.md#class_Label_property_language) | `""` |
| [int](class_int.md#class_int) | [lines_skipped](class_label.md#class_Label_property_lines_skipped) | `0` |
| [int](class_int.md#class_int) | [max_lines_visible](class_label.md#class_Label_property_max_lines_visible) | `-1` |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | mouse_filter | `2` (overrides [Control](class_control.md#class_Control_property_mouse_filter)) |
| [String](class_string.md#class_String) | [paragraph_separator](class_label.md#class_Label_property_paragraph_separator) | `"\\n"` |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_vertical | `4` (overrides [Control](class_control.md#class_Control_property_size_flags_vertical)) |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_label.md#class_Label_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_label.md#class_Label_property_structured_text_bidi_override_options) | `[]` |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [tab_stops](class_label.md#class_Label_property_tab_stops) | `PackedFloat32Array()` |
| [String](class_string.md#class_String) | [text](class_label.md#class_Label_property_text) | `""` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_label.md#class_Label_property_text_direction) | `0` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [text_overrun_behavior](class_label.md#class_Label_property_text_overrun_behavior) | `0` |
| [bool](class_bool.md#class_bool) | [uppercase](class_label.md#class_Label_property_uppercase) | `false` |
| VerticalAlignment | [vertical_alignment](class_label.md#class_Label_property_vertical_alignment) | `0` |
| [int](class_int.md#class_int) | [visible_characters](class_label.md#class_Label_property_visible_characters) | `-1` |
| [VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) | [visible_characters_behavior](class_label.md#class_Label_property_visible_characters_behavior) | `0` |
| [float](class_float.md#class_float) | [visible_ratio](class_label.md#class_Label_property_visible_ratio) | `1.0` |

### Methods


| [Rect2](class_rect2.md#class_Rect2) | [get_character_bounds](class_label.md#class_Label_method_get_character_bounds) ( pos: [int](class_int.md#class_int) ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_line_count](class_label.md#class_Label_method_get_line_count) ( ) const |
| [int](class_int.md#class_int) | [get_line_height](class_label.md#class_Label_method_get_line_height) ( line: [int](class_int.md#class_int) = -1 ) const |
| [int](class_int.md#class_int) | [get_total_character_count](class_label.md#class_Label_method_get_total_character_count) ( ) const |
| [int](class_int.md#class_int) | [get_visible_line_count](class_label.md#class_Label_method_get_visible_line_count) ( ) const |

### Theme Properties


| [Color](class_color.md#class_Color) | [font_color](class_label.md#class_Label_theme_color_font_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_outline_color](class_label.md#class_Label_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_shadow_color](class_label.md#class_Label_theme_color_font_shadow_color) | `Color(0, 0, 0, 0)` |
| [int](class_int.md#class_int) | [line_spacing](class_label.md#class_Label_theme_constant_line_spacing) | `3` |
| [int](class_int.md#class_int) | [outline_size](class_label.md#class_Label_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [paragraph_spacing](class_label.md#class_Label_theme_constant_paragraph_spacing) | `0` |
| [int](class_int.md#class_int) | [shadow_offset_x](class_label.md#class_Label_theme_constant_shadow_offset_x) | `1` |
| [int](class_int.md#class_int) | [shadow_offset_y](class_label.md#class_Label_theme_constant_shadow_offset_y) | `1` |
| [int](class_int.md#class_int) | [shadow_outline_size](class_label.md#class_Label_theme_constant_shadow_outline_size) | `1` |
| [Font](class_font.md#class_Font) | [font](class_label.md#class_Label_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_label.md#class_Label_theme_font_size_font_size) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_label.md#class_Label_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal](class_label.md#class_Label_theme_style_normal) |

---

### Property Descriptions

<span id="class_Label_property_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **autowrap_mode** = `0` [🔗](class_label.md#class_Label_property_autowrap_mode)

- void **set_autowrap_mode** ( value: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) )
- [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( )

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

---

<span id="class_Label_property_autowrap_trim_flags"></span>

*BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **autowrap_trim_flags** = `192` [🔗](class_label.md#class_Label_property_autowrap_trim_flags)

- void **set_autowrap_trim_flags** ( value: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] )
- *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **get_autowrap_trim_flags** ( )

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES) for more info.

---

<span id="class_Label_property_clip_text"></span>

[bool](class_bool.md#class_bool) **clip_text** = `false` [🔗](class_label.md#class_Label_property_clip_text)

- void **set_clip_text** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_clipping_text** ( )

If `true`, the Label only shows the text that fits inside its bounding rectangle and will clip text horizontally.

---

<span id="class_Label_property_ellipsis_char"></span>

[String](class_string.md#class_String) **ellipsis_char** = `"…"` [🔗](class_label.md#class_Label_property_ellipsis_char)

- void **set_ellipsis_char** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_ellipsis_char** ( )

Ellipsis character used for text clipping.

---

<span id="class_Label_property_horizontal_alignment"></span>

HorizontalAlignment **horizontal_alignment** = `0` [🔗](class_label.md#class_Label_property_horizontal_alignment)

- void **set_horizontal_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_horizontal_alignment** ( )

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

<span id="class_Label_property_justification_flags"></span>

*BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **justification_flags** = `163` [🔗](class_label.md#class_Label_property_justification_flags)

- void **set_justification_flags** ( value: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] )
- *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **get_justification_flags** ( )

Line fill alignment rules.

---

<span id="class_Label_property_label_settings"></span>

[LabelSettings](class_labelsettings.md#class_LabelSettings) **label_settings** [🔗](class_label.md#class_Label_property_label_settings)

- void **set_label_settings** ( value: [LabelSettings](class_labelsettings.md#class_LabelSettings) )
- [LabelSettings](class_labelsettings.md#class_LabelSettings) **get_label_settings** ( )

A [LabelSettings](class_labelsettings.md#class_LabelSettings) resource that can be shared between multiple **Label** nodes. Takes priority over theme properties.

---

<span id="class_Label_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_label.md#class_Label_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_Label_property_lines_skipped"></span>

[int](class_int.md#class_int) **lines_skipped** = `0` [🔗](class_label.md#class_Label_property_lines_skipped)

- void **set_lines_skipped** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_lines_skipped** ( )

The number of the lines ignored and not displayed from the start of the [text](class_label.md#class_Label_property_text) value.

---

<span id="class_Label_property_max_lines_visible"></span>

[int](class_int.md#class_int) **max_lines_visible** = `-1` [🔗](class_label.md#class_Label_property_max_lines_visible)

- void **set_max_lines_visible** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_lines_visible** ( )

Limits the lines of text the node shows on screen.

---

<span id="class_Label_property_paragraph_separator"></span>

[String](class_string.md#class_String) **paragraph_separator** = `"\\n"` [🔗](class_label.md#class_Label_property_paragraph_separator)

- void **set_paragraph_separator** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_paragraph_separator** ( )

String used as a paragraph separator. Each paragraph is processed independently, in its own BiDi context.

---

<span id="class_Label_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_label.md#class_Label_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_Label_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_label.md#class_Label_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_Label_property_tab_stops"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **tab_stops** = `PackedFloat32Array()` [🔗](class_label.md#class_Label_property_tab_stops)

- void **set_tab_stops** ( value: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) )
- [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_tab_stops** ( )

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) for more details.

---

<span id="class_Label_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_label.md#class_Label_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The text to display on screen.

---

<span id="class_Label_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_label.md#class_Label_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_Label_property_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **text_overrun_behavior** = `0` [🔗](class_label.md#class_Label_property_text_overrun_behavior)

- void **set_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( )

The clipping behavior when the text exceeds the node's bounding rectangle.

---

<span id="class_Label_property_uppercase"></span>

[bool](class_bool.md#class_bool) **uppercase** = `false` [🔗](class_label.md#class_Label_property_uppercase)

- void **set_uppercase** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_uppercase** ( )

If `true`, all the text displays as UPPERCASE.

---

<span id="class_Label_property_vertical_alignment"></span>

VerticalAlignment **vertical_alignment** = `0` [🔗](class_label.md#class_Label_property_vertical_alignment)

- void **set_vertical_alignment** ( value: VerticalAlignment )
- VerticalAlignment **get_vertical_alignment** ( )

Controls the text's vertical alignment. Supports top, center, bottom, and fill.

---

<span id="class_Label_property_visible_characters"></span>

[int](class_int.md#class_int) **visible_characters** = `-1` [🔗](class_label.md#class_Label_property_visible_characters)

- void **set_visible_characters** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_visible_characters** ( )

The number of characters to display. If set to `-1`, all characters are displayed. This can be useful when animating the text appearing in a dialog box.

 **Note:** Setting this property updates [visible_ratio](class_label.md#class_Label_property_visible_ratio) accordingly.

 **Note:** Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.

---

<span id="class_Label_property_visible_characters_behavior"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **visible_characters_behavior** = `0` [🔗](class_label.md#class_Label_property_visible_characters_behavior)

- void **set_visible_characters_behavior** ( value: [VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) )
- [VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **get_visible_characters_behavior** ( )

The clipping behavior when [visible_characters](class_label.md#class_Label_property_visible_characters) or [visible_ratio](class_label.md#class_Label_property_visible_ratio) is set.

---

<span id="class_Label_property_visible_ratio"></span>

[float](class_float.md#class_float) **visible_ratio** = `1.0` [🔗](class_label.md#class_Label_property_visible_ratio)

- void **set_visible_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_visible_ratio** ( )

The fraction of characters to display, relative to the total number of characters (see [get_total_character_count()](class_label.md#class_Label_method_get_total_character_count)). If set to `1.0`, all characters are displayed. If set to `0.5`, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.

 **Note:** Setting this property updates [visible_characters](class_label.md#class_Label_property_visible_characters) accordingly.

---

### Method Descriptions

<span id="class_Label_method_get_character_bounds"></span>

[Rect2](class_rect2.md#class_Rect2) **get_character_bounds** ( pos: [int](class_int.md#class_int) ) *const* [🔗](class_label.md#class_Label_method_get_character_bounds)

Returns the bounding rectangle of the character at position `pos` in the label's local coordinate system. If the character is a non-visual character or `pos` is outside the valid range, an empty [Rect2](class_rect2.md#class_Rect2) is returned. If the character is a part of a composite grapheme, the bounding rectangle of the whole grapheme is returned.

---

<span id="class_Label_method_get_line_count"></span>

[int](class_int.md#class_int) **get_line_count** ( ) *const* [🔗](class_label.md#class_Label_method_get_line_count)

Returns the number of lines of text the Label has.

---

<span id="class_Label_method_get_line_height"></span>

[int](class_int.md#class_int) **get_line_height** ( line: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_label.md#class_Label_method_get_line_height)

Returns the height of the line `line`.

If `line` is set to `-1`, returns the biggest line height.

If there are no lines, returns font size in pixels.

---

<span id="class_Label_method_get_total_character_count"></span>

[int](class_int.md#class_int) **get_total_character_count** ( ) *const* [🔗](class_label.md#class_Label_method_get_total_character_count)

Returns the total number of printable characters in the text (excluding spaces and newlines).

---

<span id="class_Label_method_get_visible_line_count"></span>

[int](class_int.md#class_int) **get_visible_line_count** ( ) *const* [🔗](class_label.md#class_Label_method_get_visible_line_count)

Returns the number of lines shown. Useful if the **Label**'s height cannot currently display all lines.

---

### Theme Property Descriptions

<span id="class_Label_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(1, 1, 1, 1)` [🔗](class_label.md#class_Label_theme_color_font_color)

Default text [Color](class_color.md#class_Color) of the **Label**.

---

<span id="class_Label_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_label.md#class_Label_theme_color_font_outline_color)

The color of text outline.

---

<span id="class_Label_theme_color_font_shadow_color"></span>

[Color](class_color.md#class_Color) **font_shadow_color** = `Color(0, 0, 0, 0)` [🔗](class_label.md#class_Label_theme_color_font_shadow_color)

[Color](class_color.md#class_Color) of the text's shadow effect.

---

<span id="class_Label_theme_constant_line_spacing"></span>

[int](class_int.md#class_int) **line_spacing** = `3` [🔗](class_label.md#class_Label_theme_constant_line_spacing)

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_Label_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_label.md#class_Label_theme_constant_outline_size)

Text outline size.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_label.md#class_Label_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

 **Note:** Using a value that is larger than half the font size is not recommended, as the font outline may fail to be fully closed in this case.

---

<span id="class_Label_theme_constant_paragraph_spacing"></span>

[int](class_int.md#class_int) **paragraph_spacing** = `0` [🔗](class_label.md#class_Label_theme_constant_paragraph_spacing)

Vertical space between paragraphs. Added on top of [line_spacing](class_label.md#class_Label_theme_constant_line_spacing).

---

<span id="class_Label_theme_constant_shadow_offset_x"></span>

[int](class_int.md#class_int) **shadow_offset_x** = `1` [🔗](class_label.md#class_Label_theme_constant_shadow_offset_x)

The horizontal offset of the text's shadow.

---

<span id="class_Label_theme_constant_shadow_offset_y"></span>

[int](class_int.md#class_int) **shadow_offset_y** = `1` [🔗](class_label.md#class_Label_theme_constant_shadow_offset_y)

The vertical offset of the text's shadow.

---

<span id="class_Label_theme_constant_shadow_outline_size"></span>

[int](class_int.md#class_int) **shadow_outline_size** = `1` [🔗](class_label.md#class_Label_theme_constant_shadow_outline_size)

The size of the shadow outline.

---

<span id="class_Label_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_label.md#class_Label_theme_font_font)

[Font](class_font.md#class_Font) used for the **Label**'s text.

---

<span id="class_Label_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_label.md#class_Label_theme_font_size_font_size)

Font size of the **Label**'s text.

---

<span id="class_Label_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_label.md#class_Label_theme_style_focus)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Label** is focused (when used with assistive apps).

---

<span id="class_Label_theme_style_normal"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal** [🔗](class_label.md#class_Label_theme_style_normal)

Background [StyleBox](class_stylebox.md#class_StyleBox) for the **Label**.
