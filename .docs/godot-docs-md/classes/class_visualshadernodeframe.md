<span id="class_VisualShaderNodeFrame"></span>

## VisualShaderNodeFrame

**Inherits:** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeComment](class_visualshadernodecomment.md#class_VisualShaderNodeComment)

A frame other visual shader nodes can be attached to for better organization.

### Description

A rectangular frame that can be used to group visual shader nodes together to improve organization.

Nodes attached to the frame will move with it when it is dragged and it can automatically resize to enclose all attached nodes.

Its title, description and color can be customized.

### Properties


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [attached_nodes](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_attached_nodes) | `PackedInt32Array()` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [autoshrink](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_autoshrink) | `true` |
| [Color](class_color.md#class_Color) | [tint_color](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_tint_color) | `Color(0.3, 0.3, 0.3, 0.75)` |
| [bool](class_bool.md#class_bool) | [tint_color_enabled](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_tint_color_enabled) | `false` |
| [String](class_string.md#class_String) | [title](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_title) | `"Title"` |

### Methods


| void | [add_attached_node](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_method_add_attached_node) ( node: [int](class_int.md#class_int) ) |
| --- | --- |
| void | [remove_attached_node](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_method_remove_attached_node) ( node: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_VisualShaderNodeFrame_property_attached_nodes"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **attached_nodes** = `PackedInt32Array()` [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_attached_nodes)

- void **set_attached_nodes** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_attached_nodes** ( )

The list of nodes attached to the frame.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_VisualShaderNodeFrame_property_autoshrink"></span>

[bool](class_bool.md#class_bool) **autoshrink** = `true` [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_autoshrink)

- void **set_autoshrink_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_autoshrink_enabled** ( )

If `true`, the frame will automatically resize to enclose all attached nodes.

---

<span id="class_VisualShaderNodeFrame_property_tint_color"></span>

[Color](class_color.md#class_Color) **tint_color** = `Color(0.3, 0.3, 0.3, 0.75)` [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_tint_color)

- void **set_tint_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_tint_color** ( )

The color of the frame when [tint_color_enabled](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_tint_color_enabled) is `true`.

---

<span id="class_VisualShaderNodeFrame_property_tint_color_enabled"></span>

[bool](class_bool.md#class_bool) **tint_color_enabled** = `false` [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_tint_color_enabled)

- void **set_tint_color_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_tint_color_enabled** ( )

If `true`, the frame will be tinted with the color specified in [tint_color](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_tint_color).

---

<span id="class_VisualShaderNodeFrame_property_title"></span>

[String](class_string.md#class_String) **title** = `"Title"` [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_property_title)

- void **set_title** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_title** ( )

The title of the node.

---

### Method Descriptions

<span id="class_VisualShaderNodeFrame_method_add_attached_node"></span>

void **add_attached_node** ( node: [int](class_int.md#class_int) ) [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_method_add_attached_node)

Adds a node to the list of nodes attached to the frame. Should not be called directly, use the [VisualShader.attach_node_to_frame()](class_visualshader.md#class_VisualShader_method_attach_node_to_frame) method instead.

---

<span id="class_VisualShaderNodeFrame_method_remove_attached_node"></span>

void **remove_attached_node** ( node: [int](class_int.md#class_int) ) [🔗](class_visualshadernodeframe.md#class_VisualShaderNodeFrame_method_remove_attached_node)

Removes a node from the list of nodes attached to the frame. Should not be called directly, use the [VisualShader.detach_node_from_frame()](class_visualshader.md#class_VisualShader_method_detach_node_from_frame) method instead.
