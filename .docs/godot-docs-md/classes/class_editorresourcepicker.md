<span id="class_EditorResourcePicker"></span>

## EditorResourcePicker

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) **<** [BoxContainer](class_boxcontainer.md#class_BoxContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorScriptPicker](class_editorscriptpicker.md#class_EditorScriptPicker)

Godot editor's control for selecting [Resource](class_resource.md#class_Resource) type properties.

### Description

This [Control](class_control.md#class_Control) node is used in the editor's Inspector dock to allow editing of [Resource](class_resource.md#class_Resource) type properties. It provides options for creating, loading, saving and converting resources. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) to recreate the same behavior.

 **Note:** This [Control](class_control.md#class_Control) does not include any editor for the resource, as editing is controlled by the Inspector dock itself or sub-Inspectors.

### Properties


| [String](class_string.md#class_String) | [base_type](class_editorresourcepicker.md#class_EditorResourcePicker_property_base_type) | `""` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [editable](class_editorresourcepicker.md#class_EditorResourcePicker_property_editable) | `true` |
| [Resource](class_resource.md#class_Resource) | [edited_resource](class_editorresourcepicker.md#class_EditorResourcePicker_property_edited_resource) |
| [bool](class_bool.md#class_bool) | [toggle_mode](class_editorresourcepicker.md#class_EditorResourcePicker_property_toggle_mode) | `false` |

### Methods


| [bool](class_bool.md#class_bool) | [_handle_menu_selected](class_editorresourcepicker.md#class_EditorResourcePicker_private_method__handle_menu_selected) ( id: [int](class_int.md#class_int) ) virtual |
| --- | --- |
| void | [_set_create_options](class_editorresourcepicker.md#class_EditorResourcePicker_private_method__set_create_options) ( menu_node: [Object](class_object.md#class_Object) ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_allowed_types](class_editorresourcepicker.md#class_EditorResourcePicker_method_get_allowed_types) ( ) const |
| void | [set_toggle_pressed](class_editorresourcepicker.md#class_EditorResourcePicker_method_set_toggle_pressed) ( pressed: [bool](class_bool.md#class_bool) ) |

---

### Signals

<span id="class_EditorResourcePicker_signal_resource_changed"></span>

**resource_changed** ( resource: [Resource](class_resource.md#class_Resource) ) [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_signal_resource_changed)

Emitted when the value of the edited resource was changed.

---

<span id="class_EditorResourcePicker_signal_resource_selected"></span>

**resource_selected** ( resource: [Resource](class_resource.md#class_Resource), inspect: [bool](class_bool.md#class_bool) ) [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_signal_resource_selected)

Emitted when the resource value was set and user clicked to edit it. When `inspect` is `true`, the signal was caused by the context menu "Edit" or "Inspect" option.

---

### Property Descriptions

<span id="class_EditorResourcePicker_property_base_type"></span>

[String](class_string.md#class_String) **base_type** = `""` [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_property_base_type)

- void **set_base_type** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_base_type** ( )

The base type of allowed resource types. Can be a comma-separated list of several options.

---

<span id="class_EditorResourcePicker_property_editable"></span>

[bool](class_bool.md#class_bool) **editable** = `true` [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_property_editable)

- void **set_editable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editable** ( )

If `true`, the value can be selected and edited.

---

<span id="class_EditorResourcePicker_property_edited_resource"></span>

[Resource](class_resource.md#class_Resource) **edited_resource** [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_property_edited_resource)

- void **set_edited_resource** ( value: [Resource](class_resource.md#class_Resource) )
- [Resource](class_resource.md#class_Resource) **get_edited_resource** ( )

The edited resource value.

---

<span id="class_EditorResourcePicker_property_toggle_mode"></span>

[bool](class_bool.md#class_bool) **toggle_mode** = `false` [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_property_toggle_mode)

- void **set_toggle_mode** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_toggle_mode** ( )

If `true`, the main button with the resource preview works in the toggle mode. Use [set_toggle_pressed()](class_editorresourcepicker.md#class_EditorResourcePicker_method_set_toggle_pressed) to manually set the state.

---

### Method Descriptions

<span id="class_EditorResourcePicker_private_method__handle_menu_selected"></span>

[bool](class_bool.md#class_bool) **_handle_menu_selected** ( id: [int](class_int.md#class_int) ) *virtual* [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_private_method__handle_menu_selected)

This virtual method can be implemented to handle context menu items not handled by default. See [_set_create_options()](class_editorresourcepicker.md#class_EditorResourcePicker_private_method__set_create_options).

---

<span id="class_EditorResourcePicker_private_method__set_create_options"></span>

void **_set_create_options** ( menu_node: [Object](class_object.md#class_Object) ) *virtual* [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_private_method__set_create_options)

This virtual method is called when updating the context menu of **EditorResourcePicker**. Implement this method to override the "New ..." items with your own options. `menu_node` is a reference to the [PopupMenu](class_popupmenu.md#class_PopupMenu) node.

 **Note:** Implement [_handle_menu_selected()](class_editorresourcepicker.md#class_EditorResourcePicker_private_method__handle_menu_selected) to handle these custom items.

---

<span id="class_EditorResourcePicker_method_get_allowed_types"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_allowed_types** ( ) *const* [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_method_get_allowed_types)

Returns a list of all allowed types and subtypes corresponding to the [base_type](class_editorresourcepicker.md#class_EditorResourcePicker_property_base_type). If the [base_type](class_editorresourcepicker.md#class_EditorResourcePicker_property_base_type) is empty, an empty list is returned.

---

<span id="class_EditorResourcePicker_method_set_toggle_pressed"></span>

void **set_toggle_pressed** ( pressed: [bool](class_bool.md#class_bool) ) [🔗](class_editorresourcepicker.md#class_EditorResourcePicker_method_set_toggle_pressed)

Sets the toggle mode state for the main button. Works only if [toggle_mode](class_editorresourcepicker.md#class_EditorResourcePicker_property_toggle_mode) is set to `true`.
