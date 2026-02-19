<span id="class_LinkButton"></span>

## LinkButton

**Inherits:** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A button that represents a link.

### Description

A button that represents a link. This type of button is primarily used for interactions that cause a context change (like linking to a web page).

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

### Properties


| [String](class_string.md#class_String) | [ellipsis_char](class_linkbutton.md#class_LinkButton_property_ellipsis_char) | `"…"` |
| --- | --- | --- |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `3` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [String](class_string.md#class_String) | [language](class_linkbutton.md#class_LinkButton_property_language) | `""` |
| [CursorShape](class_control.md#enum_Control_CursorShape) | mouse_default_cursor_shape | `2` (overrides [Control](class_control.md#class_Control_property_mouse_default_cursor_shape)) |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_linkbutton.md#class_LinkButton_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_linkbutton.md#class_LinkButton_property_structured_text_bidi_override_options) | `[]` |
| [String](class_string.md#class_String) | [text](class_linkbutton.md#class_LinkButton_property_text) | `""` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_linkbutton.md#class_LinkButton_property_text_direction) | `0` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [text_overrun_behavior](class_linkbutton.md#class_LinkButton_property_text_overrun_behavior) | `0` |
| [UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) | [underline](class_linkbutton.md#class_LinkButton_property_underline) | `0` |
| [String](class_string.md#class_String) | [uri](class_linkbutton.md#class_LinkButton_property_uri) | `""` |

### Theme Properties


| [Color](class_color.md#class_Color) | [font_color](class_linkbutton.md#class_LinkButton_theme_color_font_color) | `Color(0.875, 0.875, 0.875, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_disabled_color](class_linkbutton.md#class_LinkButton_theme_color_font_disabled_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_focus_color](class_linkbutton.md#class_LinkButton_theme_color_font_focus_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hover_color](class_linkbutton.md#class_LinkButton_theme_color_font_hover_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hover_pressed_color](class_linkbutton.md#class_LinkButton_theme_color_font_hover_pressed_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_linkbutton.md#class_LinkButton_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_pressed_color](class_linkbutton.md#class_LinkButton_theme_color_font_pressed_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [outline_size](class_linkbutton.md#class_LinkButton_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [underline_spacing](class_linkbutton.md#class_LinkButton_theme_constant_underline_spacing) | `2` |
| [Font](class_font.md#class_Font) | [font](class_linkbutton.md#class_LinkButton_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_linkbutton.md#class_LinkButton_theme_font_size_font_size) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_linkbutton.md#class_LinkButton_theme_style_focus) |

---

### Enumerations

<span id="enum_LinkButton_UnderlineMode"></span>

enum **UnderlineMode**: [🔗](class_linkbutton.md#enum_LinkButton_UnderlineMode)

<span id="class_LinkButton_constant_UNDERLINE_MODE_ALWAYS"></span>

[UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) **UNDERLINE_MODE_ALWAYS** = `0`

The LinkButton will always show an underline at the bottom of its text.

<span id="class_LinkButton_constant_UNDERLINE_MODE_ON_HOVER"></span>

[UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) **UNDERLINE_MODE_ON_HOVER** = `1`

The LinkButton will show an underline at the bottom of its text when the mouse cursor is over it.

<span id="class_LinkButton_constant_UNDERLINE_MODE_NEVER"></span>

[UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) **UNDERLINE_MODE_NEVER** = `2`

The LinkButton will never show an underline at the bottom of its text.

---

### Property Descriptions

<span id="class_LinkButton_property_ellipsis_char"></span>

[String](class_string.md#class_String) **ellipsis_char** = `"…"` [🔗](class_linkbutton.md#class_LinkButton_property_ellipsis_char)

- void **set_ellipsis_char** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_ellipsis_char** ( )

Ellipsis character used for text clipping.

---

<span id="class_LinkButton_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_linkbutton.md#class_LinkButton_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_LinkButton_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_linkbutton.md#class_LinkButton_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_LinkButton_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_linkbutton.md#class_LinkButton_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_LinkButton_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_linkbutton.md#class_LinkButton_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The button's text that will be displayed inside the button's area.

---

<span id="class_LinkButton_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_linkbutton.md#class_LinkButton_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_LinkButton_property_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **text_overrun_behavior** = `0` [🔗](class_linkbutton.md#class_LinkButton_property_text_overrun_behavior)

- void **set_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( )

Sets the clipping behavior when the text exceeds the node's bounding rectangle.

---

<span id="class_LinkButton_property_underline"></span>

[UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) **underline** = `0` [🔗](class_linkbutton.md#class_LinkButton_property_underline)

- void **set_underline_mode** ( value: [UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) )
- [UnderlineMode](class_linkbutton.md#enum_LinkButton_UnderlineMode) **get_underline_mode** ( )

The underline mode to use for the text.

---

<span id="class_LinkButton_property_uri"></span>

[String](class_string.md#class_String) **uri** = `""` [🔗](class_linkbutton.md#class_LinkButton_property_uri)

- void **set_uri** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_uri** ( )

The URI for this **LinkButton**. If set to a valid URI, pressing the button opens the URI using the operating system's default program for the protocol (via [OS.shell_open()](class_os.md#class_OS_method_shell_open)). HTTP and HTTPS URLs open the default web browser.

.. tabs::

```
```

    uri = "https://godotengine.org"  # Opens the URL in the default web browser.
    uri = "C:\SomeFolder"  # Opens the file explorer at the given path.
    uri = "C:\SomeImage.png"  # Opens the given image in the default viewing app.

```
```

    Uri = "https://godotengine.org"; // Opens the URL in the default web browser.
    Uri = "C:\SomeFolder"; // Opens the file explorer at the given path.
    Uri = "C:\SomeImage.png"; // Opens the given image in the default viewing app.

---

### Theme Property Descriptions

<span id="class_LinkButton_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_color)

Default text [Color](class_color.md#class_Color) of the **LinkButton**.

---

<span id="class_LinkButton_theme_color_font_disabled_color"></span>

[Color](class_color.md#class_Color) **font_disabled_color** = `Color(0, 0, 0, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_disabled_color)

Text [Color](class_color.md#class_Color) used when the **LinkButton** is disabled.

---

<span id="class_LinkButton_theme_color_font_focus_color"></span>

[Color](class_color.md#class_Color) **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_focus_color)

Text [Color](class_color.md#class_Color) used when the **LinkButton** is focused. Only replaces the normal text color of the button. Disabled, hovered, and pressed states take precedence over this color.

---

<span id="class_LinkButton_theme_color_font_hover_color"></span>

[Color](class_color.md#class_Color) **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_hover_color)

Text [Color](class_color.md#class_Color) used when the **LinkButton** is being hovered.

---

<span id="class_LinkButton_theme_color_font_hover_pressed_color"></span>

[Color](class_color.md#class_Color) **font_hover_pressed_color** = `Color(0, 0, 0, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_hover_pressed_color)

Text [Color](class_color.md#class_Color) used when the **LinkButton** is being hovered and pressed.

---

<span id="class_LinkButton_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_outline_color)

The tint of text outline of the **LinkButton**.

---

<span id="class_LinkButton_theme_color_font_pressed_color"></span>

[Color](class_color.md#class_Color) **font_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_linkbutton.md#class_LinkButton_theme_color_font_pressed_color)

Text [Color](class_color.md#class_Color) used when the **LinkButton** is being pressed.

---

<span id="class_LinkButton_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_linkbutton.md#class_LinkButton_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_linkbutton.md#class_LinkButton_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_LinkButton_theme_constant_underline_spacing"></span>

[int](class_int.md#class_int) **underline_spacing** = `2` [🔗](class_linkbutton.md#class_LinkButton_theme_constant_underline_spacing)

The vertical space between the baseline of text and the underline.

---

<span id="class_LinkButton_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_linkbutton.md#class_LinkButton_theme_font_font)

[Font](class_font.md#class_Font) of the **LinkButton**'s text.

---

<span id="class_LinkButton_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_linkbutton.md#class_LinkButton_theme_font_size_font_size)

Font size of the **LinkButton**'s text.

---

<span id="class_LinkButton_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_linkbutton.md#class_LinkButton_theme_style_focus)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **LinkButton** is focused. The [focus](class_linkbutton.md#class_LinkButton_theme_style_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox), so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.
