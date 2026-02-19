.. meta::
	:keywords: dropdown

<span id="class_MenuButton"></span>

## MenuButton

**Inherits:** [Button](class_button.md#class_Button) **<** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A button that brings up a [PopupMenu](class_popupmenu.md#class_PopupMenu) when clicked.

### Description

A button that brings up a [PopupMenu](class_popupmenu.md#class_PopupMenu) when clicked. To create new items inside this [PopupMenu](class_popupmenu.md#class_PopupMenu), use `get_popup().add_item("My Item Name")`. You can also create them directly from Godot editor's inspector.

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

### Properties


| [ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) | action_mode | `0` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_action_mode)) |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | flat | `true` (overrides [Button](class_button.md#class_Button_property_flat)) |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `3` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [int](class_int.md#class_int) | [item_count](class_menubutton.md#class_MenuButton_property_item_count) | `0` |
| [bool](class_bool.md#class_bool) | [switch_on_hover](class_menubutton.md#class_MenuButton_property_switch_on_hover) | `false` |
| [bool](class_bool.md#class_bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_toggle_mode)) |

### Methods


| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_popup](class_menubutton.md#class_MenuButton_method_get_popup) ( ) const |
| --- | --- |
| void | [set_disable_shortcuts](class_menubutton.md#class_MenuButton_method_set_disable_shortcuts) ( disabled: [bool](class_bool.md#class_bool) ) |
| void | [show_popup](class_menubutton.md#class_MenuButton_method_show_popup) ( ) |

---

### Signals

<span id="class_MenuButton_signal_about_to_popup"></span>

**about_to_popup** ( ) [🔗](class_menubutton.md#class_MenuButton_signal_about_to_popup)

Emitted when the [PopupMenu](class_popupmenu.md#class_PopupMenu) of this MenuButton is about to show.

---

### Property Descriptions

<span id="class_MenuButton_property_item_count"></span>

[int](class_int.md#class_int) **item_count** = `0` [🔗](class_menubutton.md#class_MenuButton_property_item_count)

- void **set_item_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_item_count** ( )

The number of items currently in the list.

---

<span id="class_MenuButton_property_switch_on_hover"></span>

[bool](class_bool.md#class_bool) **switch_on_hover** = `false` [🔗](class_menubutton.md#class_MenuButton_property_switch_on_hover)

- void **set_switch_on_hover** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_switch_on_hover** ( )

If `true`, when the cursor hovers above another **MenuButton** within the same parent which also has [switch_on_hover](class_menubutton.md#class_MenuButton_property_switch_on_hover) enabled, it will close the current **MenuButton** and open the other one.

---

### Method Descriptions

<span id="class_MenuButton_method_get_popup"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_popup** ( ) *const* [🔗](class_menubutton.md#class_MenuButton_method_get_popup)

Returns the [PopupMenu](class_popupmenu.md#class_PopupMenu) contained in this button.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

<span id="class_MenuButton_method_set_disable_shortcuts"></span>

void **set_disable_shortcuts** ( disabled: [bool](class_bool.md#class_bool) ) [🔗](class_menubutton.md#class_MenuButton_method_set_disable_shortcuts)

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---

<span id="class_MenuButton_method_show_popup"></span>

void **show_popup** ( ) [🔗](class_menubutton.md#class_MenuButton_method_show_popup)

Adjusts popup position and sizing for the **MenuButton**, then shows the [PopupMenu](class_popupmenu.md#class_PopupMenu). Prefer this over using `get_popup().popup()`.
