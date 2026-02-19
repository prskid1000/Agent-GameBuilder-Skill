.. meta::
	:keywords: select, dropdown

<span id="class_OptionButton"></span>

## OptionButton

**Inherits:** [Button](class_button.md#class_Button) **<** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A button that brings up a dropdown with selectable options when pressed.

### Description

**OptionButton** is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

 **Note:** The IDs used for items are limited to signed 32-bit integers, not the full 64 bits of [int](class_int.md#class_int). These have a range of `-2^31` to `2^31 - 1`, that is, `-2147483648` to `2147483647`.

 **Note:** The [Button.text](class_button.md#class_Button_property_text) and [Button.icon](class_button.md#class_Button_property_icon) properties are set automatically based on the selected item. They shouldn't be changed manually.

### Properties


| [ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) | action_mode | `0` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_action_mode)) |
| --- | --- | --- |
| HorizontalAlignment | alignment | `0` (overrides [Button](class_button.md#class_Button_property_alignment)) |
| [bool](class_bool.md#class_bool) | [allow_reselect](class_optionbutton.md#class_OptionButton_property_allow_reselect) | `false` |
| [bool](class_bool.md#class_bool) | [fit_to_longest_item](class_optionbutton.md#class_OptionButton_property_fit_to_longest_item) | `true` |
| [int](class_int.md#class_int) | [item_count](class_optionbutton.md#class_OptionButton_property_item_count) | `0` |
| [int](class_int.md#class_int) | [selected](class_optionbutton.md#class_OptionButton_property_selected) | `-1` |
| [bool](class_bool.md#class_bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_toggle_mode)) |

### Methods


| void | [add_icon_item](class_optionbutton.md#class_OptionButton_method_add_icon_item) ( texture: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), id: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [add_item](class_optionbutton.md#class_OptionButton_method_add_item) ( label: [String](class_string.md#class_String), id: [int](class_int.md#class_int) = -1 ) |
| void | [add_separator](class_optionbutton.md#class_OptionButton_method_add_separator) ( text: [String](class_string.md#class_String) = "" ) |
| void | [clear](class_optionbutton.md#class_OptionButton_method_clear) ( ) |
| [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) | [get_item_auto_translate_mode](class_optionbutton.md#class_OptionButton_method_get_item_auto_translate_mode) ( idx: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_item_icon](class_optionbutton.md#class_OptionButton_method_get_item_icon) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_item_id](class_optionbutton.md#class_OptionButton_method_get_item_id) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_item_index](class_optionbutton.md#class_OptionButton_method_get_item_index) ( id: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_item_metadata](class_optionbutton.md#class_OptionButton_method_get_item_metadata) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_item_text](class_optionbutton.md#class_OptionButton_method_get_item_text) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_item_tooltip](class_optionbutton.md#class_OptionButton_method_get_item_tooltip) ( idx: [int](class_int.md#class_int) ) const |
| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_popup](class_optionbutton.md#class_OptionButton_method_get_popup) ( ) const |
| [int](class_int.md#class_int) | [get_selectable_item](class_optionbutton.md#class_OptionButton_method_get_selectable_item) ( from_last: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [get_selected_id](class_optionbutton.md#class_OptionButton_method_get_selected_id) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_selected_metadata](class_optionbutton.md#class_OptionButton_method_get_selected_metadata) ( ) const |
| [bool](class_bool.md#class_bool) | [has_selectable_items](class_optionbutton.md#class_OptionButton_method_has_selectable_items) ( ) const |
| [bool](class_bool.md#class_bool) | [is_item_disabled](class_optionbutton.md#class_OptionButton_method_is_item_disabled) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_item_separator](class_optionbutton.md#class_OptionButton_method_is_item_separator) ( idx: [int](class_int.md#class_int) ) const |
| void | [remove_item](class_optionbutton.md#class_OptionButton_method_remove_item) ( idx: [int](class_int.md#class_int) ) |
| void | [select](class_optionbutton.md#class_OptionButton_method_select) ( idx: [int](class_int.md#class_int) ) |
| void | [set_disable_shortcuts](class_optionbutton.md#class_OptionButton_method_set_disable_shortcuts) ( disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_item_auto_translate_mode](class_optionbutton.md#class_OptionButton_method_set_item_auto_translate_mode) ( idx: [int](class_int.md#class_int), mode: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) ) |
| void | [set_item_disabled](class_optionbutton.md#class_OptionButton_method_set_item_disabled) ( idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_item_icon](class_optionbutton.md#class_OptionButton_method_set_item_icon) ( idx: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_item_id](class_optionbutton.md#class_OptionButton_method_set_item_id) ( idx: [int](class_int.md#class_int), id: [int](class_int.md#class_int) ) |
| void | [set_item_metadata](class_optionbutton.md#class_OptionButton_method_set_item_metadata) ( idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) |
| void | [set_item_text](class_optionbutton.md#class_OptionButton_method_set_item_text) ( idx: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [set_item_tooltip](class_optionbutton.md#class_OptionButton_method_set_item_tooltip) ( idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |
| void | [show_popup](class_optionbutton.md#class_OptionButton_method_show_popup) ( ) |

### Theme Properties


| [int](class_int.md#class_int) | [arrow_margin](class_optionbutton.md#class_OptionButton_theme_constant_arrow_margin) | `4` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [modulate_arrow](class_optionbutton.md#class_OptionButton_theme_constant_modulate_arrow) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [arrow](class_optionbutton.md#class_OptionButton_theme_icon_arrow) |

---

### Signals

<span id="class_OptionButton_signal_item_focused"></span>

**item_focused** ( index: [int](class_int.md#class_int) ) [🔗](class_optionbutton.md#class_OptionButton_signal_item_focused)

Emitted when the user navigates to an item using the ProjectSettings.input/ui_up or ProjectSettings.input/ui_down input actions. The index of the item selected is passed as argument.

---

<span id="class_OptionButton_signal_item_selected"></span>

**item_selected** ( index: [int](class_int.md#class_int) ) [🔗](class_optionbutton.md#class_OptionButton_signal_item_selected)

Emitted when the current item has been changed by the user. The index of the item selected is passed as argument.

 [allow_reselect](class_optionbutton.md#class_OptionButton_property_allow_reselect) must be enabled to reselect an item.

---

### Property Descriptions

<span id="class_OptionButton_property_allow_reselect"></span>

[bool](class_bool.md#class_bool) **allow_reselect** = `false` [🔗](class_optionbutton.md#class_OptionButton_property_allow_reselect)

- void **set_allow_reselect** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_allow_reselect** ( )

If `true`, the currently selected item can be selected again.

---

<span id="class_OptionButton_property_fit_to_longest_item"></span>

[bool](class_bool.md#class_bool) **fit_to_longest_item** = `true` [🔗](class_optionbutton.md#class_OptionButton_property_fit_to_longest_item)

- void **set_fit_to_longest_item** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_fit_to_longest_item** ( )

If `true`, minimum size will be determined by the longest item's text, instead of the currently selected one's.

 **Note:** For performance reasons, the minimum size doesn't update immediately when adding, removing or modifying items.

---

<span id="class_OptionButton_property_item_count"></span>

[int](class_int.md#class_int) **item_count** = `0` [🔗](class_optionbutton.md#class_OptionButton_property_item_count)

- void **set_item_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_item_count** ( )

The number of items to select from.

---

<span id="class_OptionButton_property_selected"></span>

[int](class_int.md#class_int) **selected** = `-1` [🔗](class_optionbutton.md#class_OptionButton_property_selected)

- [int](class_int.md#class_int) **get_selected** ( )

The index of the currently selected item, or `-1` if no item is selected.

---

### Method Descriptions

<span id="class_OptionButton_method_add_icon_item"></span>

void **add_icon_item** ( texture: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), id: [int](class_int.md#class_int) = -1 ) [🔗](class_optionbutton.md#class_OptionButton_method_add_icon_item)

Adds an item, with a `texture` icon, text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

 **Note:** The item will be selected if there are no other items.

---

<span id="class_OptionButton_method_add_item"></span>

void **add_item** ( label: [String](class_string.md#class_String), id: [int](class_int.md#class_int) = -1 ) [🔗](class_optionbutton.md#class_OptionButton_method_add_item)

Adds an item, with text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

 **Note:** The item will be selected if there are no other items.

---

<span id="class_OptionButton_method_add_separator"></span>

void **add_separator** ( text: [String](class_string.md#class_String) = "" ) [🔗](class_optionbutton.md#class_OptionButton_method_add_separator)

Adds a separator to the list of items. Separators help to group items, and can optionally be given a `text` header. A separator also gets an index assigned, and is appended at the end of the item list.

---

<span id="class_OptionButton_method_clear"></span>

void **clear** ( ) [🔗](class_optionbutton.md#class_OptionButton_method_clear)

Clears all the items in the **OptionButton**.

---

<span id="class_OptionButton_method_get_item_auto_translate_mode"></span>

[AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) **get_item_auto_translate_mode** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_auto_translate_mode)

Returns the auto translate mode of the item at index `idx`.

---

<span id="class_OptionButton_method_get_item_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_item_icon** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_icon)

Returns the icon of the item at index `idx`.

---

<span id="class_OptionButton_method_get_item_id"></span>

[int](class_int.md#class_int) **get_item_id** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_id)

Returns the ID of the item at index `idx`.

---

<span id="class_OptionButton_method_get_item_index"></span>

[int](class_int.md#class_int) **get_item_index** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_index)

Returns the index of the item with the given `id`.

---

<span id="class_OptionButton_method_get_item_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_item_metadata** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_metadata)

Retrieves the metadata of an item. Metadata may be any type and can be used to store extra information about an item, such as an external string ID.

---

<span id="class_OptionButton_method_get_item_text"></span>

[String](class_string.md#class_String) **get_item_text** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_text)

Returns the text of the item at index `idx`.

---

<span id="class_OptionButton_method_get_item_tooltip"></span>

[String](class_string.md#class_String) **get_item_tooltip** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_item_tooltip)

Returns the tooltip of the item at index `idx`.

---

<span id="class_OptionButton_method_get_popup"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_popup** ( ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_popup)

Returns the [PopupMenu](class_popupmenu.md#class_PopupMenu) contained in this button.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

<span id="class_OptionButton_method_get_selectable_item"></span>

[int](class_int.md#class_int) **get_selectable_item** ( from_last: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_selectable_item)

Returns the index of the first item which is not disabled, or marked as a separator. If `from_last` is `true`, the items will be searched in reverse order.

Returns `-1` if no item is found.

---

<span id="class_OptionButton_method_get_selected_id"></span>

[int](class_int.md#class_int) **get_selected_id** ( ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_selected_id)

Returns the ID of the selected item, or `-1` if no item is selected.

---

<span id="class_OptionButton_method_get_selected_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_selected_metadata** ( ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_get_selected_metadata)

Gets the metadata of the selected item. Metadata for items can be set using [set_item_metadata()](class_optionbutton.md#class_OptionButton_method_set_item_metadata).

---

<span id="class_OptionButton_method_has_selectable_items"></span>

[bool](class_bool.md#class_bool) **has_selectable_items** ( ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_has_selectable_items)

Returns `true` if this button contains at least one item which is not disabled, or marked as a separator.

---

<span id="class_OptionButton_method_is_item_disabled"></span>

[bool](class_bool.md#class_bool) **is_item_disabled** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_is_item_disabled)

Returns `true` if the item at index `idx` is disabled.

---

<span id="class_OptionButton_method_is_item_separator"></span>

[bool](class_bool.md#class_bool) **is_item_separator** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_optionbutton.md#class_OptionButton_method_is_item_separator)

Returns `true` if the item at index `idx` is marked as a separator.

---

<span id="class_OptionButton_method_remove_item"></span>

void **remove_item** ( idx: [int](class_int.md#class_int) ) [🔗](class_optionbutton.md#class_OptionButton_method_remove_item)

Removes the item at index `idx`.

---

<span id="class_OptionButton_method_select"></span>

void **select** ( idx: [int](class_int.md#class_int) ) [🔗](class_optionbutton.md#class_OptionButton_method_select)

Selects an item by index and makes it the current item. This will work even if the item is disabled.

Passing `-1` as the index deselects any currently selected item.

---

<span id="class_OptionButton_method_set_disable_shortcuts"></span>

void **set_disable_shortcuts** ( disabled: [bool](class_bool.md#class_bool) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_disable_shortcuts)

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---

<span id="class_OptionButton_method_set_item_auto_translate_mode"></span>

void **set_item_auto_translate_mode** ( idx: [int](class_int.md#class_int), mode: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_auto_translate_mode)

Sets the auto translate mode of the item at index `idx`.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT) by default, which uses the same auto translate mode as the **OptionButton** itself.

---

<span id="class_OptionButton_method_set_item_disabled"></span>

void **set_item_disabled** ( idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_disabled)

Sets whether the item at index `idx` is disabled.

Disabled items are drawn differently in the dropdown and are not selectable by the user. If the current selected item is set as disabled, it will remain selected.

---

<span id="class_OptionButton_method_set_item_icon"></span>

void **set_item_icon** ( idx: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_icon)

Sets the icon of the item at index `idx`.

---

<span id="class_OptionButton_method_set_item_id"></span>

void **set_item_id** ( idx: [int](class_int.md#class_int), id: [int](class_int.md#class_int) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_id)

Sets the ID of the item at index `idx`.

---

<span id="class_OptionButton_method_set_item_metadata"></span>

void **set_item_metadata** ( idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_metadata)

Sets the metadata of an item. Metadata may be of any type and can be used to store extra information about an item, such as an external string ID.

---

<span id="class_OptionButton_method_set_item_text"></span>

void **set_item_text** ( idx: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_text)

Sets the text of the item at index `idx`.

---

<span id="class_OptionButton_method_set_item_tooltip"></span>

void **set_item_tooltip** ( idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_optionbutton.md#class_OptionButton_method_set_item_tooltip)

Sets the tooltip of the item at index `idx`.

---

<span id="class_OptionButton_method_show_popup"></span>

void **show_popup** ( ) [🔗](class_optionbutton.md#class_OptionButton_method_show_popup)

Adjusts popup position and sizing for the **OptionButton**, then shows the [PopupMenu](class_popupmenu.md#class_PopupMenu). Prefer this over using `get_popup().popup()`.

---

### Theme Property Descriptions

<span id="class_OptionButton_theme_constant_arrow_margin"></span>

[int](class_int.md#class_int) **arrow_margin** = `4` [🔗](class_optionbutton.md#class_OptionButton_theme_constant_arrow_margin)

The horizontal space between the arrow icon and the right edge of the button.

---

<span id="class_OptionButton_theme_constant_modulate_arrow"></span>

[int](class_int.md#class_int) **modulate_arrow** = `0` [🔗](class_optionbutton.md#class_OptionButton_theme_constant_modulate_arrow)

If different than `0`, the arrow icon will be modulated to the font color.

---

<span id="class_OptionButton_theme_icon_arrow"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **arrow** [🔗](class_optionbutton.md#class_OptionButton_theme_icon_arrow)

The arrow icon to be drawn on the right end of the button.
