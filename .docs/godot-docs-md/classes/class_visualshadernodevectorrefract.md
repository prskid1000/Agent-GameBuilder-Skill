<span id="class_VisualShaderNodeVectorRefract"></span>

## VisualShaderNodeVectorRefract

**Inherits:** [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class_VisualShaderNodeVectorBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Returns the vector that points in the direction of refraction. For use within the visual shader graph.

### Description

Translated to `refract(I, N, eta)` in the shader language, where `I` is the incident vector, `N` is the normal vector and `eta` is the ratio of the indices of the refraction.
