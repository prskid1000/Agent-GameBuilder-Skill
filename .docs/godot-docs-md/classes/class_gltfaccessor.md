<span id="class_GLTFAccessor"></span>

## GLTFAccessor

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a glTF accessor.

### Description

GLTFAccessor is a data structure representing a glTF `accessor` that would be found in the `"accessors"` array. A buffer is a blob of binary data. A buffer view is a slice of a buffer. An accessor is a typed interpretation of the data in a buffer view.

Most custom data stored in glTF does not need accessors, only buffer views (see [GLTFBufferView](class_gltfbufferview.md#class_GLTFBufferView)). Accessors are for more advanced use cases such as interleaved mesh data encoded for the GPU.

### Tutorials

- Buffers, BufferViews, and Accessors in Khronos glTF specification

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) | [accessor_type](class_gltfaccessor.md#class_GLTFAccessor_property_accessor_type) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [buffer_view](class_gltfaccessor.md#class_GLTFAccessor_property_buffer_view) | `-1` |
| [int](class_int.md#class_int) | [byte_offset](class_gltfaccessor.md#class_GLTFAccessor_property_byte_offset) | `0` |
| [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) | [component_type](class_gltfaccessor.md#class_GLTFAccessor_property_component_type) | `0` |
| [int](class_int.md#class_int) | [count](class_gltfaccessor.md#class_GLTFAccessor_property_count) | `0` |
| [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) | [max](class_gltfaccessor.md#class_GLTFAccessor_property_max) | `PackedFloat64Array()` |
| [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) | [min](class_gltfaccessor.md#class_GLTFAccessor_property_min) | `PackedFloat64Array()` |
| [bool](class_bool.md#class_bool) | [normalized](class_gltfaccessor.md#class_GLTFAccessor_property_normalized) | `false` |
| [int](class_int.md#class_int) | [sparse_count](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_count) | `0` |
| [int](class_int.md#class_int) | [sparse_indices_buffer_view](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_indices_buffer_view) | `0` |
| [int](class_int.md#class_int) | [sparse_indices_byte_offset](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_indices_byte_offset) | `0` |
| [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) | [sparse_indices_component_type](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_indices_component_type) | `0` |
| [int](class_int.md#class_int) | [sparse_values_buffer_view](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_values_buffer_view) | `0` |
| [int](class_int.md#class_int) | [sparse_values_byte_offset](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_values_byte_offset) | `0` |
| [int](class_int.md#class_int) | [type](class_gltfaccessor.md#class_GLTFAccessor_property_type) |

### Methods


| [GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) | [from_dictionary](class_gltfaccessor.md#class_GLTFAccessor_method_from_dictionary) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) static |
| --- | --- |
| [Dictionary](class_dictionary.md#class_Dictionary) | [to_dictionary](class_gltfaccessor.md#class_GLTFAccessor_method_to_dictionary) ( ) const |

---

### Enumerations

<span id="enum_GLTFAccessor_GLTFAccessorType"></span>

enum **GLTFAccessorType**: [🔗](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType)

<span id="class_GLTFAccessor_constant_TYPE_SCALAR"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_SCALAR** = `0`

Accessor type "SCALAR". For the glTF object model, this can be used to map to a single float, int, or bool value, or a float array.

<span id="class_GLTFAccessor_constant_TYPE_VEC2"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_VEC2** = `1`

Accessor type "VEC2". For the glTF object model, this maps to "float2", represented in the glTF JSON as an array of two floats.

<span id="class_GLTFAccessor_constant_TYPE_VEC3"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_VEC3** = `2`

Accessor type "VEC3". For the glTF object model, this maps to "float3", represented in the glTF JSON as an array of three floats.

<span id="class_GLTFAccessor_constant_TYPE_VEC4"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_VEC4** = `3`

Accessor type "VEC4". For the glTF object model, this maps to "float4", represented in the glTF JSON as an array of four floats.

<span id="class_GLTFAccessor_constant_TYPE_MAT2"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_MAT2** = `4`

Accessor type "MAT2". For the glTF object model, this maps to "float2x2", represented in the glTF JSON as an array of four floats.

<span id="class_GLTFAccessor_constant_TYPE_MAT3"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_MAT3** = `5`

Accessor type "MAT3". For the glTF object model, this maps to "float3x3", represented in the glTF JSON as an array of nine floats.

<span id="class_GLTFAccessor_constant_TYPE_MAT4"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **TYPE_MAT4** = `6`

Accessor type "MAT4". For the glTF object model, this maps to "float4x4", represented in the glTF JSON as an array of sixteen floats.

---

<span id="enum_GLTFAccessor_GLTFComponentType"></span>

enum **GLTFComponentType**: [🔗](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType)

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_NONE"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_NONE** = `0`

Component type "NONE". This is not a valid component type, and is used to indicate that the component type is not set.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_BYTE"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_SIGNED_BYTE** = `5120`

Component type "BYTE". The value is `0x1400` which comes from OpenGL. This indicates data is stored in 1-byte or 8-bit signed integers. This is a core part of the glTF specification.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_BYTE"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_UNSIGNED_BYTE** = `5121`

Component type "UNSIGNED_BYTE". The value is `0x1401` which comes from OpenGL. This indicates data is stored in 1-byte or 8-bit unsigned integers. This is a core part of the glTF specification.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_SHORT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_SIGNED_SHORT** = `5122`

Component type "SHORT". The value is `0x1402` which comes from OpenGL. This indicates data is stored in 2-byte or 16-bit signed integers. This is a core part of the glTF specification.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_SHORT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_UNSIGNED_SHORT** = `5123`

Component type "UNSIGNED_SHORT". The value is `0x1403` which comes from OpenGL. This indicates data is stored in 2-byte or 16-bit unsigned integers. This is a core part of the glTF specification.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_INT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_SIGNED_INT** = `5124`

Component type "INT". The value is `0x1404` which comes from OpenGL. This indicates data is stored in 4-byte or 32-bit signed integers. This is NOT a core part of the glTF specification, and may not be supported by all glTF importers. May be used by some extensions including `KHR_interactivity`.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_INT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_UNSIGNED_INT** = `5125`

Component type "UNSIGNED_INT". The value is `0x1405` which comes from OpenGL. This indicates data is stored in 4-byte or 32-bit unsigned integers. This is a core part of the glTF specification.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_SINGLE_FLOAT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_SINGLE_FLOAT** = `5126`

Component type "FLOAT". The value is `0x1406` which comes from OpenGL. This indicates data is stored in 4-byte or 32-bit floating-point numbers. This is a core part of the glTF specification.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_DOUBLE_FLOAT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_DOUBLE_FLOAT** = `5130`

Component type "DOUBLE". The value is `0x140A` which comes from OpenGL. This indicates data is stored in 8-byte or 64-bit floating-point numbers. This is NOT a core part of the glTF specification, and may not be supported by all glTF importers. May be used by some extensions including `KHR_interactivity`.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_HALF_FLOAT"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_HALF_FLOAT** = `5131`

Component type "HALF_FLOAT". The value is `0x140B` which comes from OpenGL. This indicates data is stored in 2-byte or 16-bit floating-point numbers. This is NOT a core part of the glTF specification, and may not be supported by all glTF importers. May be used by some extensions including `KHR_interactivity`.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_LONG"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_SIGNED_LONG** = `5134`

Component type "LONG". The value is `0x140E` which comes from OpenGL. This indicates data is stored in 8-byte or 64-bit signed integers. This is NOT a core part of the glTF specification, and may not be supported by all glTF importers. May be used by some extensions including `KHR_interactivity`.

<span id="class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_LONG"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **COMPONENT_TYPE_UNSIGNED_LONG** = `5135`

Component type "UNSIGNED_LONG". The value is `0x140F` which comes from OpenGL. This indicates data is stored in 8-byte or 64-bit unsigned integers. This is NOT a core part of the glTF specification, and may not be supported by all glTF importers. May be used by some extensions including `KHR_interactivity`.

---

### Property Descriptions

<span id="class_GLTFAccessor_property_accessor_type"></span>

[GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **accessor_type** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_accessor_type)

- void **set_accessor_type** ( value: [GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) )
- [GLTFAccessorType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFAccessorType) **get_accessor_type** ( )

The glTF accessor type, as an enum.

---

<span id="class_GLTFAccessor_property_buffer_view"></span>

[int](class_int.md#class_int) **buffer_view** = `-1` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_buffer_view)

- void **set_buffer_view** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_buffer_view** ( )

The index of the buffer view this accessor is referencing. If `-1`, this accessor is not referencing any buffer view.

---

<span id="class_GLTFAccessor_property_byte_offset"></span>

[int](class_int.md#class_int) **byte_offset** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_byte_offset)

- void **set_byte_offset** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_byte_offset** ( )

The offset relative to the start of the buffer view in bytes.

---

<span id="class_GLTFAccessor_property_component_type"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **component_type** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_component_type)

- void **set_component_type** ( value: [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) )
- [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **get_component_type** ( )

The glTF component type as an enum. See [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) for possible values. Within the core glTF specification, a value of 5125 or "UNSIGNED_INT" must not be used for any accessor that is not referenced by mesh.primitive.indices.

---

<span id="class_GLTFAccessor_property_count"></span>

[int](class_int.md#class_int) **count** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_count)

- void **set_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_count** ( )

The number of elements referenced by this accessor.

---

<span id="class_GLTFAccessor_property_max"></span>

[PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) **max** = `PackedFloat64Array()` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_max)

- void **set_max** ( value: [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) )
- [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) **get_max** ( )

Maximum value of each component in this accessor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) for more details.

---

<span id="class_GLTFAccessor_property_min"></span>

[PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) **min** = `PackedFloat64Array()` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_min)

- void **set_min** ( value: [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) )
- [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) **get_min** ( )

Minimum value of each component in this accessor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) for more details.

---

<span id="class_GLTFAccessor_property_normalized"></span>

[bool](class_bool.md#class_bool) **normalized** = `false` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_normalized)

- void **set_normalized** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_normalized** ( )

Specifies whether integer data values are normalized before usage.

---

<span id="class_GLTFAccessor_property_sparse_count"></span>

[int](class_int.md#class_int) **sparse_count** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_count)

- void **set_sparse_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sparse_count** ( )

Number of deviating accessor values stored in the sparse array.

---

<span id="class_GLTFAccessor_property_sparse_indices_buffer_view"></span>

[int](class_int.md#class_int) **sparse_indices_buffer_view** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_indices_buffer_view)

- void **set_sparse_indices_buffer_view** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sparse_indices_buffer_view** ( )

The index of the buffer view with sparse indices. The referenced buffer view MUST NOT have its target or byteStride properties defined. The buffer view and the optional byteOffset MUST be aligned to the componentType byte length.

---

<span id="class_GLTFAccessor_property_sparse_indices_byte_offset"></span>

[int](class_int.md#class_int) **sparse_indices_byte_offset** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_indices_byte_offset)

- void **set_sparse_indices_byte_offset** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sparse_indices_byte_offset** ( )

The offset relative to the start of the buffer view in bytes.

---

<span id="class_GLTFAccessor_property_sparse_indices_component_type"></span>

[GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **sparse_indices_component_type** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_indices_component_type)

- void **set_sparse_indices_component_type** ( value: [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) )
- [GLTFComponentType](class_gltfaccessor.md#enum_GLTFAccessor_GLTFComponentType) **get_sparse_indices_component_type** ( )

The indices component data type as an enum. Possible values are 5121 for "UNSIGNED_BYTE", 5123 for "UNSIGNED_SHORT", and 5125 for "UNSIGNED_INT".

---

<span id="class_GLTFAccessor_property_sparse_values_buffer_view"></span>

[int](class_int.md#class_int) **sparse_values_buffer_view** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_values_buffer_view)

- void **set_sparse_values_buffer_view** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sparse_values_buffer_view** ( )

The index of the bufferView with sparse values. The referenced buffer view MUST NOT have its target or byteStride properties defined.

---

<span id="class_GLTFAccessor_property_sparse_values_byte_offset"></span>

[int](class_int.md#class_int) **sparse_values_byte_offset** = `0` [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_sparse_values_byte_offset)

- void **set_sparse_values_byte_offset** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sparse_values_byte_offset** ( )

The offset relative to the start of the bufferView in bytes.

---

<span id="class_GLTFAccessor_property_type"></span>

[int](class_int.md#class_int) **type** [🔗](class_gltfaccessor.md#class_GLTFAccessor_property_type)

- void **set_type** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_type** ( )

**Deprecated:** Use [accessor_type](class_gltfaccessor.md#class_GLTFAccessor_property_accessor_type) instead.

The glTF accessor type, as an [int](class_int.md#class_int). Possible values are `0` for "SCALAR", `1` for "VEC2", `2` for "VEC3", `3` for "VEC4", `4` for "MAT2", `5` for "MAT3", and `6` for "MAT4".

---

### Method Descriptions

<span id="class_GLTFAccessor_method_from_dictionary"></span>

[GLTFAccessor](class_gltfaccessor.md#class_GLTFAccessor) **from_dictionary** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) *static* [🔗](class_gltfaccessor.md#class_GLTFAccessor_method_from_dictionary)

Creates a new GLTFAccessor instance by parsing the given [Dictionary](class_dictionary.md#class_Dictionary).

---

<span id="class_GLTFAccessor_method_to_dictionary"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **to_dictionary** ( ) *const* [🔗](class_gltfaccessor.md#class_GLTFAccessor_method_to_dictionary)

Serializes this GLTFAccessor instance into a [Dictionary](class_dictionary.md#class_Dictionary).
