<span id="class_UniformSetCacheRD"></span>

## UniformSetCacheRD

**Inherits:** [Object](class_object.md#class_Object)

Uniform set cache manager for Rendering Device based renderers.

### Description

Uniform set cache manager for [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

### Methods


| [RID](class_rid.md#class_RID) | [get_cache](class_uniformsetcacherd.md#class_UniformSetCacheRD_method_get_cache) ( shader: [RID](class_rid.md#class_RID), set: [int](class_int.md#class_int), uniforms: [Array](class_array.md#class_Array)\[[RDUniform](class_rduniform.md#class_RDUniform)\] ) static |
| --- | --- |

---

### Method Descriptions

<span id="class_UniformSetCacheRD_method_get_cache"></span>

[RID](class_rid.md#class_RID) **get_cache** ( shader: [RID](class_rid.md#class_RID), set: [int](class_int.md#class_int), uniforms: [Array](class_array.md#class_Array)\[[RDUniform](class_rduniform.md#class_RDUniform)\] ) *static* [🔗](class_uniformsetcacherd.md#class_UniformSetCacheRD_method_get_cache)

Creates/returns a cached uniform set based on the provided uniforms for a given shader.
