<span id="class_EditorScriptPicker"></span>

## EditorScriptPicker

**Inherits:** [EditorResourcePicker](class_editorresourcepicker.md#class_EditorResourcePicker) **<** [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) **<** [BoxContainer](class_boxcontainer.md#class_BoxContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Godot editor's control for selecting the `script` property of a [Node](class_node.md#class_Node).

### Description

Similar to [EditorResourcePicker](class_editorresourcepicker.md#class_EditorResourcePicker) this [Control](class_control.md#class_Control) node is used in the editor's Inspector dock, but only to edit the `script` property of a [Node](class_node.md#class_Node). Default options for creating new resources of all possible subtypes are replaced with dedicated buttons that open the "Attach Node Script" dialog. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) to recreate the same behavior.

 **Note:** You must set the [script_owner](class_editorscriptpicker.md#class_EditorScriptPicker_property_script_owner) for the custom context menu items to work.

### Properties


| [Node](class_node.md#class_Node) | [script_owner](class_editorscriptpicker.md#class_EditorScriptPicker_property_script_owner) |
| --- | --- |

---

### Property Descriptions

<span id="class_EditorScriptPicker_property_script_owner"></span>

[Node](class_node.md#class_Node) **script_owner** [🔗](class_editorscriptpicker.md#class_EditorScriptPicker_property_script_owner)

- void **set_script_owner** ( value: [Node](class_node.md#class_Node) )
- [Node](class_node.md#class_Node) **get_script_owner** ( )

The owner [Node](class_node.md#class_Node) of the script property that holds the edited resource.
