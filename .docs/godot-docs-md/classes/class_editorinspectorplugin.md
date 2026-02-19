<span id="class_EditorInspectorPlugin"></span>

## EditorInspectorPlugin

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plugin for adding custom property editors on the inspector.

### Description

**EditorInspectorPlugin** allows adding custom property editors to [EditorInspector](class_editorinspector.md#class_EditorInspector).

When an object is edited, the [_can_handle()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__can_handle) function is called and must return `true` if the object type is supported.

If supported, the function [_parse_begin()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_begin) will be called, allowing to place custom controls at the beginning of the class.

Subsequently, the [_parse_category()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_category) and [_parse_property()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_property) are called for every category and property. They offer the ability to add custom controls to the inspector too.

Finally, [_parse_end()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_end) will be called.

On each of these calls, the "add" functions can be called.

To use **EditorInspectorPlugin**, register it using the [EditorPlugin.add_inspector_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin) method first.

### Tutorials

- [Inspector plugins](../tutorials/plugins/editor/inspector_plugins.md)

### Methods


| [bool](class_bool.md#class_bool) | [_can_handle](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__can_handle) ( object: [Object](class_object.md#class_Object) ) | virtual | const |
| --- | --- | --- | --- |
| void | [_parse_begin](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_begin) ( object: [Object](class_object.md#class_Object) ) virtual |
| void | [_parse_category](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_category) ( object: [Object](class_object.md#class_Object), category: [String](class_string.md#class_String) ) virtual |
| void | [_parse_end](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_end) ( object: [Object](class_object.md#class_Object) ) virtual |
| void | [_parse_group](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_group) ( object: [Object](class_object.md#class_Object), group: [String](class_string.md#class_String) ) virtual |
| [bool](class_bool.md#class_bool) | [_parse_property](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_property) ( object: [Object](class_object.md#class_Object), type: Variant.Type, name: [String](class_string.md#class_String), hint_type: PropertyHint, hint_string: [String](class_string.md#class_String), usage_flags: | bitfield | \[PropertyUsageFlags\], wide: [bool](class_bool.md#class_bool) ) | virtual |
| void | [add_custom_control](class_editorinspectorplugin.md#class_EditorInspectorPlugin_method_add_custom_control) ( control: [Control](class_control.md#class_Control) ) |
| void | [add_property_editor](class_editorinspectorplugin.md#class_EditorInspectorPlugin_method_add_property_editor) ( property: [String](class_string.md#class_String), editor: [Control](class_control.md#class_Control), add_to_end: [bool](class_bool.md#class_bool) = false, label: [String](class_string.md#class_String) = "" ) |
| void | [add_property_editor_for_multiple_properties](class_editorinspectorplugin.md#class_EditorInspectorPlugin_method_add_property_editor_for_multiple_properties) ( label: [String](class_string.md#class_String), properties: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), editor: [Control](class_control.md#class_Control) ) |

---

### Method Descriptions

<span id="class_EditorInspectorPlugin_private_method__can_handle"></span>

[bool](class_bool.md#class_bool) **_can_handle** ( object: [Object](class_object.md#class_Object) ) *virtual* *const* [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__can_handle)

Returns `true` if this object can be handled by this plugin.

---

<span id="class_EditorInspectorPlugin_private_method__parse_begin"></span>

void **_parse_begin** ( object: [Object](class_object.md#class_Object) ) *virtual* [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_begin)

Called to allow adding controls at the beginning of the property list for `object`.

---

<span id="class_EditorInspectorPlugin_private_method__parse_category"></span>

void **_parse_category** ( object: [Object](class_object.md#class_Object), category: [String](class_string.md#class_String) ) *virtual* [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_category)

Called to allow adding controls at the beginning of a category in the property list for `object`.

---

<span id="class_EditorInspectorPlugin_private_method__parse_end"></span>

void **_parse_end** ( object: [Object](class_object.md#class_Object) ) *virtual* [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_end)

Called to allow adding controls at the end of the property list for `object`.

---

<span id="class_EditorInspectorPlugin_private_method__parse_group"></span>

void **_parse_group** ( object: [Object](class_object.md#class_Object), group: [String](class_string.md#class_String) ) *virtual* [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_group)

Called to allow adding controls at the beginning of a group or a sub-group in the property list for `object`.

---

<span id="class_EditorInspectorPlugin_private_method__parse_property"></span>

[bool](class_bool.md#class_bool) **_parse_property** ( object: [Object](class_object.md#class_Object), type: Variant.Type, name: [String](class_string.md#class_String), hint_type: PropertyHint, hint_string: [String](class_string.md#class_String), usage_flags: *BitField*\[PropertyUsageFlags\], wide: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_property)

Called to allow adding property-specific editors to the property list for `object`. The added editor control must extend [EditorProperty](class_editorproperty.md#class_EditorProperty). Returning `true` removes the built-in editor for this property, otherwise allows to insert a custom editor before the built-in one.

---

<span id="class_EditorInspectorPlugin_method_add_custom_control"></span>

void **add_custom_control** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_method_add_custom_control)

Adds a custom control, which is not necessarily a property editor.

---

<span id="class_EditorInspectorPlugin_method_add_property_editor"></span>

void **add_property_editor** ( property: [String](class_string.md#class_String), editor: [Control](class_control.md#class_Control), add_to_end: [bool](class_bool.md#class_bool) = false, label: [String](class_string.md#class_String) = "" ) [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_method_add_property_editor)

Adds a property editor for an individual property. The `editor` control must extend [EditorProperty](class_editorproperty.md#class_EditorProperty).

There can be multiple property editors for a property. If `add_to_end` is `true`, this newly added editor will be displayed after all the other editors of the property whose `add_to_end` is `false`. For example, the editor uses this parameter to add an "Edit Region" button for [Sprite2D.region_rect](class_sprite2d.md#class_Sprite2D_property_region_rect) below the regular [Rect2](class_rect2.md#class_Rect2) editor.

 `label` can be used to choose a custom label for the property editor in the inspector. If left empty, the label is computed from the name of the property instead.

---

<span id="class_EditorInspectorPlugin_method_add_property_editor_for_multiple_properties"></span>

void **add_property_editor_for_multiple_properties** ( label: [String](class_string.md#class_String), properties: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), editor: [Control](class_control.md#class_Control) ) [🔗](class_editorinspectorplugin.md#class_EditorInspectorPlugin_method_add_property_editor_for_multiple_properties)

Adds an editor that allows modifying multiple properties. The `editor` control must extend [EditorProperty](class_editorproperty.md#class_EditorProperty).
