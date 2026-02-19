<span id="class_MenuBar"></span>

## MenuBar

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A horizontal menu bar that creates a menu for each [PopupMenu](class_popupmenu.md#class_PopupMenu) child.

### Description

A horizontal menu bar that creates a menu for each [PopupMenu](class_popupmenu.md#class_PopupMenu) child. New items are created by adding [PopupMenu](class_popupmenu.md#class_PopupMenu) s to this node. Item title is determined by [Window.title](class_window.md#class_Window_property_title), or node name if [Window.title](class_window.md#class_Window_property_title) is empty. Item title can be overridden using [set_menu_title()](class_menubar.md#class_MenuBar_method_set_menu_title).

### Properties


| [bool](class_bool.md#class_bool) | [flat](class_menubar.md#class_MenuBar_property_flat) | `false` |
| --- | --- | --- |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `3` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [String](class_string.md#class_String) | [language](class_menubar.md#class_MenuBar_property_language) | `""` |
| [bool](class_bool.md#class_bool) | [prefer_global_menu](class_menubar.md#class_MenuBar_property_prefer_global_menu) | `true` |
| [int](class_int.md#class_int) | [start_index](class_menubar.md#class_MenuBar_property_start_index) | `-1` |
| [bool](class_bool.md#class_bool) | [switch_on_hover](class_menubar.md#class_MenuBar_property_switch_on_hover) | `true` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_menubar.md#class_MenuBar_property_text_direction) | `0` |

### Methods


| [int](class_int.md#class_int) | [get_menu_count](class_menubar.md#class_MenuBar_method_get_menu_count) ( ) const |
| --- | --- |
| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_menu_popup](class_menubar.md#class_MenuBar_method_get_menu_popup) ( menu: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_menu_title](class_menubar.md#class_MenuBar_method_get_menu_title) ( menu: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_menu_tooltip](class_menubar.md#class_MenuBar_method_get_menu_tooltip) ( menu: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_menu_disabled](class_menubar.md#class_MenuBar_method_is_menu_disabled) ( menu: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_menu_hidden](class_menubar.md#class_MenuBar_method_is_menu_hidden) ( menu: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_native_menu](class_menubar.md#class_MenuBar_method_is_native_menu) ( ) const |
| void | [set_disable_shortcuts](class_menubar.md#class_MenuBar_method_set_disable_shortcuts) ( disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_menu_disabled](class_menubar.md#class_MenuBar_method_set_menu_disabled) ( menu: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_menu_hidden](class_menubar.md#class_MenuBar_method_set_menu_hidden) ( menu: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) |
| void | [set_menu_title](class_menubar.md#class_MenuBar_method_set_menu_title) ( menu: [int](class_int.md#class_int), title: [String](class_string.md#class_String) ) |
| void | [set_menu_tooltip](class_menubar.md#class_MenuBar_method_set_menu_tooltip) ( menu: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [font_color](class_menubar.md#class_MenuBar_theme_color_font_color) | `Color(0.875, 0.875, 0.875, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_disabled_color](class_menubar.md#class_MenuBar_theme_color_font_disabled_color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class_Color) | [font_focus_color](class_menubar.md#class_MenuBar_theme_color_font_focus_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hover_color](class_menubar.md#class_MenuBar_theme_color_font_hover_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hover_pressed_color](class_menubar.md#class_MenuBar_theme_color_font_hover_pressed_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_menubar.md#class_MenuBar_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_pressed_color](class_menubar.md#class_MenuBar_theme_color_font_pressed_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [h_separation](class_menubar.md#class_MenuBar_theme_constant_h_separation) | `4` |
| [int](class_int.md#class_int) | [outline_size](class_menubar.md#class_MenuBar_theme_constant_outline_size) | `0` |
| [Font](class_font.md#class_Font) | [font](class_menubar.md#class_MenuBar_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_menubar.md#class_MenuBar_theme_font_size_font_size) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [disabled](class_menubar.md#class_MenuBar_theme_style_disabled) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [disabled_mirrored](class_menubar.md#class_MenuBar_theme_style_disabled_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover](class_menubar.md#class_MenuBar_theme_style_hover) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover_mirrored](class_menubar.md#class_MenuBar_theme_style_hover_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover_pressed](class_menubar.md#class_MenuBar_theme_style_hover_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hover_pressed_mirrored](class_menubar.md#class_MenuBar_theme_style_hover_pressed_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal](class_menubar.md#class_MenuBar_theme_style_normal) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal_mirrored](class_menubar.md#class_MenuBar_theme_style_normal_mirrored) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [pressed](class_menubar.md#class_MenuBar_theme_style_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [pressed_mirrored](class_menubar.md#class_MenuBar_theme_style_pressed_mirrored) |

---

### Property Descriptions

<span id="class_MenuBar_property_flat"></span>

[bool](class_bool.md#class_bool) **flat** = `false` [🔗](class_menubar.md#class_MenuBar_property_flat)

- void **set_flat** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flat** ( )

Flat **MenuBar** don't display item decoration.

---

<span id="class_MenuBar_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_menubar.md#class_MenuBar_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_MenuBar_property_prefer_global_menu"></span>

[bool](class_bool.md#class_bool) **prefer_global_menu** = `true` [🔗](class_menubar.md#class_MenuBar_property_prefer_global_menu)

- void **set_prefer_global_menu** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_prefer_global_menu** ( )

If `true`, **MenuBar** will use system global menu when supported.

 **Note:** If `true` and global menu is supported, this node is not displayed, has zero size, and all its child nodes except [PopupMenu](class_popupmenu.md#class_PopupMenu) s are inaccessible.

 **Note:** This property overrides the value of the [PopupMenu.prefer_native_menu](class_popupmenu.md#class_PopupMenu_property_prefer_native_menu) property of the child nodes.

---

<span id="class_MenuBar_property_start_index"></span>

[int](class_int.md#class_int) **start_index** = `-1` [🔗](class_menubar.md#class_MenuBar_property_start_index)

- void **set_start_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_start_index** ( )

Position order in the global menu to insert **MenuBar** items at. All menu items in the **MenuBar** are always inserted as a continuous range. Menus with lower [start_index](class_menubar.md#class_MenuBar_property_start_index) are inserted first. Menus with [start_index](class_menubar.md#class_MenuBar_property_start_index) equal to `-1` are inserted last.

---

<span id="class_MenuBar_property_switch_on_hover"></span>

[bool](class_bool.md#class_bool) **switch_on_hover** = `true` [🔗](class_menubar.md#class_MenuBar_property_switch_on_hover)

- void **set_switch_on_hover** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_switch_on_hover** ( )

If `true`, when the cursor hovers above menu item, it will close the current [PopupMenu](class_popupmenu.md#class_PopupMenu) and open the other one.

---

<span id="class_MenuBar_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_menubar.md#class_MenuBar_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

### Method Descriptions

<span id="class_MenuBar_method_get_menu_count"></span>

[int](class_int.md#class_int) **get_menu_count** ( ) *const* [🔗](class_menubar.md#class_MenuBar_method_get_menu_count)

Returns number of menu items.

---

<span id="class_MenuBar_method_get_menu_popup"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_menu_popup** ( menu: [int](class_int.md#class_int) ) *const* [🔗](class_menubar.md#class_MenuBar_method_get_menu_popup)

Returns [PopupMenu](class_popupmenu.md#class_PopupMenu) associated with menu item.

---

<span id="class_MenuBar_method_get_menu_title"></span>

[String](class_string.md#class_String) **get_menu_title** ( menu: [int](class_int.md#class_int) ) *const* [🔗](class_menubar.md#class_MenuBar_method_get_menu_title)

Returns menu item title.

---

<span id="class_MenuBar_method_get_menu_tooltip"></span>

[String](class_string.md#class_String) **get_menu_tooltip** ( menu: [int](class_int.md#class_int) ) *const* [🔗](class_menubar.md#class_MenuBar_method_get_menu_tooltip)

Returns menu item tooltip.

---

<span id="class_MenuBar_method_is_menu_disabled"></span>

[bool](class_bool.md#class_bool) **is_menu_disabled** ( menu: [int](class_int.md#class_int) ) *const* [🔗](class_menubar.md#class_MenuBar_method_is_menu_disabled)

Returns `true` if the menu item is disabled.

---

<span id="class_MenuBar_method_is_menu_hidden"></span>

[bool](class_bool.md#class_bool) **is_menu_hidden** ( menu: [int](class_int.md#class_int) ) *const* [🔗](class_menubar.md#class_MenuBar_method_is_menu_hidden)

Returns `true` if the menu item is hidden.

---

<span id="class_MenuBar_method_is_native_menu"></span>

[bool](class_bool.md#class_bool) **is_native_menu** ( ) *const* [🔗](class_menubar.md#class_MenuBar_method_is_native_menu)

Returns `true` if the current system's global menu is supported and used by this **MenuBar**.

---

<span id="class_MenuBar_method_set_disable_shortcuts"></span>

void **set_disable_shortcuts** ( disabled: [bool](class_bool.md#class_bool) ) [🔗](class_menubar.md#class_MenuBar_method_set_disable_shortcuts)

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---

<span id="class_MenuBar_method_set_menu_disabled"></span>

void **set_menu_disabled** ( menu: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_menubar.md#class_MenuBar_method_set_menu_disabled)

If `true`, menu item is disabled.

---

<span id="class_MenuBar_method_set_menu_hidden"></span>

void **set_menu_hidden** ( menu: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) [🔗](class_menubar.md#class_MenuBar_method_set_menu_hidden)

If `true`, menu item is hidden.

---

<span id="class_MenuBar_method_set_menu_title"></span>

void **set_menu_title** ( menu: [int](class_int.md#class_int), title: [String](class_string.md#class_String) ) [🔗](class_menubar.md#class_MenuBar_method_set_menu_title)

Sets menu item title.

---

<span id="class_MenuBar_method_set_menu_tooltip"></span>

void **set_menu_tooltip** ( menu: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_menubar.md#class_MenuBar_method_set_menu_tooltip)

Sets menu item tooltip.

---

### Theme Property Descriptions

<span id="class_MenuBar_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_color)

Default text [Color](class_color.md#class_Color) of the menu item.

---

<span id="class_MenuBar_theme_color_font_disabled_color"></span>

[Color](class_color.md#class_Color) **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_disabled_color)

Text [Color](class_color.md#class_Color) used when the menu item is disabled.

---

<span id="class_MenuBar_theme_color_font_focus_color"></span>

[Color](class_color.md#class_Color) **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_focus_color)

Text [Color](class_color.md#class_Color) used when the menu item is focused. Only replaces the normal text color of the menu item. Disabled, hovered, and pressed states take precedence over this color.

---

<span id="class_MenuBar_theme_color_font_hover_color"></span>

[Color](class_color.md#class_Color) **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_hover_color)

Text [Color](class_color.md#class_Color) used when the menu item is being hovered.

---

<span id="class_MenuBar_theme_color_font_hover_pressed_color"></span>

[Color](class_color.md#class_Color) **font_hover_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_hover_pressed_color)

Text [Color](class_color.md#class_Color) used when the menu item is being hovered and pressed.

---

<span id="class_MenuBar_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_outline_color)

The tint of text outline of the menu item.

---

<span id="class_MenuBar_theme_color_font_pressed_color"></span>

[Color](class_color.md#class_Color) **font_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_menubar.md#class_MenuBar_theme_color_font_pressed_color)

Text [Color](class_color.md#class_Color) used when the menu item is being pressed.

---

<span id="class_MenuBar_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `4` [🔗](class_menubar.md#class_MenuBar_theme_constant_h_separation)

The horizontal space between menu items.

---

<span id="class_MenuBar_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_menubar.md#class_MenuBar_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_menubar.md#class_MenuBar_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_MenuBar_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_menubar.md#class_MenuBar_theme_font_font)

[Font](class_font.md#class_Font) of the menu item's text.

---

<span id="class_MenuBar_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_menubar.md#class_MenuBar_theme_font_size_font_size)

Font size of the menu item's text.

---

<span id="class_MenuBar_theme_style_disabled"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **disabled** [🔗](class_menubar.md#class_MenuBar_theme_style_disabled)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is disabled.

---

<span id="class_MenuBar_theme_style_disabled_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **disabled_mirrored** [🔗](class_menubar.md#class_MenuBar_theme_style_disabled_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is disabled (for right-to-left layouts).

---

<span id="class_MenuBar_theme_style_hover"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover** [🔗](class_menubar.md#class_MenuBar_theme_style_hover)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is being hovered.

---

<span id="class_MenuBar_theme_style_hover_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover_mirrored** [🔗](class_menubar.md#class_MenuBar_theme_style_hover_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is being hovered (for right-to-left layouts).

---

<span id="class_MenuBar_theme_style_hover_pressed"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover_pressed** [🔗](class_menubar.md#class_MenuBar_theme_style_hover_pressed)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is being pressed and hovered at the same time.

---

<span id="class_MenuBar_theme_style_hover_pressed_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hover_pressed_mirrored** [🔗](class_menubar.md#class_MenuBar_theme_style_hover_pressed_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is being pressed and hovered at the same time (for right-to-left layouts).

---

<span id="class_MenuBar_theme_style_normal"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal** [🔗](class_menubar.md#class_MenuBar_theme_style_normal)

Default [StyleBox](class_stylebox.md#class_StyleBox) for the menu item.

---

<span id="class_MenuBar_theme_style_normal_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal_mirrored** [🔗](class_menubar.md#class_MenuBar_theme_style_normal_mirrored)

Default [StyleBox](class_stylebox.md#class_StyleBox) for the menu item (for right-to-left layouts).

---

<span id="class_MenuBar_theme_style_pressed"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **pressed** [🔗](class_menubar.md#class_MenuBar_theme_style_pressed)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is being pressed.

---

<span id="class_MenuBar_theme_style_pressed_mirrored"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **pressed_mirrored** [🔗](class_menubar.md#class_MenuBar_theme_style_pressed_mirrored)

[StyleBox](class_stylebox.md#class_StyleBox) used when the menu item is being pressed (for right-to-left layouts).
