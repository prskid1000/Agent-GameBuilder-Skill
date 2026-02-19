<span id="class_OpenXRInteractionProfileEditorBase"></span>

## OpenXRInteractionProfileEditorBase

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) **<** [BoxContainer](class_boxcontainer.md#class_BoxContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRInteractionProfileEditor](class_openxrinteractionprofileeditor.md#class_OpenXRInteractionProfileEditor)

Base class for editing interaction profiles.

### Description

This is a base class for interaction profile editors used by the OpenXR action map editor. It can be used to create bespoke editors for specific interaction profiles.

### Properties


| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_horizontal | `3` (overrides [Control](class_control.md#class_Control_property_size_flags_horizontal)) |
| --- | --- | --- | --- |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_vertical | `3` (overrides [Control](class_control.md#class_Control_property_size_flags_vertical)) |

### Methods


| void | [setup](class_openxrinteractionprofileeditorbase.md#class_OpenXRInteractionProfileEditorBase_method_setup) ( action_map: [OpenXRActionMap](class_openxractionmap.md#class_OpenXRActionMap), interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) ) |
| --- | --- |

---

### Method Descriptions

<span id="class_OpenXRInteractionProfileEditorBase_method_setup"></span>

void **setup** ( action_map: [OpenXRActionMap](class_openxractionmap.md#class_OpenXRActionMap), interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) ) [🔗](class_openxrinteractionprofileeditorbase.md#class_OpenXRInteractionProfileEditorBase_method_setup)

Setup this editor for the provided `action_map` and `interaction_profile`.
