<span id="class_RDUniform"></span>

## RDUniform

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Shader uniform (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [int](class_int.md#class_int) | [binding](class_rduniform.md#class_RDUniform_property_binding) | `0` |
| --- | --- | --- |
| [UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) | [uniform_type](class_rduniform.md#class_RDUniform_property_uniform_type) | `3` |

### Methods


| void | [add_id](class_rduniform.md#class_RDUniform_method_add_id) ( id: [RID](class_rid.md#class_RID) ) |
| --- | --- |
| void | [clear_ids](class_rduniform.md#class_RDUniform_method_clear_ids) ( ) |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [get_ids](class_rduniform.md#class_RDUniform_method_get_ids) ( ) const |

---

### Property Descriptions

<span id="class_RDUniform_property_binding"></span>

[int](class_int.md#class_int) **binding** = `0` [🔗](class_rduniform.md#class_RDUniform_property_binding)

- void **set_binding** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_binding** ( )

The uniform's binding.

---

<span id="class_RDUniform_property_uniform_type"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **uniform_type** = `3` [🔗](class_rduniform.md#class_RDUniform_property_uniform_type)

- void **set_uniform_type** ( value: [UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) )
- [UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **get_uniform_type** ( )

The uniform's data type.

---

### Method Descriptions

<span id="class_RDUniform_method_add_id"></span>

void **add_id** ( id: [RID](class_rid.md#class_RID) ) [🔗](class_rduniform.md#class_RDUniform_method_add_id)

Binds the given id to the uniform. The data associated with the id is then used when the uniform is passed to a shader.

---

<span id="class_RDUniform_method_clear_ids"></span>

void **clear_ids** ( ) [🔗](class_rduniform.md#class_RDUniform_method_clear_ids)

Unbinds all ids currently bound to the uniform.

---

<span id="class_RDUniform_method_get_ids"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_ids** ( ) *const* [🔗](class_rduniform.md#class_RDUniform_method_get_ids)

Returns an array of all ids currently bound to the uniform.
