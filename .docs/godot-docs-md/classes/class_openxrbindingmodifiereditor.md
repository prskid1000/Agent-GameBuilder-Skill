<span id="class_OpenXRBindingModifierEditor"></span>

## OpenXRBindingModifierEditor

**Inherits:** [PanelContainer](class_panelcontainer.md#class_PanelContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Binding modifier editor.

### Description

This is the default binding modifier editor used in the OpenXR action map.

### Properties


| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_horizontal | `3` (overrides [Control](class_control.md#class_Control_property_size_flags_horizontal)) |
| --- | --- | --- | --- |

### Methods


| [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) | [get_binding_modifier](class_openxrbindingmodifiereditor.md#class_OpenXRBindingModifierEditor_method_get_binding_modifier) ( ) const |
| --- | --- |
| void | [setup](class_openxrbindingmodifiereditor.md#class_OpenXRBindingModifierEditor_method_setup) ( action_map: [OpenXRActionMap](class_openxractionmap.md#class_OpenXRActionMap), binding_modifier: [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) ) |

---

### Signals

<span id="class_OpenXRBindingModifierEditor_signal_binding_modifier_removed"></span>

**binding_modifier_removed** ( binding_modifier_editor: [Object](class_object.md#class_Object) ) [🔗](class_openxrbindingmodifiereditor.md#class_OpenXRBindingModifierEditor_signal_binding_modifier_removed)

Signal emitted when the user presses the delete binding modifier button for this modifier.

---

### Method Descriptions

<span id="class_OpenXRBindingModifierEditor_method_get_binding_modifier"></span>

[OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) **get_binding_modifier** ( ) *const* [🔗](class_openxrbindingmodifiereditor.md#class_OpenXRBindingModifierEditor_method_get_binding_modifier)

Returns the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) currently being edited.

---

<span id="class_OpenXRBindingModifierEditor_method_setup"></span>

void **setup** ( action_map: [OpenXRActionMap](class_openxractionmap.md#class_OpenXRActionMap), binding_modifier: [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) ) [🔗](class_openxrbindingmodifiereditor.md#class_OpenXRBindingModifierEditor_method_setup)

Setup this editor for the provided `action_map` and `binding_modifier`.
