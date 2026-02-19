<span id="class_Lightmapper"></span>

## Lightmapper

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [LightmapperRD](class_lightmapperrd.md#class_LightmapperRD)

Abstract class extended by lightmappers, for use in [LightmapGI](class_lightmapgi.md#class_LightmapGI).

### Description

This class should be extended by custom lightmapper classes. Lightmappers can then be used with [LightmapGI](class_lightmapgi.md#class_LightmapGI) to provide fast baked global illumination in 3D.

Godot contains a built-in GPU-based lightmapper [LightmapperRD](class_lightmapperrd.md#class_LightmapperRD) that uses compute shaders, but custom lightmappers can be implemented by C++ modules.
