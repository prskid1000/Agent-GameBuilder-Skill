<span id="class_VisualShaderNode"></span>

## VisualShaderNode

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeBillboard](class_visualshadernodebillboard.md#class_VisualShaderNodeBillboard), [VisualShaderNodeClamp](class_visualshadernodeclamp.md#class_VisualShaderNodeClamp), [VisualShaderNodeColorFunc](class_visualshadernodecolorfunc.md#class_VisualShaderNodeColorFunc), [VisualShaderNodeColorOp](class_visualshadernodecolorop.md#class_VisualShaderNodeColorOp), [VisualShaderNodeCompare](class_visualshadernodecompare.md#class_VisualShaderNodeCompare), [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class_VisualShaderNodeConstant), [VisualShaderNodeCubemap](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap), [VisualShaderNodeCustom](class_visualshadernodecustom.md#class_VisualShaderNodeCustom), [VisualShaderNodeDerivativeFunc](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc), [VisualShaderNodeDeterminant](class_visualshadernodedeterminant.md#class_VisualShaderNodeDeterminant), [VisualShaderNodeDistanceFade](class_visualshadernodedistancefade.md#class_VisualShaderNodeDistanceFade), [VisualShaderNodeDotProduct](class_visualshadernodedotproduct.md#class_VisualShaderNodeDotProduct), [VisualShaderNodeFloatFunc](class_visualshadernodefloatfunc.md#class_VisualShaderNodeFloatFunc), [VisualShaderNodeFloatOp](class_visualshadernodefloatop.md#class_VisualShaderNodeFloatOp), [VisualShaderNodeFresnel](class_visualshadernodefresnel.md#class_VisualShaderNodeFresnel), [VisualShaderNodeIf](class_visualshadernodeif.md#class_VisualShaderNodeIf), [VisualShaderNodeInput](class_visualshadernodeinput.md#class_VisualShaderNodeInput), [VisualShaderNodeIntFunc](class_visualshadernodeintfunc.md#class_VisualShaderNodeIntFunc), [VisualShaderNodeIntOp](class_visualshadernodeintop.md#class_VisualShaderNodeIntOp), [VisualShaderNodeIs](class_visualshadernodeis.md#class_VisualShaderNodeIs), [VisualShaderNodeLinearSceneDepth](class_visualshadernodelinearscenedepth.md#class_VisualShaderNodeLinearSceneDepth), [VisualShaderNodeMix](class_visualshadernodemix.md#class_VisualShaderNodeMix), [VisualShaderNodeMultiplyAdd](class_visualshadernodemultiplyadd.md#class_VisualShaderNodeMultiplyAdd), [VisualShaderNodeOuterProduct](class_visualshadernodeouterproduct.md#class_VisualShaderNodeOuterProduct), [VisualShaderNodeOutput](class_visualshadernodeoutput.md#class_VisualShaderNodeOutput), [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter), [VisualShaderNodeParameterRef](class_visualshadernodeparameterref.md#class_VisualShaderNodeParameterRef), [VisualShaderNodeParticleAccelerator](class_visualshadernodeparticleaccelerator.md#class_VisualShaderNodeParticleAccelerator), [VisualShaderNodeParticleConeVelocity](class_visualshadernodeparticleconevelocity.md#class_VisualShaderNodeParticleConeVelocity), [VisualShaderNodeParticleEmit](class_visualshadernodeparticleemit.md#class_VisualShaderNodeParticleEmit), [VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class_VisualShaderNodeParticleEmitter), [VisualShaderNodeParticleMultiplyByAxisAngle](class_visualshadernodeparticlemultiplybyaxisangle.md#class_VisualShaderNodeParticleMultiplyByAxisAngle), [VisualShaderNodeParticleRandomness](class_visualshadernodeparticlerandomness.md#class_VisualShaderNodeParticleRandomness), [VisualShaderNodeProximityFade](class_visualshadernodeproximityfade.md#class_VisualShaderNodeProximityFade), [VisualShaderNodeRandomRange](class_visualshadernoderandomrange.md#class_VisualShaderNodeRandomRange), [VisualShaderNodeRemap](class_visualshadernoderemap.md#class_VisualShaderNodeRemap), [VisualShaderNodeReroute](class_visualshadernodereroute.md#class_VisualShaderNodeReroute), [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase), [VisualShaderNodeRotationByAxis](class_visualshadernoderotationbyaxis.md#class_VisualShaderNodeRotationByAxis), [VisualShaderNodeSample3D](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D), [VisualShaderNodeScreenNormalWorldSpace](class_visualshadernodescreennormalworldspace.md#class_VisualShaderNodeScreenNormalWorldSpace), [VisualShaderNodeScreenUVToSDF](class_visualshadernodescreenuvtosdf.md#class_VisualShaderNodeScreenUVToSDF), [VisualShaderNodeSDFRaymarch](class_visualshadernodesdfraymarch.md#class_VisualShaderNodeSDFRaymarch), [VisualShaderNodeSDFToScreenUV](class_visualshadernodesdftoscreenuv.md#class_VisualShaderNodeSDFToScreenUV), [VisualShaderNodeSmoothStep](class_visualshadernodesmoothstep.md#class_VisualShaderNodeSmoothStep), [VisualShaderNodeStep](class_visualshadernodestep.md#class_VisualShaderNodeStep), [VisualShaderNodeSwitch](class_visualshadernodeswitch.md#class_VisualShaderNodeSwitch), [VisualShaderNodeTexture](class_visualshadernodetexture.md#class_VisualShaderNodeTexture), [VisualShaderNodeTextureSDF](class_visualshadernodetexturesdf.md#class_VisualShaderNodeTextureSDF), [VisualShaderNodeTextureSDFNormal](class_visualshadernodetexturesdfnormal.md#class_VisualShaderNodeTextureSDFNormal), [VisualShaderNodeTransformCompose](class_visualshadernodetransformcompose.md#class_VisualShaderNodeTransformCompose), [VisualShaderNodeTransformDecompose](class_visualshadernodetransformdecompose.md#class_VisualShaderNodeTransformDecompose), [VisualShaderNodeTransformFunc](class_visualshadernodetransformfunc.md#class_VisualShaderNodeTransformFunc), [VisualShaderNodeTransformOp](class_visualshadernodetransformop.md#class_VisualShaderNodeTransformOp), [VisualShaderNodeTransformVecMult](class_visualshadernodetransformvecmult.md#class_VisualShaderNodeTransformVecMult), [VisualShaderNodeUIntFunc](class_visualshadernodeuintfunc.md#class_VisualShaderNodeUIntFunc), [VisualShaderNodeUIntOp](class_visualshadernodeuintop.md#class_VisualShaderNodeUIntOp), [VisualShaderNodeUVFunc](class_visualshadernodeuvfunc.md#class_VisualShaderNodeUVFunc), [VisualShaderNodeUVPolarCoord](class_visualshadernodeuvpolarcoord.md#class_VisualShaderNodeUVPolarCoord), [VisualShaderNodeVarying](class_visualshadernodevarying.md#class_VisualShaderNodeVarying), [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class_VisualShaderNodeVectorBase), [VisualShaderNodeWorldPositionFromDepth](class_visualshadernodeworldpositionfromdepth.md#class_VisualShaderNodeWorldPositionFromDepth)

Base class for [VisualShader](class_visualshader.md#class_VisualShader) nodes. Not related to scene nodes.

### Description

Visual shader graphs consist of various nodes. Each node in the graph is a separate object and they are represented as a rectangular boxes with title and a set of properties. Each node also has connection ports that allow to connect it to another nodes and control the flow of the shader.

### Tutorials

- [Using VisualShaders](../tutorials/shaders/visual_shaders.md)

### Properties


| [int](class_int.md#class_int) | [linked_parent_graph_frame](class_visualshadernode.md#class_VisualShaderNode_property_linked_parent_graph_frame) | `-1` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [output_port_for_preview](class_visualshadernode.md#class_VisualShaderNode_property_output_port_for_preview) | `-1` |

### Methods


| void | [clear_default_input_values](class_visualshadernode.md#class_VisualShaderNode_method_clear_default_input_values) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_default_input_port](class_visualshadernode.md#class_VisualShaderNode_method_get_default_input_port) ( type: [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) ) const |
| [Array](class_array.md#class_Array) | [get_default_input_values](class_visualshadernode.md#class_VisualShaderNode_method_get_default_input_values) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_input_port_default_value](class_visualshadernode.md#class_VisualShaderNode_method_get_input_port_default_value) ( port: [int](class_int.md#class_int) ) const |
| void | [remove_input_port_default_value](class_visualshadernode.md#class_VisualShaderNode_method_remove_input_port_default_value) ( port: [int](class_int.md#class_int) ) |
| void | [set_default_input_values](class_visualshadernode.md#class_VisualShaderNode_method_set_default_input_values) ( values: [Array](class_array.md#class_Array) ) |
| void | [set_input_port_default_value](class_visualshadernode.md#class_VisualShaderNode_method_set_input_port_default_value) ( port: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant), prev_value: [Variant](class_variant.md#class_Variant) = null ) |

---

### Enumerations

<span id="enum_VisualShaderNode_PortType"></span>

enum **PortType**: [🔗](class_visualshadernode.md#enum_VisualShaderNode_PortType)

<span id="class_VisualShaderNode_constant_PORT_TYPE_SCALAR"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_SCALAR** = `0`

Floating-point scalar. Translated to `float` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_SCALAR_INT"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_SCALAR_INT** = `1`

Integer scalar. Translated to `int` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_SCALAR_UINT"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_SCALAR_UINT** = `2`

Unsigned integer scalar. Translated to `uint` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_VECTOR_2D"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_VECTOR_2D** = `3`

2D vector of floating-point values. Translated to `vec2` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_VECTOR_3D"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_VECTOR_3D** = `4`

3D vector of floating-point values. Translated to `vec3` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_VECTOR_4D"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_VECTOR_4D** = `5`

4D vector of floating-point values. Translated to `vec4` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_BOOLEAN"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_BOOLEAN** = `6`

Boolean type. Translated to `bool` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_TRANSFORM"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_TRANSFORM** = `7`

Transform type. Translated to `mat4` type in shader code.

<span id="class_VisualShaderNode_constant_PORT_TYPE_SAMPLER"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_SAMPLER** = `8`

Sampler type. Translated to reference of sampler uniform in shader code. Can only be used for input ports in non-uniform nodes.

<span id="class_VisualShaderNode_constant_PORT_TYPE_MAX"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **PORT_TYPE_MAX** = `9`

Represents the size of the [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNode_property_linked_parent_graph_frame"></span>

[int](class_int.md#class_int) **linked_parent_graph_frame** = `-1` [🔗](class_visualshadernode.md#class_VisualShaderNode_property_linked_parent_graph_frame)

- void **set_frame** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_frame** ( )

Represents the index of the frame this node is linked to. If set to `-1` the node is not linked to any frame.

---

<span id="class_VisualShaderNode_property_output_port_for_preview"></span>

[int](class_int.md#class_int) **output_port_for_preview** = `-1` [🔗](class_visualshadernode.md#class_VisualShaderNode_property_output_port_for_preview)

- void **set_output_port_for_preview** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_output_port_for_preview** ( )

Sets the output port index which will be showed for preview. If set to `-1` no port will be open for preview.

---

### Method Descriptions

<span id="class_VisualShaderNode_method_clear_default_input_values"></span>

void **clear_default_input_values** ( ) [🔗](class_visualshadernode.md#class_VisualShaderNode_method_clear_default_input_values)

Clears the default input ports value.

---

<span id="class_VisualShaderNode_method_get_default_input_port"></span>

[int](class_int.md#class_int) **get_default_input_port** ( type: [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) ) *const* [🔗](class_visualshadernode.md#class_VisualShaderNode_method_get_default_input_port)

Returns the input port which should be connected by default when this node is created as a result of dragging a connection from an existing node to the empty space on the graph.

---

<span id="class_VisualShaderNode_method_get_default_input_values"></span>

[Array](class_array.md#class_Array) **get_default_input_values** ( ) *const* [🔗](class_visualshadernode.md#class_VisualShaderNode_method_get_default_input_values)

Returns an [Array](class_array.md#class_Array) containing default values for all of the input ports of the node in the form `[index0, value0, index1, value1, ...]`.

---

<span id="class_VisualShaderNode_method_get_input_port_default_value"></span>

[Variant](class_variant.md#class_Variant) **get_input_port_default_value** ( port: [int](class_int.md#class_int) ) *const* [🔗](class_visualshadernode.md#class_VisualShaderNode_method_get_input_port_default_value)

Returns the default value of the input `port`.

---

<span id="class_VisualShaderNode_method_remove_input_port_default_value"></span>

void **remove_input_port_default_value** ( port: [int](class_int.md#class_int) ) [🔗](class_visualshadernode.md#class_VisualShaderNode_method_remove_input_port_default_value)

Removes the default value of the input `port`.

---

<span id="class_VisualShaderNode_method_set_default_input_values"></span>

void **set_default_input_values** ( values: [Array](class_array.md#class_Array) ) [🔗](class_visualshadernode.md#class_VisualShaderNode_method_set_default_input_values)

Sets the default input ports values using an [Array](class_array.md#class_Array) of the form `[index0, value0, index1, value1, ...]`. For example: `[0, Vector3(0, 0, 0), 1, Vector3(0, 0, 0)]`.

---

<span id="class_VisualShaderNode_method_set_input_port_default_value"></span>

void **set_input_port_default_value** ( port: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant), prev_value: [Variant](class_variant.md#class_Variant) = null ) [🔗](class_visualshadernode.md#class_VisualShaderNode_method_set_input_port_default_value)

Sets the default `value` for the selected input `port`.
