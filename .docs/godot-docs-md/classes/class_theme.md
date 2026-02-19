<span id="class_Theme"></span>

## Theme

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A resource used for styling/skinning [Control](class_control.md#class_Control) s and [Window](class_window.md#class_Window) s.

### Description

A resource used for styling/skinning [Control](class_control.md#class_Control) and [Window](class_window.md#class_Window) nodes. While individual controls can be styled using their local theme overrides (see [Control.add_theme_color_override()](class_control.md#class_Control_method_add_theme_color_override)), theme resources allow you to store and apply the same settings across all controls sharing the same type (e.g. style all [Button](class_button.md#class_Button) s the same). One theme resource can be used for the entire project, but you can also set a separate theme resource to a branch of control nodes. A theme resource assigned to a control applies to the control itself, as well as all of its direct and indirect children (as long as a chain of controls is uninterrupted).

Use ProjectSettings.gui/theme/custom to set up a project-scope theme that will be available to every control in your project.

Use [Control.theme](class_control.md#class_Control_property_theme) of any control node to set up a theme that will be available to that control and all of its direct and indirect children.

### Tutorials

- [GUI skinning](../tutorials/ui/gui_skinning.md)

- [Using the theme editor](../tutorials/ui/gui_using_theme_editor.md)

### Properties


| [float](class_float.md#class_float) | [default_base_scale](class_theme.md#class_Theme_property_default_base_scale) | `0.0` |
| --- | --- | --- |
| [Font](class_font.md#class_Font) | [default_font](class_theme.md#class_Theme_property_default_font) |
| [int](class_int.md#class_int) | [default_font_size](class_theme.md#class_Theme_property_default_font_size) | `-1` |

### Methods


| void | [add_type](class_theme.md#class_Theme_method_add_type) ( theme_type: [StringName](class_stringname.md#class_StringName) ) |
| --- | --- |
| void | [clear](class_theme.md#class_Theme_method_clear) ( ) |
| void | [clear_color](class_theme.md#class_Theme_method_clear_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_constant](class_theme.md#class_Theme_method_clear_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_font](class_theme.md#class_Theme_method_clear_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_font_size](class_theme.md#class_Theme_method_clear_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_icon](class_theme.md#class_Theme_method_clear_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_stylebox](class_theme.md#class_Theme_method_clear_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_theme_item](class_theme.md#class_Theme_method_clear_theme_item) ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_type_variation](class_theme.md#class_Theme_method_clear_type_variation) ( theme_type: [StringName](class_stringname.md#class_StringName) ) |
| [Color](class_color.md#class_Color) | [get_color](class_theme.md#class_Theme_method_get_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_color_list](class_theme.md#class_Theme_method_get_color_list) ( theme_type: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_color_type_list](class_theme.md#class_Theme_method_get_color_type_list) ( ) const |
| [int](class_int.md#class_int) | [get_constant](class_theme.md#class_Theme_method_get_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_constant_list](class_theme.md#class_Theme_method_get_constant_list) ( theme_type: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_constant_type_list](class_theme.md#class_Theme_method_get_constant_type_list) ( ) const |
| [Font](class_font.md#class_Font) | [get_font](class_theme.md#class_Theme_method_get_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_font_list](class_theme.md#class_Theme_method_get_font_list) ( theme_type: [String](class_string.md#class_String) ) const |
| [int](class_int.md#class_int) | [get_font_size](class_theme.md#class_Theme_method_get_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_font_size_list](class_theme.md#class_Theme_method_get_font_size_list) ( theme_type: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_font_size_type_list](class_theme.md#class_Theme_method_get_font_size_type_list) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_font_type_list](class_theme.md#class_Theme_method_get_font_type_list) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_icon](class_theme.md#class_Theme_method_get_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_icon_list](class_theme.md#class_Theme_method_get_icon_list) ( theme_type: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_icon_type_list](class_theme.md#class_Theme_method_get_icon_type_list) ( ) const |
| [StyleBox](class_stylebox.md#class_StyleBox) | [get_stylebox](class_theme.md#class_Theme_method_get_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_stylebox_list](class_theme.md#class_Theme_method_get_stylebox_list) ( theme_type: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_stylebox_type_list](class_theme.md#class_Theme_method_get_stylebox_type_list) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_theme_item](class_theme.md#class_Theme_method_get_theme_item) ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_theme_item_list](class_theme.md#class_Theme_method_get_theme_item_list) ( data_type: [DataType](class_theme.md#enum_Theme_DataType), theme_type: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_theme_item_type_list](class_theme.md#class_Theme_method_get_theme_item_type_list) ( data_type: [DataType](class_theme.md#enum_Theme_DataType) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_type_list](class_theme.md#class_Theme_method_get_type_list) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_type_variation_base](class_theme.md#class_Theme_method_get_type_variation_base) ( theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_type_variation_list](class_theme.md#class_Theme_method_get_type_variation_list) ( base_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_color](class_theme.md#class_Theme_method_has_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_constant](class_theme.md#class_Theme_method_has_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_default_base_scale](class_theme.md#class_Theme_method_has_default_base_scale) ( ) const |
| [bool](class_bool.md#class_bool) | [has_default_font](class_theme.md#class_Theme_method_has_default_font) ( ) const |
| [bool](class_bool.md#class_bool) | [has_default_font_size](class_theme.md#class_Theme_method_has_default_font_size) ( ) const |
| [bool](class_bool.md#class_bool) | [has_font](class_theme.md#class_Theme_method_has_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_font_size](class_theme.md#class_Theme_method_has_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_icon](class_theme.md#class_Theme_method_has_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_stylebox](class_theme.md#class_Theme_method_has_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_item](class_theme.md#class_Theme_method_has_theme_item) ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [is_type_variation](class_theme.md#class_Theme_method_is_type_variation) ( theme_type: [StringName](class_stringname.md#class_StringName), base_type: [StringName](class_stringname.md#class_StringName) ) const |
| void | [merge_with](class_theme.md#class_Theme_method_merge_with) ( other: [Theme](class_theme.md#class_Theme) ) |
| void | [remove_type](class_theme.md#class_Theme_method_remove_type) ( theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_color](class_theme.md#class_Theme_method_rename_color) ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_constant](class_theme.md#class_Theme_method_rename_constant) ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_font](class_theme.md#class_Theme_method_rename_font) ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_font_size](class_theme.md#class_Theme_method_rename_font_size) ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_icon](class_theme.md#class_Theme_method_rename_icon) ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_stylebox](class_theme.md#class_Theme_method_rename_stylebox) ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_theme_item](class_theme.md#class_Theme_method_rename_theme_item) ( data_type: [DataType](class_theme.md#enum_Theme_DataType), old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_type](class_theme.md#class_Theme_method_rename_type) ( old_theme_type: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_color](class_theme.md#class_Theme_method_set_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) |
| void | [set_constant](class_theme.md#class_Theme_method_set_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), constant: [int](class_int.md#class_int) ) |
| void | [set_font](class_theme.md#class_Theme_method_set_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), font: [Font](class_font.md#class_Font) ) |
| void | [set_font_size](class_theme.md#class_Theme_method_set_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), font_size: [int](class_int.md#class_int) ) |
| void | [set_icon](class_theme.md#class_Theme_method_set_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_stylebox](class_theme.md#class_Theme_method_set_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), texture: [StyleBox](class_stylebox.md#class_StyleBox) ) |
| void | [set_theme_item](class_theme.md#class_Theme_method_set_theme_item) ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [set_type_variation](class_theme.md#class_Theme_method_set_type_variation) ( theme_type: [StringName](class_stringname.md#class_StringName), base_type: [StringName](class_stringname.md#class_StringName) ) |

---

### Enumerations

<span id="enum_Theme_DataType"></span>

enum **DataType**: [🔗](class_theme.md#enum_Theme_DataType)

<span id="class_Theme_constant_DATA_TYPE_COLOR"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_COLOR** = `0`

Theme's [Color](class_color.md#class_Color) item type.

<span id="class_Theme_constant_DATA_TYPE_CONSTANT"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_CONSTANT** = `1`

Theme's constant item type.

<span id="class_Theme_constant_DATA_TYPE_FONT"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_FONT** = `2`

Theme's [Font](class_font.md#class_Font) item type.

<span id="class_Theme_constant_DATA_TYPE_FONT_SIZE"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_FONT_SIZE** = `3`

Theme's font size item type.

<span id="class_Theme_constant_DATA_TYPE_ICON"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_ICON** = `4`

Theme's icon [Texture2D](class_texture2d.md#class_Texture2D) item type.

<span id="class_Theme_constant_DATA_TYPE_STYLEBOX"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_STYLEBOX** = `5`

Theme's [StyleBox](class_stylebox.md#class_StyleBox) item type.

<span id="class_Theme_constant_DATA_TYPE_MAX"></span>

[DataType](class_theme.md#enum_Theme_DataType) **DATA_TYPE_MAX** = `6`

Maximum value for the DataType enum.

---

### Property Descriptions

<span id="class_Theme_property_default_base_scale"></span>

[float](class_float.md#class_float) **default_base_scale** = `0.0` [🔗](class_theme.md#class_Theme_property_default_base_scale)

- void **set_default_base_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_default_base_scale** ( )

The default base scale factor of this theme resource. Used by some controls to scale their visual properties based on the global scale factor. If this value is set to `0.0`, the global scale factor is used (see [ThemeDB.fallback_base_scale](class_themedb.md#class_ThemeDB_property_fallback_base_scale)).

Use [has_default_base_scale()](class_theme.md#class_Theme_method_has_default_base_scale) to check if this value is valid.

---

<span id="class_Theme_property_default_font"></span>

[Font](class_font.md#class_Font) **default_font** [🔗](class_theme.md#class_Theme_property_default_font)

- void **set_default_font** ( value: [Font](class_font.md#class_Font) )
- [Font](class_font.md#class_Font) **get_default_font** ( )

The default font of this theme resource. Used as the default value when trying to fetch a font resource that doesn't exist in this theme or is in invalid state. If the default font is also missing or invalid, the engine fallback value is used (see [ThemeDB.fallback_font](class_themedb.md#class_ThemeDB_property_fallback_font)).

Use [has_default_font()](class_theme.md#class_Theme_method_has_default_font) to check if this value is valid.

---

<span id="class_Theme_property_default_font_size"></span>

[int](class_int.md#class_int) **default_font_size** = `-1` [🔗](class_theme.md#class_Theme_property_default_font_size)

- void **set_default_font_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_default_font_size** ( )

The default font size of this theme resource. Used as the default value when trying to fetch a font size value that doesn't exist in this theme or is in invalid state. If the default font size is also missing or invalid, the engine fallback value is used (see [ThemeDB.fallback_font_size](class_themedb.md#class_ThemeDB_property_fallback_font_size)).

Values below `1` are invalid and can be used to unset the property. Use [has_default_font_size()](class_theme.md#class_Theme_method_has_default_font_size) to check if this value is valid.

---

### Method Descriptions

<span id="class_Theme_method_add_type"></span>

void **add_type** ( theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_add_type)

Adds an empty theme type for every valid data type.

 **Note:** Empty types are not saved with the theme. This method only exists to perform in-memory changes to the resource. Use available `set_*` methods to add theme items.

---

<span id="class_Theme_method_clear"></span>

void **clear** ( ) [🔗](class_theme.md#class_Theme_method_clear)

Removes all the theme properties defined on the theme resource.

---

<span id="class_Theme_method_clear_color"></span>

void **clear_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_color)

Removes the [Color](class_color.md#class_Color) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_color()](class_theme.md#class_Theme_method_has_color) to check for existence.

---

<span id="class_Theme_method_clear_constant"></span>

void **clear_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_constant)

Removes the constant property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_constant()](class_theme.md#class_Theme_method_has_constant) to check for existence.

---

<span id="class_Theme_method_clear_font"></span>

void **clear_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_font)

Removes the [Font](class_font.md#class_Font) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_font()](class_theme.md#class_Theme_method_has_font) to check for existence.

---

<span id="class_Theme_method_clear_font_size"></span>

void **clear_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_font_size)

Removes the font size property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_font_size()](class_theme.md#class_Theme_method_has_font_size) to check for existence.

---

<span id="class_Theme_method_clear_icon"></span>

void **clear_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_icon)

Removes the icon property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_icon()](class_theme.md#class_Theme_method_has_icon) to check for existence.

---

<span id="class_Theme_method_clear_stylebox"></span>

void **clear_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_stylebox)

Removes the [StyleBox](class_stylebox.md#class_StyleBox) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_stylebox()](class_theme.md#class_Theme_method_has_stylebox) to check for existence.

---

<span id="class_Theme_method_clear_theme_item"></span>

void **clear_theme_item** ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_theme_item)

Removes the theme property of `data_type` defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use [has_theme_item()](class_theme.md#class_Theme_method_has_theme_item) to check for existence.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_clear_type_variation"></span>

void **clear_type_variation** ( theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_clear_type_variation)

Unmarks `theme_type` as being a variation of another theme type. See [set_type_variation()](class_theme.md#class_Theme_method_set_type_variation).

---

<span id="class_Theme_method_get_color"></span>

[Color](class_color.md#class_Color) **get_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_color)

Returns the [Color](class_color.md#class_Color) property defined by `name` and `theme_type`, if it exists.

Returns the default color value if the property doesn't exist. Use [has_color()](class_theme.md#class_Theme_method_has_color) to check for existence.

---

<span id="class_Theme_method_get_color_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_color_list** ( theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_color_list)

Returns a list of names for [Color](class_color.md#class_Color) properties defined with `theme_type`. Use [get_color_type_list()](class_theme.md#class_Theme_method_get_color_type_list) to get a list of possible theme type names.

---

<span id="class_Theme_method_get_color_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_color_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_color_type_list)

Returns a list of all unique theme type names for [Color](class_color.md#class_Color) properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

---

<span id="class_Theme_method_get_constant"></span>

[int](class_int.md#class_int) **get_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_constant)

Returns the constant property defined by `name` and `theme_type`, if it exists.

Returns `0` if the property doesn't exist. Use [has_constant()](class_theme.md#class_Theme_method_has_constant) to check for existence.

---

<span id="class_Theme_method_get_constant_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_constant_list** ( theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_constant_list)

Returns a list of names for constant properties defined with `theme_type`. Use [get_constant_type_list()](class_theme.md#class_Theme_method_get_constant_type_list) to get a list of possible theme type names.

---

<span id="class_Theme_method_get_constant_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_constant_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_constant_type_list)

Returns a list of all unique theme type names for constant properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

---

<span id="class_Theme_method_get_font"></span>

[Font](class_font.md#class_Font) **get_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_font)

Returns the [Font](class_font.md#class_Font) property defined by `name` and `theme_type`, if it exists.

Returns the default theme font if the property doesn't exist and the default theme font is set up (see [default_font](class_theme.md#class_Theme_property_default_font)). Use [has_font()](class_theme.md#class_Theme_method_has_font) to check for existence of the property and [has_default_font()](class_theme.md#class_Theme_method_has_default_font) to check for existence of the default theme font.

Returns the engine fallback font value, if neither exist (see [ThemeDB.fallback_font](class_themedb.md#class_ThemeDB_property_fallback_font)).

---

<span id="class_Theme_method_get_font_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_font_list** ( theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_font_list)

Returns a list of names for [Font](class_font.md#class_Font) properties defined with `theme_type`. Use [get_font_type_list()](class_theme.md#class_Theme_method_get_font_type_list) to get a list of possible theme type names.

---

<span id="class_Theme_method_get_font_size"></span>

[int](class_int.md#class_int) **get_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_font_size)

Returns the font size property defined by `name` and `theme_type`, if it exists.

Returns the default theme font size if the property doesn't exist and the default theme font size is set up (see [default_font_size](class_theme.md#class_Theme_property_default_font_size)). Use [has_font_size()](class_theme.md#class_Theme_method_has_font_size) to check for existence of the property and [has_default_font_size()](class_theme.md#class_Theme_method_has_default_font_size) to check for existence of the default theme font.

Returns the engine fallback font size value, if neither exist (see [ThemeDB.fallback_font_size](class_themedb.md#class_ThemeDB_property_fallback_font_size)).

---

<span id="class_Theme_method_get_font_size_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_font_size_list** ( theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_font_size_list)

Returns a list of names for font size properties defined with `theme_type`. Use [get_font_size_type_list()](class_theme.md#class_Theme_method_get_font_size_type_list) to get a list of possible theme type names.

---

<span id="class_Theme_method_get_font_size_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_font_size_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_font_size_type_list)

Returns a list of all unique theme type names for font size properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

---

<span id="class_Theme_method_get_font_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_font_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_font_type_list)

Returns a list of all unique theme type names for [Font](class_font.md#class_Font) properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

---

<span id="class_Theme_method_get_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_icon)

Returns the icon property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback icon value if the property doesn't exist (see [ThemeDB.fallback_icon](class_themedb.md#class_ThemeDB_property_fallback_icon)). Use [has_icon()](class_theme.md#class_Theme_method_has_icon) to check for existence.

---

<span id="class_Theme_method_get_icon_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_icon_list** ( theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_icon_list)

Returns a list of names for icon properties defined with `theme_type`. Use [get_icon_type_list()](class_theme.md#class_Theme_method_get_icon_type_list) to get a list of possible theme type names.

---

<span id="class_Theme_method_get_icon_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_icon_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_icon_type_list)

Returns a list of all unique theme type names for icon properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

---

<span id="class_Theme_method_get_stylebox"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **get_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_stylebox)

Returns the [StyleBox](class_stylebox.md#class_StyleBox) property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback stylebox value if the property doesn't exist (see [ThemeDB.fallback_stylebox](class_themedb.md#class_ThemeDB_property_fallback_stylebox)). Use [has_stylebox()](class_theme.md#class_Theme_method_has_stylebox) to check for existence.

---

<span id="class_Theme_method_get_stylebox_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_stylebox_list** ( theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_stylebox_list)

Returns a list of names for [StyleBox](class_stylebox.md#class_StyleBox) properties defined with `theme_type`. Use [get_stylebox_type_list()](class_theme.md#class_Theme_method_get_stylebox_type_list) to get a list of possible theme type names.

---

<span id="class_Theme_method_get_stylebox_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_stylebox_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_stylebox_type_list)

Returns a list of all unique theme type names for [StyleBox](class_stylebox.md#class_StyleBox) properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

---

<span id="class_Theme_method_get_theme_item"></span>

[Variant](class_variant.md#class_Variant) **get_theme_item** ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_theme_item)

Returns the theme property of `data_type` defined by `name` and `theme_type`, if it exists.

Returns the engine fallback value if the property doesn't exist (see [ThemeDB](class_themedb.md#class_ThemeDB)). Use [has_theme_item()](class_theme.md#class_Theme_method_has_theme_item) to check for existence.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_get_theme_item_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_theme_item_list** ( data_type: [DataType](class_theme.md#enum_Theme_DataType), theme_type: [String](class_string.md#class_String) ) *const* [🔗](class_theme.md#class_Theme_method_get_theme_item_list)

Returns a list of names for properties of `data_type` defined with `theme_type`. Use [get_theme_item_type_list()](class_theme.md#class_Theme_method_get_theme_item_type_list) to get a list of possible theme type names.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_get_theme_item_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_theme_item_type_list** ( data_type: [DataType](class_theme.md#enum_Theme_DataType) ) *const* [🔗](class_theme.md#class_Theme_method_get_theme_item_type_list)

Returns a list of all unique theme type names for `data_type` properties. Use [get_type_list()](class_theme.md#class_Theme_method_get_type_list) to get a list of all unique theme types.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_get_type_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_type_list** ( ) *const* [🔗](class_theme.md#class_Theme_method_get_type_list)

Returns a list of all unique theme type names. Use the appropriate `get_*_type_list` method to get a list of unique theme types for a single data type.

---

<span id="class_Theme_method_get_type_variation_base"></span>

[StringName](class_stringname.md#class_StringName) **get_type_variation_base** ( theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_type_variation_base)

Returns the name of the base theme type if `theme_type` is a valid variation type. Returns an empty string otherwise.

---

<span id="class_Theme_method_get_type_variation_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_type_variation_list** ( base_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_get_type_variation_list)

Returns a list of all type variations for the given `base_type`.

---

<span id="class_Theme_method_has_color"></span>

[bool](class_bool.md#class_bool) **has_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_color)

Returns `true` if the [Color](class_color.md#class_Color) property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_color()](class_theme.md#class_Theme_method_set_color) to define it.

---

<span id="class_Theme_method_has_constant"></span>

[bool](class_bool.md#class_bool) **has_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_constant)

Returns `true` if the constant property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_constant()](class_theme.md#class_Theme_method_set_constant) to define it.

---

<span id="class_Theme_method_has_default_base_scale"></span>

[bool](class_bool.md#class_bool) **has_default_base_scale** ( ) *const* [🔗](class_theme.md#class_Theme_method_has_default_base_scale)

Returns `true` if [default_base_scale](class_theme.md#class_Theme_property_default_base_scale) has a valid value.

Returns `false` if it doesn't. The value must be greater than `0.0` to be considered valid.

---

<span id="class_Theme_method_has_default_font"></span>

[bool](class_bool.md#class_bool) **has_default_font** ( ) *const* [🔗](class_theme.md#class_Theme_method_has_default_font)

Returns `true` if [default_font](class_theme.md#class_Theme_property_default_font) has a valid value.

Returns `false` if it doesn't.

---

<span id="class_Theme_method_has_default_font_size"></span>

[bool](class_bool.md#class_bool) **has_default_font_size** ( ) *const* [🔗](class_theme.md#class_Theme_method_has_default_font_size)

Returns `true` if [default_font_size](class_theme.md#class_Theme_property_default_font_size) has a valid value.

Returns `false` if it doesn't. The value must be greater than `0` to be considered valid.

---

<span id="class_Theme_method_has_font"></span>

[bool](class_bool.md#class_bool) **has_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_font)

Returns `true` if the [Font](class_font.md#class_Font) property defined by `name` and `theme_type` exists, or if the default theme font is set up (see [has_default_font()](class_theme.md#class_Theme_method_has_default_font)).

Returns `false` if neither exist. Use [set_font()](class_theme.md#class_Theme_method_set_font) to define the property.

---

<span id="class_Theme_method_has_font_size"></span>

[bool](class_bool.md#class_bool) **has_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_font_size)

Returns `true` if the font size property defined by `name` and `theme_type` exists, or if the default theme font size is set up (see [has_default_font_size()](class_theme.md#class_Theme_method_has_default_font_size)).

Returns `false` if neither exist. Use [set_font_size()](class_theme.md#class_Theme_method_set_font_size) to define the property.

---

<span id="class_Theme_method_has_icon"></span>

[bool](class_bool.md#class_bool) **has_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_icon)

Returns `true` if the icon property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_icon()](class_theme.md#class_Theme_method_set_icon) to define it.

---

<span id="class_Theme_method_has_stylebox"></span>

[bool](class_bool.md#class_bool) **has_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_stylebox)

Returns `true` if the [StyleBox](class_stylebox.md#class_StyleBox) property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_stylebox()](class_theme.md#class_Theme_method_set_stylebox) to define it.

---

<span id="class_Theme_method_has_theme_item"></span>

[bool](class_bool.md#class_bool) **has_theme_item** ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_has_theme_item)

Returns `true` if the theme property of `data_type` defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use [set_theme_item()](class_theme.md#class_Theme_method_set_theme_item) to define it.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_is_type_variation"></span>

[bool](class_bool.md#class_bool) **is_type_variation** ( theme_type: [StringName](class_stringname.md#class_StringName), base_type: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_theme.md#class_Theme_method_is_type_variation)

Returns `true` if `theme_type` is marked as a variation of `base_type`.

---

<span id="class_Theme_method_merge_with"></span>

void **merge_with** ( other: [Theme](class_theme.md#class_Theme) ) [🔗](class_theme.md#class_Theme_method_merge_with)

Adds missing and overrides existing definitions with values from the `other` theme resource.

 **Note:** This modifies the current theme. If you want to merge two themes together without modifying either one, create a new empty theme and merge the other two into it one after another.

---

<span id="class_Theme_method_remove_type"></span>

void **remove_type** ( theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_remove_type)

Removes the theme type, gracefully discarding defined theme items. If the type is a variation, this information is also erased. If the type is a base for type variations, those variations lose their base.

---

<span id="class_Theme_method_rename_color"></span>

void **rename_color** ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_color)

Renames the [Color](class_color.md#class_Color) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_color()](class_theme.md#class_Theme_method_has_color) to check for existence, and [clear_color()](class_theme.md#class_Theme_method_clear_color) to remove the existing property.

---

<span id="class_Theme_method_rename_constant"></span>

void **rename_constant** ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_constant)

Renames the constant property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_constant()](class_theme.md#class_Theme_method_has_constant) to check for existence, and [clear_constant()](class_theme.md#class_Theme_method_clear_constant) to remove the existing property.

---

<span id="class_Theme_method_rename_font"></span>

void **rename_font** ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_font)

Renames the [Font](class_font.md#class_Font) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_font()](class_theme.md#class_Theme_method_has_font) to check for existence, and [clear_font()](class_theme.md#class_Theme_method_clear_font) to remove the existing property.

---

<span id="class_Theme_method_rename_font_size"></span>

void **rename_font_size** ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_font_size)

Renames the font size property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_font_size()](class_theme.md#class_Theme_method_has_font_size) to check for existence, and [clear_font_size()](class_theme.md#class_Theme_method_clear_font_size) to remove the existing property.

---

<span id="class_Theme_method_rename_icon"></span>

void **rename_icon** ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_icon)

Renames the icon property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_icon()](class_theme.md#class_Theme_method_has_icon) to check for existence, and [clear_icon()](class_theme.md#class_Theme_method_clear_icon) to remove the existing property.

---

<span id="class_Theme_method_rename_stylebox"></span>

void **rename_stylebox** ( old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_stylebox)

Renames the [StyleBox](class_stylebox.md#class_StyleBox) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_stylebox()](class_theme.md#class_Theme_method_has_stylebox) to check for existence, and [clear_stylebox()](class_theme.md#class_Theme_method_clear_stylebox) to remove the existing property.

---

<span id="class_Theme_method_rename_theme_item"></span>

void **rename_theme_item** ( data_type: [DataType](class_theme.md#enum_Theme_DataType), old_name: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_theme_item)

Renames the theme property of `data_type` defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use [has_theme_item()](class_theme.md#class_Theme_method_has_theme_item) to check for existence, and [clear_theme_item()](class_theme.md#class_Theme_method_clear_theme_item) to remove the existing property.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_rename_type"></span>

void **rename_type** ( old_theme_type: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_rename_type)

Renames the theme type `old_theme_type` to `theme_type`, if the old type exists and the new one doesn't exist.

 **Note:** Renaming a theme type to an empty name or a variation to a type associated with a built-in class removes type variation connections in a way that cannot be undone by reversing the rename alone.

---

<span id="class_Theme_method_set_color"></span>

void **set_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) [🔗](class_theme.md#class_Theme_method_set_color)

Creates or changes the value of the [Color](class_color.md#class_Color) property defined by `name` and `theme_type`. Use [clear_color()](class_theme.md#class_Theme_method_clear_color) to remove the property.

---

<span id="class_Theme_method_set_constant"></span>

void **set_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), constant: [int](class_int.md#class_int) ) [🔗](class_theme.md#class_Theme_method_set_constant)

Creates or changes the value of the constant property defined by `name` and `theme_type`. Use [clear_constant()](class_theme.md#class_Theme_method_clear_constant) to remove the property.

---

<span id="class_Theme_method_set_font"></span>

void **set_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), font: [Font](class_font.md#class_Font) ) [🔗](class_theme.md#class_Theme_method_set_font)

Creates or changes the value of the [Font](class_font.md#class_Font) property defined by `name` and `theme_type`. Use [clear_font()](class_theme.md#class_Theme_method_clear_font) to remove the property.

---

<span id="class_Theme_method_set_font_size"></span>

void **set_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), font_size: [int](class_int.md#class_int) ) [🔗](class_theme.md#class_Theme_method_set_font_size)

Creates or changes the value of the font size property defined by `name` and `theme_type`. Use [clear_font_size()](class_theme.md#class_Theme_method_clear_font_size) to remove the property.

---

<span id="class_Theme_method_set_icon"></span>

void **set_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_theme.md#class_Theme_method_set_icon)

Creates or changes the value of the icon property defined by `name` and `theme_type`. Use [clear_icon()](class_theme.md#class_Theme_method_clear_icon) to remove the property.

---

<span id="class_Theme_method_set_stylebox"></span>

void **set_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), texture: [StyleBox](class_stylebox.md#class_StyleBox) ) [🔗](class_theme.md#class_Theme_method_set_stylebox)

Creates or changes the value of the [StyleBox](class_stylebox.md#class_StyleBox) property defined by `name` and `theme_type`. Use [clear_stylebox()](class_theme.md#class_Theme_method_clear_stylebox) to remove the property.

---

<span id="class_Theme_method_set_theme_item"></span>

void **set_theme_item** ( data_type: [DataType](class_theme.md#enum_Theme_DataType), name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_theme.md#class_Theme_method_set_theme_item)

Creates or changes the value of the theme property of `data_type` defined by `name` and `theme_type`. Use [clear_theme_item()](class_theme.md#class_Theme_method_clear_theme_item) to remove the property.

Fails if the `value` type is not accepted by `data_type`.

 **Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

<span id="class_Theme_method_set_type_variation"></span>

void **set_type_variation** ( theme_type: [StringName](class_stringname.md#class_StringName), base_type: [StringName](class_stringname.md#class_StringName) ) [🔗](class_theme.md#class_Theme_method_set_type_variation)

Marks `theme_type` as a variation of `base_type`.

This adds `theme_type` as a suggested option for [Control.theme_type_variation](class_control.md#class_Control_property_theme_type_variation) on a [Control](class_control.md#class_Control) that is of the `base_type` class.

Variations can also be nested, i.e. `base_type` can be another variation. If a chain of variations ends with a `base_type` matching the class of the [Control](class_control.md#class_Control), the whole chain is going to be suggested as options.

 **Note:** Suggestions only show up if this theme resource is set as the project default theme. See ProjectSettings.gui/theme/custom.
