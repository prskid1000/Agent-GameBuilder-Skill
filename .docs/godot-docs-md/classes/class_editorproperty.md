<span id="class_EditorProperty"></span>

## EditorProperty

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Custom control for editing properties that can be added to the [EditorInspector](class_editorinspector.md#class_EditorInspector).

### Description

A custom control for editing properties that can be added to the [EditorInspector](class_editorinspector.md#class_EditorInspector). It is added via [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin).

### Properties


| [bool](class_bool.md#class_bool) | [checkable](class_editorproperty.md#class_EditorProperty_property_checkable) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [checked](class_editorproperty.md#class_EditorProperty_property_checked) | `false` |
| [bool](class_bool.md#class_bool) | [deletable](class_editorproperty.md#class_EditorProperty_property_deletable) | `false` |
| [bool](class_bool.md#class_bool) | [draw_background](class_editorproperty.md#class_EditorProperty_property_draw_background) | `true` |
| [bool](class_bool.md#class_bool) | [draw_label](class_editorproperty.md#class_EditorProperty_property_draw_label) | `true` |
| [bool](class_bool.md#class_bool) | [draw_warning](class_editorproperty.md#class_EditorProperty_property_draw_warning) | `false` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `3` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [bool](class_bool.md#class_bool) | [keying](class_editorproperty.md#class_EditorProperty_property_keying) | `false` |
| [String](class_string.md#class_String) | [label](class_editorproperty.md#class_EditorProperty_property_label) | `""` |
| [float](class_float.md#class_float) | [name_split_ratio](class_editorproperty.md#class_EditorProperty_property_name_split_ratio) | `0.5` |
| [bool](class_bool.md#class_bool) | [read_only](class_editorproperty.md#class_EditorProperty_property_read_only) | `false` |
| [bool](class_bool.md#class_bool) | [selectable](class_editorproperty.md#class_EditorProperty_property_selectable) | `true` |
| [bool](class_bool.md#class_bool) | [use_folding](class_editorproperty.md#class_EditorProperty_property_use_folding) | `false` |

### Methods


| void | [_set_read_only](class_editorproperty.md#class_EditorProperty_private_method__set_read_only) ( read_only: [bool](class_bool.md#class_bool) ) virtual |
| --- | --- |
| void | [_update_property](class_editorproperty.md#class_EditorProperty_private_method__update_property) ( ) virtual |
| void | [add_focusable](class_editorproperty.md#class_EditorProperty_method_add_focusable) ( control: [Control](class_control.md#class_Control) ) |
| void | [deselect](class_editorproperty.md#class_EditorProperty_method_deselect) ( ) |
| void | [emit_changed](class_editorproperty.md#class_EditorProperty_method_emit_changed) ( property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant), field: [StringName](class_stringname.md#class_StringName) = &"", changing: [bool](class_bool.md#class_bool) = false ) |
| [Object](class_object.md#class_Object) | [get_edited_object](class_editorproperty.md#class_EditorProperty_method_get_edited_object) ( ) |
| [StringName](class_stringname.md#class_StringName) | [get_edited_property](class_editorproperty.md#class_EditorProperty_method_get_edited_property) ( ) const |
| [bool](class_bool.md#class_bool) | [is_selected](class_editorproperty.md#class_EditorProperty_method_is_selected) ( ) const |
| void | [select](class_editorproperty.md#class_EditorProperty_method_select) ( focusable: [int](class_int.md#class_int) = -1 ) |
| void | [set_bottom_editor](class_editorproperty.md#class_EditorProperty_method_set_bottom_editor) ( editor: [Control](class_control.md#class_Control) ) |
| void | [set_label_reference](class_editorproperty.md#class_EditorProperty_method_set_label_reference) ( control: [Control](class_control.md#class_Control) ) |
| void | [set_object_and_property](class_editorproperty.md#class_EditorProperty_method_set_object_and_property) ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName) ) |
| void | [update_property](class_editorproperty.md#class_EditorProperty_method_update_property) ( ) |

---

### Signals

<span id="class_EditorProperty_signal_multiple_properties_changed"></span>

**multiple_properties_changed** ( properties: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), value: [Array](class_array.md#class_Array) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_multiple_properties_changed)

Emit it if you want multiple properties modified at the same time. Do not use if added via [EditorInspectorPlugin._parse_property()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_property).

---

<span id="class_EditorProperty_signal_object_id_selected"></span>

**object_id_selected** ( property: [StringName](class_stringname.md#class_StringName), id: [int](class_int.md#class_int) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_object_id_selected)

Used by sub-inspectors. Emit it if what was selected was an Object ID.

---

<span id="class_EditorProperty_signal_property_can_revert_changed"></span>

**property_can_revert_changed** ( property: [StringName](class_stringname.md#class_StringName), can_revert: [bool](class_bool.md#class_bool) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_can_revert_changed)

Emitted when the revertability (i.e., whether it has a non-default value and thus is displayed with a revert icon) of a property has changed.

---

<span id="class_EditorProperty_signal_property_changed"></span>

**property_changed** ( property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant), field: [StringName](class_stringname.md#class_StringName), changing: [bool](class_bool.md#class_bool) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_changed)

Do not emit this manually, use the [emit_changed()](class_editorproperty.md#class_EditorProperty_method_emit_changed) method instead.

---

<span id="class_EditorProperty_signal_property_checked"></span>

**property_checked** ( property: [StringName](class_stringname.md#class_StringName), checked: [bool](class_bool.md#class_bool) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_checked)

Emitted when a property was checked. Used internally.

---

<span id="class_EditorProperty_signal_property_deleted"></span>

**property_deleted** ( property: [StringName](class_stringname.md#class_StringName) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_deleted)

Emitted when a property was deleted. Used internally.

---

<span id="class_EditorProperty_signal_property_favorited"></span>

**property_favorited** ( property: [StringName](class_stringname.md#class_StringName), favorited: [bool](class_bool.md#class_bool) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_favorited)

Emit it if you want to mark a property as favorited, making it appear at the top of the inspector.

---

<span id="class_EditorProperty_signal_property_keyed"></span>

**property_keyed** ( property: [StringName](class_stringname.md#class_StringName) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_keyed)

Emit it if you want to add this value as an animation key (check for keying being enabled first).

---

<span id="class_EditorProperty_signal_property_keyed_with_value"></span>

**property_keyed_with_value** ( property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_keyed_with_value)

Emit it if you want to key a property with a single value.

---

<span id="class_EditorProperty_signal_property_overridden"></span>

**property_overridden** ( ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_overridden)

Emitted when a setting override for the current project is requested.

---

<span id="class_EditorProperty_signal_property_pinned"></span>

**property_pinned** ( property: [StringName](class_stringname.md#class_StringName), pinned: [bool](class_bool.md#class_bool) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_property_pinned)

Emit it if you want to mark (or unmark) the value of a property for being saved regardless of being equal to the default value.

The default value is the one the property will get when the node is just instantiated and can come from an ancestor scene in the inheritance/instantiation chain, a script or a builtin class.

---

<span id="class_EditorProperty_signal_resource_selected"></span>

**resource_selected** ( path: [String](class_string.md#class_String), resource: [Resource](class_resource.md#class_Resource) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_resource_selected)

If you want a sub-resource to be edited, emit this signal with the resource.

---

<span id="class_EditorProperty_signal_selected"></span>

**selected** ( path: [String](class_string.md#class_String), focusable_idx: [int](class_int.md#class_int) ) [🔗](class_editorproperty.md#class_EditorProperty_signal_selected)

Emitted when selected. Used internally.

---

### Property Descriptions

<span id="class_EditorProperty_property_checkable"></span>

[bool](class_bool.md#class_bool) **checkable** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_checkable)

- void **set_checkable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_checkable** ( )

Used by the inspector, set to `true` when the property is checkable.

---

<span id="class_EditorProperty_property_checked"></span>

[bool](class_bool.md#class_bool) **checked** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_checked)

- void **set_checked** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_checked** ( )

Used by the inspector, set to `true` when the property is checked.

---

<span id="class_EditorProperty_property_deletable"></span>

[bool](class_bool.md#class_bool) **deletable** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_deletable)

- void **set_deletable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_deletable** ( )

Used by the inspector, set to `true` when the property can be deleted by the user.

---

<span id="class_EditorProperty_property_draw_background"></span>

[bool](class_bool.md#class_bool) **draw_background** = `true` [🔗](class_editorproperty.md#class_EditorProperty_property_draw_background)

- void **set_draw_background** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_background** ( )

Used by the inspector, set to `true` when the property background is drawn.

---

<span id="class_EditorProperty_property_draw_label"></span>

[bool](class_bool.md#class_bool) **draw_label** = `true` [🔗](class_editorproperty.md#class_EditorProperty_property_draw_label)

- void **set_draw_label** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_label** ( )

Used by the inspector, set to `true` when the property label is drawn.

---

<span id="class_EditorProperty_property_draw_warning"></span>

[bool](class_bool.md#class_bool) **draw_warning** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_draw_warning)

- void **set_draw_warning** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_warning** ( )

Used by the inspector, set to `true` when the property is drawn with the editor theme's warning color. This is used for editable children's properties.

---

<span id="class_EditorProperty_property_keying"></span>

[bool](class_bool.md#class_bool) **keying** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_keying)

- void **set_keying** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_keying** ( )

Used by the inspector, set to `true` when the property can add keys for animation.

---

<span id="class_EditorProperty_property_label"></span>

[String](class_string.md#class_String) **label** = `""` [🔗](class_editorproperty.md#class_EditorProperty_property_label)

- void **set_label** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_label** ( )

Set this property to change the label (if you want to show one).

---

<span id="class_EditorProperty_property_name_split_ratio"></span>

[float](class_float.md#class_float) **name_split_ratio** = `0.5` [🔗](class_editorproperty.md#class_EditorProperty_property_name_split_ratio)

- void **set_name_split_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_name_split_ratio** ( )

Space distribution ratio between the label and the editing field.

---

<span id="class_EditorProperty_property_read_only"></span>

[bool](class_bool.md#class_bool) **read_only** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_read_only)

- void **set_read_only** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_read_only** ( )

Used by the inspector, set to `true` when the property is read-only.

---

<span id="class_EditorProperty_property_selectable"></span>

[bool](class_bool.md#class_bool) **selectable** = `true` [🔗](class_editorproperty.md#class_EditorProperty_property_selectable)

- void **set_selectable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_selectable** ( )

Used by the inspector, set to `true` when the property is selectable.

---

<span id="class_EditorProperty_property_use_folding"></span>

[bool](class_bool.md#class_bool) **use_folding** = `false` [🔗](class_editorproperty.md#class_EditorProperty_property_use_folding)

- void **set_use_folding** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_folding** ( )

Used by the inspector, set to `true` when the property is using folding.

---

### Method Descriptions

<span id="class_EditorProperty_private_method__set_read_only"></span>

void **_set_read_only** ( read_only: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_editorproperty.md#class_EditorProperty_private_method__set_read_only)

Called when the read-only status of the property is changed. It may be used to change custom controls into a read-only or modifiable state.

---

<span id="class_EditorProperty_private_method__update_property"></span>

void **_update_property** ( ) *virtual* [🔗](class_editorproperty.md#class_EditorProperty_private_method__update_property)

When this virtual function is called, you must update your editor.

---

<span id="class_EditorProperty_method_add_focusable"></span>

void **add_focusable** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editorproperty.md#class_EditorProperty_method_add_focusable)

If any of the controls added can gain keyboard focus, add it here. This ensures that focus will be restored if the inspector is refreshed.

---

<span id="class_EditorProperty_method_deselect"></span>

void **deselect** ( ) [🔗](class_editorproperty.md#class_EditorProperty_method_deselect)

Draw property as not selected. Used by the inspector.

---

<span id="class_EditorProperty_method_emit_changed"></span>

void **emit_changed** ( property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant), field: [StringName](class_stringname.md#class_StringName) = &"", changing: [bool](class_bool.md#class_bool) = false ) [🔗](class_editorproperty.md#class_EditorProperty_method_emit_changed)

If one or several properties have changed, this must be called. `field` is used in case your editor can modify fields separately (as an example, Vector3.x). The `changing` argument avoids the editor requesting this property to be refreshed (leave as `false` if unsure).

---

<span id="class_EditorProperty_method_get_edited_object"></span>

[Object](class_object.md#class_Object) **get_edited_object** ( ) [🔗](class_editorproperty.md#class_EditorProperty_method_get_edited_object)

Returns the edited object.

 **Note:** This method could return `null` if the editor has not yet been associated with a property. However, in [_update_property()](class_editorproperty.md#class_EditorProperty_private_method__update_property) and [_set_read_only()](class_editorproperty.md#class_EditorProperty_private_method__set_read_only), this value is *guaranteed* to be non-`null`.

---

<span id="class_EditorProperty_method_get_edited_property"></span>

[StringName](class_stringname.md#class_StringName) **get_edited_property** ( ) *const* [🔗](class_editorproperty.md#class_EditorProperty_method_get_edited_property)

Returns the edited property. If your editor is for a single property (added via [EditorInspectorPlugin._parse_property()](class_editorinspectorplugin.md#class_EditorInspectorPlugin_private_method__parse_property)), then this will return the property.

 **Note:** This method could return `null` if the editor has not yet been associated with a property. However, in [_update_property()](class_editorproperty.md#class_EditorProperty_private_method__update_property) and [_set_read_only()](class_editorproperty.md#class_EditorProperty_private_method__set_read_only), this value is *guaranteed* to be non-`null`.

---

<span id="class_EditorProperty_method_is_selected"></span>

[bool](class_bool.md#class_bool) **is_selected** ( ) *const* [🔗](class_editorproperty.md#class_EditorProperty_method_is_selected)

Returns `true` if property is drawn as selected. Used by the inspector.

---

<span id="class_EditorProperty_method_select"></span>

void **select** ( focusable: [int](class_int.md#class_int) = -1 ) [🔗](class_editorproperty.md#class_EditorProperty_method_select)

Draw property as selected. Used by the inspector.

---

<span id="class_EditorProperty_method_set_bottom_editor"></span>

void **set_bottom_editor** ( editor: [Control](class_control.md#class_Control) ) [🔗](class_editorproperty.md#class_EditorProperty_method_set_bottom_editor)

Puts the `editor` control below the property label. The control must be previously added using [Node.add_child()](class_node.md#class_Node_method_add_child).

---

<span id="class_EditorProperty_method_set_label_reference"></span>

void **set_label_reference** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editorproperty.md#class_EditorProperty_method_set_label_reference)

Used by the inspector, set to a control that will be used as a reference to calculate the size of the label.

---

<span id="class_EditorProperty_method_set_object_and_property"></span>

void **set_object_and_property** ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName) ) [🔗](class_editorproperty.md#class_EditorProperty_method_set_object_and_property)

Assigns object and property to edit.

---

<span id="class_EditorProperty_method_update_property"></span>

void **update_property** ( ) [🔗](class_editorproperty.md#class_EditorProperty_method_update_property)

Forces a refresh of the property display.
