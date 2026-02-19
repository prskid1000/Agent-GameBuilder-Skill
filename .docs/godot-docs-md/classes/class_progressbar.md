<span id="class_ProgressBar"></span>

## ProgressBar

**Inherits:** [Range](class_range.md#class_Range) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control used for visual representation of a percentage.

### Description

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, use [TextureProgressBar](class_textureprogressbar.md#class_TextureProgressBar) instead.

### Properties


| [bool](class_bool.md#class_bool) | [editor_preview_indeterminate](class_progressbar.md#class_ProgressBar_property_editor_preview_indeterminate) |
| --- | --- |
| [int](class_int.md#class_int) | [fill_mode](class_progressbar.md#class_ProgressBar_property_fill_mode) | `0` |
| [bool](class_bool.md#class_bool) | [indeterminate](class_progressbar.md#class_ProgressBar_property_indeterminate) | `false` |
| [bool](class_bool.md#class_bool) | [show_percentage](class_progressbar.md#class_ProgressBar_property_show_percentage) | `true` |

### Theme Properties


| [Color](class_color.md#class_Color) | [font_color](class_progressbar.md#class_ProgressBar_theme_color_font_color) | `Color(0.95, 0.95, 0.95, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_outline_color](class_progressbar.md#class_ProgressBar_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class_int) | [outline_size](class_progressbar.md#class_ProgressBar_theme_constant_outline_size) | `0` |
| [Font](class_font.md#class_Font) | [font](class_progressbar.md#class_ProgressBar_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_progressbar.md#class_ProgressBar_theme_font_size_font_size) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [background](class_progressbar.md#class_ProgressBar_theme_style_background) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [fill](class_progressbar.md#class_ProgressBar_theme_style_fill) |

---

### Enumerations

<span id="enum_ProgressBar_FillMode"></span>

enum **FillMode**: [🔗](class_progressbar.md#enum_ProgressBar_FillMode)

<span id="class_ProgressBar_constant_FILL_BEGIN_TO_END"></span>

[FillMode](class_progressbar.md#enum_ProgressBar_FillMode) **FILL_BEGIN_TO_END** = `0`

The progress bar fills from begin to end horizontally, according to the language direction. If [Control.is_layout_rtl()](class_control.md#class_Control_method_is_layout_rtl) returns `false`, it fills from left to right, and if it returns `true`, it fills from right to left.

<span id="class_ProgressBar_constant_FILL_END_TO_BEGIN"></span>

[FillMode](class_progressbar.md#enum_ProgressBar_FillMode) **FILL_END_TO_BEGIN** = `1`

The progress bar fills from end to begin horizontally, according to the language direction. If [Control.is_layout_rtl()](class_control.md#class_Control_method_is_layout_rtl) returns `false`, it fills from right to left, and if it returns `true`, it fills from left to right.

<span id="class_ProgressBar_constant_FILL_TOP_TO_BOTTOM"></span>

[FillMode](class_progressbar.md#enum_ProgressBar_FillMode) **FILL_TOP_TO_BOTTOM** = `2`

The progress fills from top to bottom.

<span id="class_ProgressBar_constant_FILL_BOTTOM_TO_TOP"></span>

[FillMode](class_progressbar.md#enum_ProgressBar_FillMode) **FILL_BOTTOM_TO_TOP** = `3`

The progress fills from bottom to top.

---

### Property Descriptions

<span id="class_ProgressBar_property_editor_preview_indeterminate"></span>

[bool](class_bool.md#class_bool) **editor_preview_indeterminate** [🔗](class_progressbar.md#class_ProgressBar_property_editor_preview_indeterminate)

- void **set_editor_preview_indeterminate** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editor_preview_indeterminate_enabled** ( )

If `false`, the [indeterminate](class_progressbar.md#class_ProgressBar_property_indeterminate) animation will be paused in the editor.

---

<span id="class_ProgressBar_property_fill_mode"></span>

[int](class_int.md#class_int) **fill_mode** = `0` [🔗](class_progressbar.md#class_ProgressBar_property_fill_mode)

- void **set_fill_mode** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fill_mode** ( )

The fill direction. See [FillMode](class_progressbar.md#enum_ProgressBar_FillMode) for possible values.

---

<span id="class_ProgressBar_property_indeterminate"></span>

[bool](class_bool.md#class_bool) **indeterminate** = `false` [🔗](class_progressbar.md#class_ProgressBar_property_indeterminate)

- void **set_indeterminate** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_indeterminate** ( )

When set to `true`, the progress bar indicates that something is happening with an animation, but does not show the fill percentage or value.

---

<span id="class_ProgressBar_property_show_percentage"></span>

[bool](class_bool.md#class_bool) **show_percentage** = `true` [🔗](class_progressbar.md#class_ProgressBar_property_show_percentage)

- void **set_show_percentage** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_percentage_shown** ( )

If `true`, the fill percentage is displayed on the bar.

---

### Theme Property Descriptions

<span id="class_ProgressBar_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_progressbar.md#class_ProgressBar_theme_color_font_color)

The color of the text.

---

<span id="class_ProgressBar_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_progressbar.md#class_ProgressBar_theme_color_font_outline_color)

The tint of text outline of the **ProgressBar**.

---

<span id="class_ProgressBar_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_progressbar.md#class_ProgressBar_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_progressbar.md#class_ProgressBar_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_ProgressBar_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_progressbar.md#class_ProgressBar_theme_font_font)

Font used to draw the fill percentage if [show_percentage](class_progressbar.md#class_ProgressBar_property_show_percentage) is `true`.

---

<span id="class_ProgressBar_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_progressbar.md#class_ProgressBar_theme_font_size_font_size)

Font size used to draw the fill percentage if [show_percentage](class_progressbar.md#class_ProgressBar_property_show_percentage) is `true`.

---

<span id="class_ProgressBar_theme_style_background"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **background** [🔗](class_progressbar.md#class_ProgressBar_theme_style_background)

The style of the background.

---

<span id="class_ProgressBar_theme_style_fill"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **fill** [🔗](class_progressbar.md#class_ProgressBar_theme_style_fill)

The style of the progress (i.e. the part that fills the bar).
