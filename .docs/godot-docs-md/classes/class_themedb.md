<span id="class_ThemeDB"></span>

## ThemeDB

**Inherits:** [Object](class_object.md#class_Object)

A singleton that provides access to static information about [Theme](class_theme.md#class_Theme) resources used by the engine and by your project.

### Description

This singleton provides access to static information about [Theme](class_theme.md#class_Theme) resources used by the engine and by your projects. You can fetch the default engine theme, as well as your project configured theme.

 **ThemeDB** also contains fallback values for theme properties.

### Properties


| [float](class_float.md#class_float) | [fallback_base_scale](class_themedb.md#class_ThemeDB_property_fallback_base_scale) | `1.0` |
| --- | --- | --- |
| [Font](class_font.md#class_Font) | [fallback_font](class_themedb.md#class_ThemeDB_property_fallback_font) |
| [int](class_int.md#class_int) | [fallback_font_size](class_themedb.md#class_ThemeDB_property_fallback_font_size) | `16` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [fallback_icon](class_themedb.md#class_ThemeDB_property_fallback_icon) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [fallback_stylebox](class_themedb.md#class_ThemeDB_property_fallback_stylebox) |

### Methods


| [Theme](class_theme.md#class_Theme) | [get_default_theme](class_themedb.md#class_ThemeDB_method_get_default_theme) ( ) |
| --- | --- |
| [Theme](class_theme.md#class_Theme) | [get_project_theme](class_themedb.md#class_ThemeDB_method_get_project_theme) ( ) |

---

### Signals

<span id="class_ThemeDB_signal_fallback_changed"></span>

**fallback_changed** ( ) [🔗](class_themedb.md#class_ThemeDB_signal_fallback_changed)

Emitted when one of the fallback values had been changed. Use it to refresh the look of controls that may rely on the fallback theme items.

---

### Property Descriptions

<span id="class_ThemeDB_property_fallback_base_scale"></span>

[float](class_float.md#class_float) **fallback_base_scale** = `1.0` [🔗](class_themedb.md#class_ThemeDB_property_fallback_base_scale)

- void **set_fallback_base_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fallback_base_scale** ( )

The fallback base scale factor of every [Control](class_control.md#class_Control) node and [Theme](class_theme.md#class_Theme) resource. Used when no other value is available to the control.

See also [Theme.default_base_scale](class_theme.md#class_Theme_property_default_base_scale).

---

<span id="class_ThemeDB_property_fallback_font"></span>

[Font](class_font.md#class_Font) **fallback_font** [🔗](class_themedb.md#class_ThemeDB_property_fallback_font)

- void **set_fallback_font** ( value: [Font](class_font.md#class_Font) )
- [Font](class_font.md#class_Font) **get_fallback_font** ( )

The fallback font of every [Control](class_control.md#class_Control) node and [Theme](class_theme.md#class_Theme) resource. Used when no other value is available to the control.

See also [Theme.default_font](class_theme.md#class_Theme_property_default_font).

---

<span id="class_ThemeDB_property_fallback_font_size"></span>

[int](class_int.md#class_int) **fallback_font_size** = `16` [🔗](class_themedb.md#class_ThemeDB_property_fallback_font_size)

- void **set_fallback_font_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fallback_font_size** ( )

The fallback font size of every [Control](class_control.md#class_Control) node and [Theme](class_theme.md#class_Theme) resource. Used when no other value is available to the control.

See also [Theme.default_font_size](class_theme.md#class_Theme_property_default_font_size).

---

<span id="class_ThemeDB_property_fallback_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **fallback_icon** [🔗](class_themedb.md#class_ThemeDB_property_fallback_icon)

- void **set_fallback_icon** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_fallback_icon** ( )

The fallback icon of every [Control](class_control.md#class_Control) node and [Theme](class_theme.md#class_Theme) resource. Used when no other value is available to the control.

---

<span id="class_ThemeDB_property_fallback_stylebox"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **fallback_stylebox** [🔗](class_themedb.md#class_ThemeDB_property_fallback_stylebox)

- void **set_fallback_stylebox** ( value: [StyleBox](class_stylebox.md#class_StyleBox) )
- [StyleBox](class_stylebox.md#class_StyleBox) **get_fallback_stylebox** ( )

The fallback stylebox of every [Control](class_control.md#class_Control) node and [Theme](class_theme.md#class_Theme) resource. Used when no other value is available to the control.

---

### Method Descriptions

<span id="class_ThemeDB_method_get_default_theme"></span>

[Theme](class_theme.md#class_Theme) **get_default_theme** ( ) [🔗](class_themedb.md#class_ThemeDB_method_get_default_theme)

Returns a reference to the default engine [Theme](class_theme.md#class_Theme). This theme resource is responsible for the out-of-the-box look of [Control](class_control.md#class_Control) nodes and cannot be overridden.

---

<span id="class_ThemeDB_method_get_project_theme"></span>

[Theme](class_theme.md#class_Theme) **get_project_theme** ( ) [🔗](class_themedb.md#class_ThemeDB_method_get_project_theme)

Returns a reference to the custom project [Theme](class_theme.md#class_Theme). This theme resources allows to override the default engine theme for every control node in the project.

To set the project theme, see ProjectSettings.gui/theme/custom.
