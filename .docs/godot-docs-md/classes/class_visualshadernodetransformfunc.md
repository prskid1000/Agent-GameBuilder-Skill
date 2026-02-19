<span id="class_VisualShaderNodeTransformFunc"></span>

## VisualShaderNodeTransformFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Computes a [Transform3D](class_transform3d.md#class_Transform3D) function within the visual shader graph.

### Description

Computes an inverse or transpose function on the provided [Transform3D](class_transform3d.md#class_Transform3D).

### Properties


| [Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) | [function](class_visualshadernodetransformfunc.md#class_VisualShaderNodeTransformFunc_property_function) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeTransformFunc_Function"></span>

enum **Function**: [🔗](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function)

<span id="class_VisualShaderNodeTransformFunc_constant_FUNC_INVERSE"></span>

[Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) **FUNC_INVERSE** = `0`

Perform the inverse operation on the [Transform3D](class_transform3d.md#class_Transform3D) matrix.

<span id="class_VisualShaderNodeTransformFunc_constant_FUNC_TRANSPOSE"></span>

[Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) **FUNC_TRANSPOSE** = `1`

Perform the transpose operation on the [Transform3D](class_transform3d.md#class_Transform3D) matrix.

<span id="class_VisualShaderNodeTransformFunc_constant_FUNC_MAX"></span>

[Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeTransformFunc_property_function"></span>

[Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) **function** = `0` [🔗](class_visualshadernodetransformfunc.md#class_VisualShaderNodeTransformFunc_property_function)

- void **set_function** ( value: [Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) )
- [Function](class_visualshadernodetransformfunc.md#enum_VisualShaderNodeTransformFunc_Function) **get_function** ( )

The function to be computed.
