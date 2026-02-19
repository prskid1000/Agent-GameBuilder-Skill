<span id="class_VisualShaderNodeExpression"></span>

## VisualShaderNodeExpression

**Inherits:** [VisualShaderNodeGroupBase](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase) **<** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeGlobalExpression](class_visualshadernodeglobalexpression.md#class_VisualShaderNodeGlobalExpression)

A custom visual shader graph expression written in Godot Shading Language.

### Description

Custom Godot Shading Language expression, with a custom number of input and output ports.

The provided code is directly injected into the graph's matching shader function (`vertex`, `fragment`, or `light`), so it cannot be used to declare functions, varyings, uniforms, or global constants. See [VisualShaderNodeGlobalExpression](class_visualshadernodeglobalexpression.md#class_VisualShaderNodeGlobalExpression) for such global definitions.

### Properties


| [String](class_string.md#class_String) | [expression](class_visualshadernodeexpression.md#class_VisualShaderNodeExpression_property_expression) | `""` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeExpression_property_expression"></span>

[String](class_string.md#class_String) **expression** = `""` [🔗](class_visualshadernodeexpression.md#class_VisualShaderNodeExpression_property_expression)

- void **set_expression** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_expression** ( )

An expression in Godot Shading Language, which will be injected at the start of the graph's matching shader function (`vertex`, `fragment`, or `light`), and thus cannot be used to declare functions, varyings, uniforms, or global constants.
