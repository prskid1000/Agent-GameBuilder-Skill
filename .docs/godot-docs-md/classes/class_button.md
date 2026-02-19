<span id="class_Button"></span>

## Button

**Inherits:** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CheckBox](class_checkbox.md#class_CheckBox), [CheckButton](class_checkbutton.md#class_CheckButton), [ColorPickerButton](class_colorpickerbutton.md#class_ColorPickerButton), [MenuButton](class_menubutton.md#class_MenuButton), [OptionButton](class_optionbutton.md#class_OptionButton)

A themed button that can contain text and an icon.

### Description

**Button** is the standard themed button. It can contain text and an icon, and it will display them according to the current [Theme](class_theme.md#class_Theme).

 **Example:** Create a button and connect a method that will be called when the button is pressed:

.. tabs::

```
```

    func _ready():
        var button = Button.new()
        button.text = "Click me"
        button.pressed.connect(_button_pressed)
        add_child(button)

    func _button_pressed():
        print("Hello world!")

```
```

    public override void _Ready()
    {
        var button = new Button();
        button.Text = "Click me";
        button.Pressed += ButtonPressed;
        AddChild(button);
    }

    private void ButtonPressed()
    {
        GD.Print("Hello world!");
    }

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

 **Note:** Buttons do not detect touch input and therefore don't support multitouch, since mouse emulation can only press one button at a given time. Use [TouchScreenButton](class_touchscreenbutton.md#class_TouchScreenButton) for buttons that trigger gameplay movement or actions.

### Tutorials

- 2D Dodge The Creeps Demo

- Operating System Testing Demo

### Properties


| HorizontalAlignment | [alignment](class_button.md#class_Button_property_alignment) | `1` |
| --- | --- | --- |
| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [autowrap_mode](class_button.md#class_Button_property_autowrap_mode) | `0` |
| bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] | [autowrap_trim_flags](class_button.md#class_Button_property_autowrap_trim_flags) | `128` |
| [bool](class_bool.md#class_bool) | [clip_text](class_button.md#class_Button_property_clip_text) | `false` |
| [bool](class_bool.md#class_bool) | [expand_icon](class_button.md#class_Button_property_expand_icon) | `false` |
| [bool](class_bool.md#class_bool) | [flat](class_button.md#class_Button_property_flat) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [icon](class_button.md#class_Button_property_icon) |
| HorizontalAlignment | [icon_alignment](class_button.md#class_Button_property_icon_alignment) | `0` |
| [String](class_string.md#class_String) | [language](class_button.md#class_Button_property_language) | `""` |
| [String](class_string.md#class_String) | [text](class_button.md#class_Button_property_text) | `""` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_button.md#class_Button_property_text_direction) | `0` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [text_overrun_behavior](class_button.md#class_Button_property_text_overrun_behavior) | `0` |
| VerticalAlignment | [vertical_icon_alignment](class_button.md#class_Button_property_vertical_icon_alignment) | `1` |

### Theme Properties


| [Color](class_color.md#class_Color) | [font_color](class_button.md#class_Button_theme_color_font_color) | `Color(0.875, 0.875, 0.875, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_disabled_color](class_button.md#class_Button_theme_color_font_disabled_color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class_Color) | [font_focus_color](class_button.md#class_Button_theme_color_font_focus_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hover_color](class_button.md#class_Button_theme_color_font_hover_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hover_pressed_color](class_button.md#class_Button_theme_color_font_hover_pressed_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_button.md#class_Button_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_pressed_color](class_button.md#class_Button_theme_color_font_pressed_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_disabled_color](class_button.md#class_Button_theme_color_icon_disabled_color) | `Color(1, 1, 1, 0.4)` |
| [Color](class_color.md#class_Color) | [icon_focus_color](class_button.md#class_Button_theme_color_icon_focus_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_hover_color](class_button.md#class_Button_theme_color_icon_hover_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_hover_pressed_color](class_button.md#class_Button_theme_color_icon_hover_pressed_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_normal_color](class_button.md#class_Button_theme_color_icon_normal_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_pressed_color](class_button.md#class_Button_theme_color_icon_pressed_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [align_to_largest_stylebox](class_button.md#class_Button_theme_constant_align_to_largest_stylebox) | `0` |
| [int](class_int.md#class_int) | [h_separation](class_button.md#class_Button_theme_constant_h_separation) | `4` |
| [int](class_int.md#class_int) | [icon_max_width](class_button.md#class_Button_theme_constant_icon_max_width) | `0` |
| [int](class_int.md#class_int) | [line_spacing](class_button.md#class_Button_theme_constant_line_spacing) | `0` |
| [int](class_int.md#class_int) | [outline_size](class_button.md#class_Button_theme_constant_outline_size) | `0` |
| [Font](class_font.md#class_Font) | [font](class_button.md#class_Button_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_button.md#class_Button_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [icon](class_button.md#class_Button_theme_icon_icon) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [disabled](class_button.md#class_Button_theme_style_disabled) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [disabled_mirrored](class_button.md#class_Button_theme_style_disabled_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_button.md#class_Button_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover](class_button.md#class_Button_theme_style_hover) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover_mirrored](class_button.md#class_Button_theme_style_hover_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover_pressed](class_button.md#class_Button_theme_style_hover_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover_pressed_mirrored](class_button.md#class_Button_theme_style_hover_pressed_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal](class_button.md#class_Button_theme_style_normal) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal_mirrored](class_button.md#class_Button_theme_style_normal_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [pressed](class_button.md#class_Button_theme_style_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [pressed_mirrored](class_button.md#class_Button_theme_style_pressed_mirrored) |

---

### Property Descriptions

<span id="class_Button_property_alignment"></span>

HorizontalAlignment **alignment** = `1` [🔗](class_button.md#class_Button_property_alignment)

- void **set_text_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_text_alignment** ( )

Text alignment policy for the button's text.

---

<span id="class_Button_property_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **autowrap_mode** = `0` [🔗](class_button.md#class_Button_property_autowrap_mode)

- void **set_autowrap_mode** ( value: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) )
- [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( )

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF), the text gets wrapped inside the node's bounding rectangle.

---

<span id="class_Button_property_autowrap_trim_flags"></span>

*BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **autowrap_trim_flags** = `128` [🔗](class_button.md#class_Button_property_autowrap_trim_flags)

- void **set_autowrap_trim_flags** ( value: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] )
- *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **get_autowrap_trim_flags** ( )

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES) for more info.

---

<span id="class_Button_property_clip_text"></span>

[bool](class_bool.md#class_bool) **clip_text** = `false` [🔗](class_button.md#class_Button_property_clip_text)

- void **set_clip_text** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_clip_text** ( )

If `true`, text that is too large to fit the button is clipped horizontally. If `false`, the button will always be wide enough to hold the text. The text is not vertically clipped, and the button's height is not affected by this property.

---

<span id="class_Button_property_expand_icon"></span>

[bool](class_bool.md#class_bool) **expand_icon** = `false` [🔗](class_button.md#class_Button_property_expand_icon)

- void **set_expand_icon** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_expand_icon** ( )

When enabled, the button's icon will expand/shrink to fit the button's size while keeping its aspect. See also [icon_max_width](class_button.md#class_Button_theme_constant_icon_max_width).

---

<span id="class_Button_property_flat"></span>

[bool](class_bool.md#class_bool) **flat** = `false` [🔗](class_button.md#class_Button_property_flat)

- void **set_flat** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flat** ( )

Flat buttons don't display decoration.

---

<span id="class_Button_property_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **icon** [🔗](class_button.md#class_Button_property_icon)

- void **set_button_icon** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_button_icon** ( )

Button's icon, if text is present the icon will be placed before the text.

To edit margin and spacing of the icon, use [h_separation](class_button.md#class_Button_theme_constant_h_separation) theme property and `content_margin_*` properties of the used [StyleBox](class_stylebox.md#class_StyleBox) es.

---

<span id="class_Button_property_icon_alignment"></span>

HorizontalAlignment **icon_alignment** = `0` [🔗](class_button.md#class_Button_property_icon_alignment)

- void **set_icon_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_icon_alignment** ( )

Specifies if the icon should be aligned horizontally to the left, right, or center of a button. Uses the same HorizontalAlignment constants as the text alignment. If centered horizontally and vertically, text will draw on top of the icon.

---

<span id="class_Button_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_button.md#class_Button_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_Button_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_button.md#class_Button_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The button's text that will be displayed inside the button's area.

---

<span id="class_Button_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_button.md#class_Button_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_Button_property_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **text_overrun_behavior** = `0` [🔗](class_button.md#class_Button_property_text_overrun_behavior)

- void **set_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( )

Sets the clipping behavior when the text exceeds the node's bounding rectangle.

---

<span id="class_Button_property_vertical_icon_alignment"></span>

VerticalAlignment **vertical_icon_alignment** = `1` [🔗](class_button.md#class_Button_property_vertical_icon_alignment)

- void **set_vertical_icon_alignment** ( value: VerticalAlignment )
- VerticalAlignment **get_vertical_icon_alignment** ( )

Specifies if the icon should be aligned vertically to the top, bottom, or center of a button. Uses the same VerticalAlignment constants as the text alignment. If centered horizontally and vertically, text will draw on top of the icon.

---

### Theme Property Descriptions

<span id="class_Button_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_button.md#class_Button_theme_color_font_color)

Default text [Color](class_color.md#class_Color) of the **Button**.

---

<span id="class_Button_theme_color_font_disabled_color"></span>

[Color](class_color.md#class_Color) **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_button.md#class_Button_theme_color_font_disabled_color)

Text [Color](class_color.md#class_Color) used when the **Button** is disabled.

---

<span id="class_Button_theme_color_font_focus_color"></span>

[Color](class_color.md#class_Color) **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_button.md#class_Button_theme_color_font_focus_color)

Text [Color](class_color.md#class_Color) used when the **Button** is focused. Only replaces the normal text color of the button. Disabled, hovered, and pressed states take precedence over this color.

---

<span id="class_Button_theme_color_font_hover_color"></span>

[Color](class_color.md#class_Color) **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_button.md#class_Button_theme_color_font_hover_color)

Text [Color](class_color.md#class_Color) used when the **Button** is being hovered.

---

<span id="class_Button_theme_color_font_hover_pressed_color"></span>

[Color](class_color.md#class_Color) **font_hover_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_font_hover_pressed_color)

Text [Color](class_color.md#class_Color) used when the **Button** is being hovered and pressed.

---

<span id="class_Button_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_button.md#class_Button_theme_color_font_outline_color)

The tint of text outline of the **Button**.

---

<span id="class_Button_theme_color_font_pressed_color"></span>

[Color](class_color.md#class_Color) **font_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_font_pressed_color)

Text [Color](class_color.md#class_Color) used when the **Button** is being pressed.

---

<span id="class_Button_theme_color_icon_disabled_color"></span>

[Color](class_color.md#class_Color) **icon_disabled_color** = `Color(1, 1, 1, 0.4)` [🔗](class_button.md#class_Button_theme_color_icon_disabled_color)

Icon modulate [Color](class_color.md#class_Color) used when the **Button** is disabled.

---

<span id="class_Button_theme_color_icon_focus_color"></span>

[Color](class_color.md#class_Color) **icon_focus_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_icon_focus_color)

Icon modulate [Color](class_color.md#class_Color) used when the **Button** is focused. Only replaces the normal modulate color of the button. Disabled, hovered, and pressed states take precedence over this color.

---

<span id="class_Button_theme_color_icon_hover_color"></span>

[Color](class_color.md#class_Color) **icon_hover_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_icon_hover_color)

Icon modulate [Color](class_color.md#class_Color) used when the **Button** is being hovered.

---

<span id="class_Button_theme_color_icon_hover_pressed_color"></span>

[Color](class_color.md#class_Color) **icon_hover_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_icon_hover_pressed_color)

Icon modulate [Color](class_color.md#class_Color) used when the **Button** is being hovered and pressed.

---

<span id="class_Button_theme_color_icon_normal_color"></span>

[Color](class_color.md#class_Color) **icon_normal_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_icon_normal_color)

Default icon modulate [Color](class_color.md#class_Color) of the **Button**.

---

<span id="class_Button_theme_color_icon_pressed_color"></span>

[Color](class_color.md#class_Color) **icon_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_button.md#class_Button_theme_color_icon_pressed_color)

Icon modulate [Color](class_color.md#class_Color) used when the **Button** is being pressed.

---

<span id="class_Button_theme_constant_align_to_largest_stylebox"></span>

[int](class_int.md#class_int) **align_to_largest_stylebox** = `0` [🔗](class_button.md#class_Button_theme_constant_align_to_largest_stylebox)

This constant acts as a boolean. If `true`, the minimum size of the button and text/icon alignment is always based on the largest stylebox margins, otherwise it's based on the current button state stylebox margins.

---

<span id="class_Button_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `4` [🔗](class_button.md#class_Button_theme_constant_h_separation)

The horizontal space between **Button**'s icon and text. Negative values will be treated as `0` when used.

---

<span id="class_Button_theme_constant_icon_max_width"></span>

[int](class_int.md#class_int) **icon_max_width** = `0` [🔗](class_button.md#class_Button_theme_constant_icon_max_width)

The maximum allowed width of the **Button**'s icon. This limit is applied on top of the default size of the icon, or its expanded size if [expand_icon](class_button.md#class_Button_property_expand_icon) is `true`. The height is adjusted according to the icon's ratio. If the button has additional icons (e.g. [CheckBox](class_checkbox.md#class_CheckBox)), they will also be limited.

---

<span id="class_Button_theme_constant_line_spacing"></span>

[int](class_int.md#class_int) **line_spacing** = `0` [🔗](class_button.md#class_Button_theme_constant_line_spacing)

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_Button_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_button.md#class_Button_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_button.md#class_Button_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_Button_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_button.md#class_Button_theme_font_font)

[Font](class_font.md#class_Font) of the **Button**'s text.

---

<span id="class_Button_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_button.md#class_Button_theme_font_size_font_size)

Font size of the **Button**'s text.

---

<span id="class_Button_theme_icon_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **icon** [🔗](class_button.md#class_Button_theme_icon_icon)

Default icon for the **Button**. Appears only if [icon](class_button.md#class_Button_property_icon) is not assigned.

---

<span id="class_Button_theme_style_disabled"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **disabled** [🔗](class_button.md#class_Button_theme_style_disabled)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is disabled.

---

<span id="class_Button_theme_style_disabled_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **disabled_mirrored** [🔗](class_button.md#class_Button_theme_style_disabled_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is disabled (for right-to-left layouts).

---

<span id="class_Button_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_button.md#class_Button_theme_style_focus)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is focused. The [focus](class_button.md#class_Button_theme_style_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox), so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_Button_theme_style_hover"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover** [🔗](class_button.md#class_Button_theme_style_hover)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is being hovered.

---

<span id="class_Button_theme_style_hover_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover_mirrored** [🔗](class_button.md#class_Button_theme_style_hover_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is being hovered (for right-to-left layouts).

---

<span id="class_Button_theme_style_hover_pressed"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover_pressed** [🔗](class_button.md#class_Button_theme_style_hover_pressed)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is being pressed and hovered at the same time.

---

<span id="class_Button_theme_style_hover_pressed_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover_pressed_mirrored** [🔗](class_button.md#class_Button_theme_style_hover_pressed_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is being pressed and hovered at the same time (for right-to-left layouts).

---

<span id="class_Button_theme_style_normal"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal** [🔗](class_button.md#class_Button_theme_style_normal)

Default [StyleBox](class_stylebox.md#class_StyleBox) for the **Button**.

---

<span id="class_Button_theme_style_normal_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal_mirrored** [🔗](class_button.md#class_Button_theme_style_normal_mirrored)

Default [StyleBox](class_stylebox.md#class_StyleBox) for the **Button** (for right-to-left layouts).

---

<span id="class_Button_theme_style_pressed"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **pressed** [🔗](class_button.md#class_Button_theme_style_pressed)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is being pressed.

---

<span id="class_Button_theme_style_pressed_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **pressed_mirrored** [🔗](class_button.md#class_Button_theme_style_pressed_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **Button** is being pressed (for right-to-left layouts).
