<span id="class_EditorSelection"></span>

## EditorSelection

**Inherits:** [Object](class_object.md#class_Object)

Manages the SceneTree selection in the editor.

### Description

This object manages the SceneTree selection in the editor.

 **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_selection()](class_editorinterface.md#class_EditorInterface_method_get_selection).

### Methods


| void | [add_node](class_editorselection.md#class_EditorSelection_method_add_node) ( node: [Node](class_node.md#class_Node) ) |
| --- | --- |
| void | [clear](class_editorselection.md#class_EditorSelection_method_clear) ( ) |
| [Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] | [get_selected_nodes](class_editorselection.md#class_EditorSelection_method_get_selected_nodes) ( ) |
| [Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] | [get_top_selected_nodes](class_editorselection.md#class_EditorSelection_method_get_top_selected_nodes) ( ) |
| [Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] | [get_transformable_selected_nodes](class_editorselection.md#class_EditorSelection_method_get_transformable_selected_nodes) ( ) |
| void | [remove_node](class_editorselection.md#class_EditorSelection_method_remove_node) ( node: [Node](class_node.md#class_Node) ) |

---

### Signals

<span id="class_EditorSelection_signal_selection_changed"></span>

**selection_changed** ( ) [🔗](class_editorselection.md#class_EditorSelection_signal_selection_changed)

Emitted when the selection changes.

---

### Method Descriptions

<span id="class_EditorSelection_method_add_node"></span>

void **add_node** ( node: [Node](class_node.md#class_Node) ) [🔗](class_editorselection.md#class_EditorSelection_method_add_node)

Adds a node to the selection.

 **Note:** The newly selected node will not be automatically edited in the inspector. If you want to edit a node, use [EditorInterface.edit_node()](class_editorinterface.md#class_EditorInterface_method_edit_node).

---

<span id="class_EditorSelection_method_clear"></span>

void **clear** ( ) [🔗](class_editorselection.md#class_EditorSelection_method_clear)

Clear the selection.

---

<span id="class_EditorSelection_method_get_selected_nodes"></span>

[Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] **get_selected_nodes** ( ) [🔗](class_editorselection.md#class_EditorSelection_method_get_selected_nodes)

Returns the list of selected nodes.

---

<span id="class_EditorSelection_method_get_top_selected_nodes"></span>

[Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] **get_top_selected_nodes** ( ) [🔗](class_editorselection.md#class_EditorSelection_method_get_top_selected_nodes)

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.).

For example, if there is a node A with a child B and a sibling C, then selecting all three will cause this method to return only A and C. Changing the global transform of A will affect the global transform of B, so there is no need to change B separately.

---

<span id="class_EditorSelection_method_get_transformable_selected_nodes"></span>

[Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] **get_transformable_selected_nodes** ( ) [🔗](class_editorselection.md#class_EditorSelection_method_get_transformable_selected_nodes)

**Deprecated:** Use [get_top_selected_nodes()](class_editorselection.md#class_EditorSelection_method_get_top_selected_nodes) instead.

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.). See [get_top_selected_nodes()](class_editorselection.md#class_EditorSelection_method_get_top_selected_nodes).

---

<span id="class_EditorSelection_method_remove_node"></span>

void **remove_node** ( node: [Node](class_node.md#class_Node) ) [🔗](class_editorselection.md#class_EditorSelection_method_remove_node)

Removes a node from the selection.
