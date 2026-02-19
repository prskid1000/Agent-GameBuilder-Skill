.. meta::
	:keywords: expandable, collapsible, collapse, accordion, details

<span id="class_FoldableContainer"></span>

## FoldableContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A container that can be expanded/collapsed.

### Description

A container that can be expanded/collapsed, with a title that can be filled with controls, such as buttons. This is also called an accordion.

The title can be positioned at the top or bottom of the container. The container can be expanded or collapsed by clicking the title or by pressing `ui_accept` when focused. Child control nodes are hidden when the container is collapsed. Ignores non-control children.

A FoldableContainer can be grouped with other FoldableContainers so that only one of them can be opened at a time; see [foldable_group](class_foldablecontainer.md#class_FoldableContainer_property_foldable_group) and [FoldableGroup](class_foldablegroup.md#class_FoldableGroup).

### Properties


| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| --- | --- | --- |
| [FoldableGroup](class_foldablegroup.md#class_FoldableGroup) | [foldable_group](class_foldablecontainer.md#class_FoldableContainer_property_foldable_group) |
| [bool](class_bool.md#class_bool) | [folded](class_foldablecontainer.md#class_FoldableContainer_property_folded) | `false` |
| [String](class_string.md#class_String) | [language](class_foldablecontainer.md#class_FoldableContainer_property_language) | `""` |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | mouse_filter | `0` (overrides [Control](class_control.md#class_Control_property_mouse_filter)) |
| [String](class_string.md#class_String) | [title](class_foldablecontainer.md#class_FoldableContainer_property_title) | `""` |
| HorizontalAlignment | [title_alignment](class_foldablecontainer.md#class_FoldableContainer_property_title_alignment) | `0` |
| [TitlePosition](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition) | [title_position](class_foldablecontainer.md#class_FoldableContainer_property_title_position) | `0` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [title_text_direction](class_foldablecontainer.md#class_FoldableContainer_property_title_text_direction) | `0` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [title_text_overrun_behavior](class_foldablecontainer.md#class_FoldableContainer_property_title_text_overrun_behavior) | `0` |

### Methods


| void | [add_title_bar_control](class_foldablecontainer.md#class_FoldableContainer_method_add_title_bar_control) ( control: [Control](class_control.md#class_Control) ) |
| --- | --- |
| void | [expand](class_foldablecontainer.md#class_FoldableContainer_method_expand) ( ) |
| void | [fold](class_foldablecontainer.md#class_FoldableContainer_method_fold) ( ) |
| void | [remove_title_bar_control](class_foldablecontainer.md#class_FoldableContainer_method_remove_title_bar_control) ( control: [Control](class_control.md#class_Control) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [collapsed_font_color](class_foldablecontainer.md#class_FoldableContainer_theme_color_collapsed_font_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_color](class_foldablecontainer.md#class_FoldableContainer_theme_color_font_color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_foldablecontainer.md#class_FoldableContainer_theme_color_font_outline_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [hover_font_color](class_foldablecontainer.md#class_FoldableContainer_theme_color_hover_font_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [int](class_int.md#class_int) | [h_separation](class_foldablecontainer.md#class_FoldableContainer_theme_constant_h_separation) | `2` |
| [int](class_int.md#class_int) | [outline_size](class_foldablecontainer.md#class_FoldableContainer_theme_constant_outline_size) | `0` |
| [Font](class_font.md#class_Font) | [font](class_foldablecontainer.md#class_FoldableContainer_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_foldablecontainer.md#class_FoldableContainer_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [expanded_arrow](class_foldablecontainer.md#class_FoldableContainer_theme_icon_expanded_arrow) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [expanded_arrow_mirrored](class_foldablecontainer.md#class_FoldableContainer_theme_icon_expanded_arrow_mirrored) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folded_arrow](class_foldablecontainer.md#class_FoldableContainer_theme_icon_folded_arrow) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folded_arrow_mirrored](class_foldablecontainer.md#class_FoldableContainer_theme_icon_folded_arrow_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_foldablecontainer.md#class_FoldableContainer_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel](class_foldablecontainer.md#class_FoldableContainer_theme_style_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [title_collapsed_hover_panel](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_collapsed_hover_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [title_collapsed_panel](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_collapsed_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [title_hover_panel](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_hover_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [title_panel](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_panel) |

---

### Signals

<span id="class_FoldableContainer_signal_folding_changed"></span>

**folding_changed** ( is_folded: [bool](class_bool.md#class_bool) ) [🔗](class_foldablecontainer.md#class_FoldableContainer_signal_folding_changed)

Emitted when the container is folded/expanded.

---

### Enumerations

<span id="enum_FoldableContainer_TitlePosition"></span>

enum **TitlePosition**: [🔗](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition)

<span id="class_FoldableContainer_constant_POSITION_TOP"></span>

[TitlePosition](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition) **POSITION_TOP** = `0`

Makes the title appear at the top of the container.

<span id="class_FoldableContainer_constant_POSITION_BOTTOM"></span>

[TitlePosition](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition) **POSITION_BOTTOM** = `1`

Makes the title appear at the bottom of the container. Also makes all StyleBoxes flipped vertically.

---

### Property Descriptions

<span id="class_FoldableContainer_property_foldable_group"></span>

[FoldableGroup](class_foldablegroup.md#class_FoldableGroup) **foldable_group** [🔗](class_foldablecontainer.md#class_FoldableContainer_property_foldable_group)

- void **set_foldable_group** ( value: [FoldableGroup](class_foldablegroup.md#class_FoldableGroup) )
- [FoldableGroup](class_foldablegroup.md#class_FoldableGroup) **get_foldable_group** ( )

The [FoldableGroup](class_foldablegroup.md#class_FoldableGroup) associated with the container. When multiple **FoldableContainer** nodes share the same group, only one of them is allowed to be unfolded.

---

<span id="class_FoldableContainer_property_folded"></span>

[bool](class_bool.md#class_bool) **folded** = `false` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_folded)

- void **set_folded** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_folded** ( )

If `true`, the container will becomes folded and will hide all its children.

---

<span id="class_FoldableContainer_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_FoldableContainer_property_title"></span>

[String](class_string.md#class_String) **title** = `""` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_title)

- void **set_title** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_title** ( )

The container's title text.

---

<span id="class_FoldableContainer_property_title_alignment"></span>

HorizontalAlignment **title_alignment** = `0` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_title_alignment)

- void **set_title_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_title_alignment** ( )

Title's horizontal text alignment.

---

<span id="class_FoldableContainer_property_title_position"></span>

[TitlePosition](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition) **title_position** = `0` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_title_position)

- void **set_title_position** ( value: [TitlePosition](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition) )
- [TitlePosition](class_foldablecontainer.md#enum_FoldableContainer_TitlePosition) **get_title_position** ( )

Title's position.

---

<span id="class_FoldableContainer_property_title_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **title_text_direction** = `0` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_title_text_direction)

- void **set_title_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_title_text_direction** ( )

Title text writing direction.

---

<span id="class_FoldableContainer_property_title_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **title_text_overrun_behavior** = `0` [🔗](class_foldablecontainer.md#class_FoldableContainer_property_title_text_overrun_behavior)

- void **set_title_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_title_text_overrun_behavior** ( )

Defines the behavior of the title when the text is longer than the available space.

---

### Method Descriptions

<span id="class_FoldableContainer_method_add_title_bar_control"></span>

void **add_title_bar_control** ( control: [Control](class_control.md#class_Control) ) [🔗](class_foldablecontainer.md#class_FoldableContainer_method_add_title_bar_control)

Adds a [Control](class_control.md#class_Control) that will be placed next to the container's title, obscuring the clickable area. Prime usage is adding [Button](class_button.md#class_Button) nodes, but it can be any [Control](class_control.md#class_Control).

The control will be added as a child of this container and removed from previous parent if necessary. The controls will be placed aligned to the right, with the first added control being the leftmost one.

---

<span id="class_FoldableContainer_method_expand"></span>

void **expand** ( ) [🔗](class_foldablecontainer.md#class_FoldableContainer_method_expand)

Expands the container and emits [folding_changed](class_foldablecontainer.md#class_FoldableContainer_signal_folding_changed).

---

<span id="class_FoldableContainer_method_fold"></span>

void **fold** ( ) [🔗](class_foldablecontainer.md#class_FoldableContainer_method_fold)

Folds the container and emits [folding_changed](class_foldablecontainer.md#class_FoldableContainer_signal_folding_changed).

---

<span id="class_FoldableContainer_method_remove_title_bar_control"></span>

void **remove_title_bar_control** ( control: [Control](class_control.md#class_Control) ) [🔗](class_foldablecontainer.md#class_FoldableContainer_method_remove_title_bar_control)

Removes a [Control](class_control.md#class_Control) added with [add_title_bar_control()](class_foldablecontainer.md#class_FoldableContainer_method_add_title_bar_control). The node is not freed automatically, you need to use [Node.queue_free()](class_node.md#class_Node_method_queue_free).

---

### Theme Property Descriptions

<span id="class_FoldableContainer_theme_color_collapsed_font_color"></span>

[Color](class_color.md#class_Color) **collapsed_font_color** = `Color(1, 1, 1, 1)` [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_color_collapsed_font_color)

The title's font color when collapsed.

---

<span id="class_FoldableContainer_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_color_font_color)

The title's font color when expanded.

---

<span id="class_FoldableContainer_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(1, 1, 1, 1)` [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_color_font_outline_color)

The title's font outline color.

---

<span id="class_FoldableContainer_theme_color_hover_font_color"></span>

[Color](class_color.md#class_Color) **hover_font_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_color_hover_font_color)

The title's font hover color.

---

<span id="class_FoldableContainer_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `2` [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_constant_h_separation)

The horizontal separation between the title's icon and text, and between title bar controls.

---

<span id="class_FoldableContainer_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_constant_outline_size)

The title's font outline size.

---

<span id="class_FoldableContainer_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_font_font)

The title's font.

---

<span id="class_FoldableContainer_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_font_size_font_size)

The title's font size.

---

<span id="class_FoldableContainer_theme_icon_expanded_arrow"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **expanded_arrow** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_icon_expanded_arrow)

The title's icon used when expanded.

---

<span id="class_FoldableContainer_theme_icon_expanded_arrow_mirrored"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **expanded_arrow_mirrored** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_icon_expanded_arrow_mirrored)

The title's icon used when expanded (for bottom title).

---

<span id="class_FoldableContainer_theme_icon_folded_arrow"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folded_arrow** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_icon_folded_arrow)

The title's icon used when folded (for left-to-right layouts).

---

<span id="class_FoldableContainer_theme_icon_folded_arrow_mirrored"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folded_arrow_mirrored** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_icon_folded_arrow_mirrored)

The title's icon used when collapsed (for right-to-left layouts).

---

<span id="class_FoldableContainer_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_style_focus)

Background used when **FoldableContainer** has GUI focus. The [focus](class_foldablecontainer.md#class_FoldableContainer_theme_style_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox), so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_FoldableContainer_theme_style_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_style_panel)

Default background for the **FoldableContainer**.

---

<span id="class_FoldableContainer_theme_style_title_collapsed_hover_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **title_collapsed_hover_panel** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_collapsed_hover_panel)

Background used when the mouse cursor enters the title's area when collapsed.

---

<span id="class_FoldableContainer_theme_style_title_collapsed_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **title_collapsed_panel** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_collapsed_panel)

Default background for the **FoldableContainer**'s title when collapsed.

---

<span id="class_FoldableContainer_theme_style_title_hover_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **title_hover_panel** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_hover_panel)

Background used when the mouse cursor enters the title's area when expanded.

---

<span id="class_FoldableContainer_theme_style_title_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **title_panel** [🔗](class_foldablecontainer.md#class_FoldableContainer_theme_style_title_panel)

Default background for the **FoldableContainer**'s title when expanded.
