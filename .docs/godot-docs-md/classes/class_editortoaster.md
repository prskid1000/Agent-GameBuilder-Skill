<span id="class_EditorToaster"></span>

## EditorToaster

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) **<** [BoxContainer](class_boxcontainer.md#class_BoxContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Manages toast notifications within the editor.

### Description

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

 **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_editor_toaster()](class_editorinterface.md#class_EditorInterface_method_get_editor_toaster).

### Methods


| void | [push_toast](class_editortoaster.md#class_EditorToaster_method_push_toast) ( message: [String](class_string.md#class_String), severity: [Severity](class_editortoaster.md#enum_EditorToaster_Severity) = 0, tooltip: [String](class_string.md#class_String) = "" ) |
| --- | --- |

---

### Enumerations

<span id="enum_EditorToaster_Severity"></span>

enum **Severity**: [🔗](class_editortoaster.md#enum_EditorToaster_Severity)

<span id="class_EditorToaster_constant_SEVERITY_INFO"></span>

[Severity](class_editortoaster.md#enum_EditorToaster_Severity) **SEVERITY_INFO** = `0`

Toast will display with an INFO severity.

<span id="class_EditorToaster_constant_SEVERITY_WARNING"></span>

[Severity](class_editortoaster.md#enum_EditorToaster_Severity) **SEVERITY_WARNING** = `1`

Toast will display with a WARNING severity and have a corresponding color.

<span id="class_EditorToaster_constant_SEVERITY_ERROR"></span>

[Severity](class_editortoaster.md#enum_EditorToaster_Severity) **SEVERITY_ERROR** = `2`

Toast will display with an ERROR severity and have a corresponding color.

---

### Method Descriptions

<span id="class_EditorToaster_method_push_toast"></span>

void **push_toast** ( message: [String](class_string.md#class_String), severity: [Severity](class_editortoaster.md#enum_EditorToaster_Severity) = 0, tooltip: [String](class_string.md#class_String) = "" ) [🔗](class_editortoaster.md#class_EditorToaster_method_push_toast)

Pushes a toast notification to the editor for display.
