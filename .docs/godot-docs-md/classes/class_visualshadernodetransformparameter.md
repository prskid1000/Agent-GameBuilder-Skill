<span id="class_VisualShaderNodeTransformParameter"></span>

## VisualShaderNodeTransformParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Transform3D](class_transform3d.md#class_Transform3D) parameter for use within the visual shader graph.

### Description

Translated to `uniform mat4` in the shader language.

### Properties


| [Transform3D](class_transform3d.md#class_Transform3D) | [default_value](class_visualshadernodetransformparameter.md#class_VisualShaderNodeTransformParameter_property_default_value) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodetransformparameter.md#class_VisualShaderNodeTransformParameter_property_default_value_enabled) | `false` |

---

### Property Descriptions

<span id="class_VisualShaderNodeTransformParameter_property_default_value"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **default_value** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_visualshadernodetransformparameter.md#class_VisualShaderNodeTransformParameter_property_default_value)

- void **set_default_value** ( value: [Transform3D](class_transform3d.md#class_Transform3D) )
- [Transform3D](class_transform3d.md#class_Transform3D) **get_default_value** ( )

A default value to be assigned within the shader.

---

<span id="class_VisualShaderNodeTransformParameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodetransformparameter.md#class_VisualShaderNodeTransformParameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

Enables usage of the [default_value](class_visualshadernodetransformparameter.md#class_VisualShaderNodeTransformParameter_property_default_value).
