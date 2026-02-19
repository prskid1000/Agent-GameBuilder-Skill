<span id="class_VisualShaderNodeVec4Constant"></span>

## VisualShaderNodeVec4Constant

**Inherits:** [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class_VisualShaderNodeConstant) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 4D vector constant to be used within the visual shader graph.

### Description

A constant 4D vector, which can be used as an input node.

### Properties


| [Quaternion](class_quaternion.md#class_Quaternion) | [constant](class_visualshadernodevec4constant.md#class_VisualShaderNodeVec4Constant_property_constant) | `Quaternion(0, 0, 0, 1)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeVec4Constant_property_constant"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **constant** = `Quaternion(0, 0, 0, 1)` [🔗](class_visualshadernodevec4constant.md#class_VisualShaderNodeVec4Constant_property_constant)

- void **set_constant** ( value: [Quaternion](class_quaternion.md#class_Quaternion) )
- [Quaternion](class_quaternion.md#class_Quaternion) **get_constant** ( )

A 4D vector (represented as a [Quaternion](class_quaternion.md#class_Quaternion)) constant which represents the state of this node.
