<span id="class_GLTFObjectModelProperty"></span>

## GLTFObjectModelProperty

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Describes how to access a property as defined in the glTF object model.

### Description

GLTFObjectModelProperty defines a mapping between a property in the glTF object model and a NodePath in the Godot scene tree. This can be used to animate properties in a glTF file using the `KHR_animation_pointer` extension, or to access them through an engine-agnostic script such as a behavior graph as defined by the `KHR_interactivity` extension.

The glTF property is identified by JSON pointer(s) stored in [json_pointers](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_json_pointers), while the Godot property it maps to is defined by [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths). In most cases [json_pointers](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_json_pointers) and [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths) will each only have one item, but in some cases a single glTF JSON pointer will map to multiple Godot properties, or a single Godot property will be mapped to multiple glTF JSON pointers, or it might be a many-to-many relationship.

 [Expression](class_expression.md#class_Expression) objects can be used to define conversions between the data, such as when glTF defines an angle in radians and Godot uses degrees. The [object_model_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_object_model_type) property defines the type of data stored in the glTF file as defined by the object model, see [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) for possible values.

### Tutorials

- GLTF Object Model

- KHR_animation_pointer GLTF extension

### Properties


| [Expression](class_expression.md#class_Expression) | [gltf_to_godot_expression](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_gltf_to_godot_expression) |
| --- | --- |
| [Expression](class_expression.md#class_Expression) | [godot_to_gltf_expression](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_godot_to_gltf_expression) |
| [Array](class_array.md#class_Array)\[[PackedStringArray](class_packedstringarray.md#class_PackedStringArray)\] | [json_pointers](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_json_pointers) | `[]` |
| [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] | [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths) | `[]` |
| [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) | [object_model_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_object_model_type) | `0` |
| Variant.Type | [variant_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_variant_type) | `0` |

### Methods


| void | [append_node_path](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_node_path) ( node_path: [NodePath](class_nodepath.md#class_NodePath) ) |
| --- | --- |
| void | [append_path_to_property](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_path_to_property) ( node_path: [NodePath](class_nodepath.md#class_NodePath), prop_name: [StringName](class_stringname.md#class_StringName) ) |
| [GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) | [get_accessor_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_get_accessor_type) ( ) const |
| [bool](class_bool.md#class_bool) | [has_json_pointers](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_has_json_pointers) ( ) const |
| [bool](class_bool.md#class_bool) | [has_node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_has_node_paths) ( ) const |
| void | [set_types](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_set_types) ( variant_type: Variant.Type, obj_model_type: [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) ) |

---

### Enumerations

<span id="enum_GLTFObjectModelProperty_GLTFObjectModelType"></span>

enum **GLTFObjectModelType**: [🔗](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType)

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_UNKNOWN"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_UNKNOWN** = `0`

Unknown or not set object model type. If the object model type is set to this value, the real type still needs to be determined.

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_BOOL"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_BOOL** = `1`

Object model type "bool". Represented in the glTF JSON as a boolean, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "SCALAR". When encoded in an accessor, a value of `0` is `false`, and any other value is `true`.

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT** = `2`

Object model type "float". Represented in the glTF JSON as a number, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "SCALAR".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY** = `3`

Object model type "float\[\]". Represented in the glTF JSON as an array of numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "SCALAR".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT2"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT2** = `4`

Object model type "float2". Represented in the glTF JSON as an array of two numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "VEC2".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT3"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT3** = `5`

Object model type "float3". Represented in the glTF JSON as an array of three numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "VEC3".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT4"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT4** = `6`

Object model type "float4". Represented in the glTF JSON as an array of four numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "VEC4".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT2X2"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT2X2** = `7`

Object model type "float2x2". Represented in the glTF JSON as an array of four numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "MAT2".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT3X3"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT3X3** = `8`

Object model type "float3x3". Represented in the glTF JSON as an array of nine numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "MAT3".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT4X4"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_FLOAT4X4** = `9`

Object model type "float4x4". Represented in the glTF JSON as an array of sixteen numbers, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "MAT4".

<span id="class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_INT"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **GLTF_OBJECT_MODEL_TYPE_INT** = `10`

Object model type "int". Represented in the glTF JSON as a number, and encoded in a [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) as "SCALAR". The range of values is limited to signed integers. For `KHR_interactivity`, only 32-bit integers are supported.

---

### Property Descriptions

<span id="class_GLTFObjectModelProperty_property_gltf_to_godot_expression"></span>

[Expression](class_expression.md#class_Expression) **gltf_to_godot_expression** [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_gltf_to_godot_expression)

- void **set_gltf_to_godot_expression** ( value: [Expression](class_expression.md#class_Expression) )
- [Expression](class_expression.md#class_Expression) **get_gltf_to_godot_expression** ( )

If set, this [Expression](class_expression.md#class_Expression) will be used to convert the property value from the glTF object model to the value expected by the Godot property. This is useful when the glTF object model uses a different unit system, or when the data needs to be transformed in some way. If `null`, the value will be copied as-is.

---

<span id="class_GLTFObjectModelProperty_property_godot_to_gltf_expression"></span>

[Expression](class_expression.md#class_Expression) **godot_to_gltf_expression** [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_godot_to_gltf_expression)

- void **set_godot_to_gltf_expression** ( value: [Expression](class_expression.md#class_Expression) )
- [Expression](class_expression.md#class_Expression) **get_godot_to_gltf_expression** ( )

If set, this [Expression](class_expression.md#class_Expression) will be used to convert the property value from the Godot property to the value expected by the glTF object model. This is useful when the glTF object model uses a different unit system, or when the data needs to be transformed in some way. If `null`, the value will be copied as-is.

---

<span id="class_GLTFObjectModelProperty_property_json_pointers"></span>

[Array](class_array.md#class_Array)\[[PackedStringArray](class_packedstringarray.md#class_PackedStringArray)\] **json_pointers** = `[]` [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_json_pointers)

- void **set_json_pointers** ( value: [Array](class_array.md#class_Array)\[[PackedStringArray](class_packedstringarray.md#class_PackedStringArray)\] )
- [Array](class_array.md#class_Array)\[[PackedStringArray](class_packedstringarray.md#class_PackedStringArray)\] **get_json_pointers** ( )

The glTF object model JSON pointers used to identify the property in the glTF object model. In most cases, there will be only one item in this array, but specific cases may require multiple pointers. The items are themselves arrays which represent the JSON pointer split into its components.

---

<span id="class_GLTFObjectModelProperty_property_node_paths"></span>

[Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **node_paths** = `[]` [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths)

- void **set_node_paths** ( value: [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] )
- [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **get_node_paths** ( )

An array of [NodePath](class_nodepath.md#class_NodePath) s that point to a property, or multiple properties, in the Godot scene tree. On import, this will either be set by [GLTFDocument](class_gltfdocument.md#class_GLTFDocument), or by a [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) class. For simple cases, use [append_path_to_property()](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_path_to_property) to add properties to this array.

In most cases [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths) will only have one item, but in some cases a single glTF JSON pointer will map to multiple Godot properties. For example, a [GLTFCamera](class_gltfcamera.md#class_GLTFCamera) or [GLTFLight](class_gltflight.md#class_GLTFLight) used on multiple glTF nodes will be represented by multiple Godot nodes.

---

<span id="class_GLTFObjectModelProperty_property_object_model_type"></span>

[GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **object_model_type** = `0` [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_object_model_type)

- void **set_object_model_type** ( value: [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) )
- [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) **get_object_model_type** ( )

The type of data stored in the glTF file as defined by the object model. This is a superset of the available accessor types, and determines the accessor type.

---

<span id="class_GLTFObjectModelProperty_property_variant_type"></span>

Variant.Type **variant_type** = `0` [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_variant_type)

- void **set_variant_type** ( value: Variant.Type )
- Variant.Type **get_variant_type** ( )

The type of data stored in the Godot property. This is the type of the property that the [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths) point to.

---

### Method Descriptions

<span id="class_GLTFObjectModelProperty_method_append_node_path"></span>

void **append_node_path** ( node_path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_node_path)

Appends a [NodePath](class_nodepath.md#class_NodePath) to [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths). This can be used by [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes to define how a glTF object model property maps to a Godot property, or multiple Godot properties. Prefer using [append_path_to_property()](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_path_to_property) for simple cases. Be sure to also call [set_types()](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_set_types) once (the order does not matter).

---

<span id="class_GLTFObjectModelProperty_method_append_path_to_property"></span>

void **append_path_to_property** ( node_path: [NodePath](class_nodepath.md#class_NodePath), prop_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_path_to_property)

High-level wrapper over [append_node_path()](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_append_node_path) that handles the most common cases. It constructs a new [NodePath](class_nodepath.md#class_NodePath) using `node_path` as a base and appends `prop_name` to the subpath. Be sure to also call [set_types()](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_set_types) once (the order does not matter).

---

<span id="class_GLTFObjectModelProperty_method_get_accessor_type"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **get_accessor_type** ( ) *const* [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_get_accessor_type)

The GLTF accessor type associated with this property's [object_model_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_object_model_type). See [GLTFAccessor.accessor_type](class_gltfaccessor.md#class_GLTFAccessor_property_accessor_type) for possible values, and see [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) for how the object model type maps to accessor types.

---

<span id="class_GLTFObjectModelProperty_method_has_json_pointers"></span>

[bool](class_bool.md#class_bool) **has_json_pointers** ( ) *const* [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_has_json_pointers)

Returns `true` if [json_pointers](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_json_pointers) is not empty. This is used during export to determine if a **GLTFObjectModelProperty** can handle converting a Godot property to a glTF object model property.

---

<span id="class_GLTFObjectModelProperty_method_has_node_paths"></span>

[bool](class_bool.md#class_bool) **has_node_paths** ( ) *const* [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_has_node_paths)

Returns `true` if [node_paths](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_node_paths) is not empty. This is used during import to determine if a **GLTFObjectModelProperty** can handle converting a glTF object model property to a Godot property.

---

<span id="class_GLTFObjectModelProperty_method_set_types"></span>

void **set_types** ( variant_type: Variant.Type, obj_model_type: [GLTFObjectModelType](class_gltfobjectmodelproperty.md#enum_GLTFObjectModelProperty_GLTFObjectModelType) ) [🔗](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_method_set_types)

Sets the [variant_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_variant_type) and [object_model_type](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty_property_object_model_type) properties. This is a convenience method to set both properties at once, since they are almost always known at the same time. This method should be called once. Calling it again with the same values will have no effect.
