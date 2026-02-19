<span id="class_VisualShaderNodeParameter"></span>

## VisualShaderNodeParameter

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeBooleanParameter](class_visualshadernodebooleanparameter.md#class_VisualShaderNodeBooleanParameter), [VisualShaderNodeColorParameter](class_visualshadernodecolorparameter.md#class_VisualShaderNodeColorParameter), [VisualShaderNodeFloatParameter](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter), [VisualShaderNodeIntParameter](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter), [VisualShaderNodeTextureParameter](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter), [VisualShaderNodeTransformParameter](class_visualshadernodetransformparameter.md#class_VisualShaderNodeTransformParameter), [VisualShaderNodeUIntParameter](class_visualshadernodeuintparameter.md#class_VisualShaderNodeUIntParameter), [VisualShaderNodeVec2Parameter](class_visualshadernodevec2parameter.md#class_VisualShaderNodeVec2Parameter), [VisualShaderNodeVec3Parameter](class_visualshadernodevec3parameter.md#class_VisualShaderNodeVec3Parameter), [VisualShaderNodeVec4Parameter](class_visualshadernodevec4parameter.md#class_VisualShaderNodeVec4Parameter)

A base type for the parameters within the visual shader graph.

### Description

A parameter represents a variable in the shader which is set externally, i.e. from the [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial). Parameters are exposed as properties in the [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) and can be assigned from the Inspector or from a script.

### Properties


| [int](class_int.md#class_int) | [instance_index](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_instance_index) | `0` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [parameter_name](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_parameter_name) | `""` |
| [Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) | [qualifier](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_qualifier) | `0` |

---

### Enumerations

<span id="enum_VisualShaderNodeParameter_Qualifier"></span>

enum **Qualifier**: [🔗](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier)

<span id="class_VisualShaderNodeParameter_constant_QUAL_NONE"></span>

[Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **QUAL_NONE** = `0`

The parameter will be tied to the [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) using this shader.

<span id="class_VisualShaderNodeParameter_constant_QUAL_GLOBAL"></span>

[Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **QUAL_GLOBAL** = `1`

The parameter will use a global value, defined in Project Settings.

<span id="class_VisualShaderNodeParameter_constant_QUAL_INSTANCE"></span>

[Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **QUAL_INSTANCE** = `2`

The parameter will be tied to the node with attached [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) using this shader.

<span id="class_VisualShaderNodeParameter_constant_QUAL_INSTANCE_INDEX"></span>

[Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **QUAL_INSTANCE_INDEX** = `3`

The parameter will be tied to the node with attached [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) using this shader. Enables setting a [instance_index](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_instance_index) property.

<span id="class_VisualShaderNodeParameter_constant_QUAL_MAX"></span>

[Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **QUAL_MAX** = `4`

Represents the size of the [Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeParameter_property_instance_index"></span>

[int](class_int.md#class_int) **instance_index** = `0` [🔗](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_instance_index)

- void **set_instance_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_instance_index** ( )

The index within 0-15 range, which is used to avoid clashes when shader used on multiple materials.

---

<span id="class_VisualShaderNodeParameter_property_parameter_name"></span>

[String](class_string.md#class_String) **parameter_name** = `""` [🔗](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_parameter_name)

- void **set_parameter_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_parameter_name** ( )

Name of the parameter, by which it can be accessed through the [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) properties.

---

<span id="class_VisualShaderNodeParameter_property_qualifier"></span>

[Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **qualifier** = `0` [🔗](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter_property_qualifier)

- void **set_qualifier** ( value: [Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) )
- [Qualifier](class_visualshadernodeparameter.md#enum_VisualShaderNodeParameter_Qualifier) **get_qualifier** ( )

Defines the scope of the parameter.
