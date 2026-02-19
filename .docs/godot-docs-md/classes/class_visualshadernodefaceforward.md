<span id="class_VisualShaderNodeFaceForward"></span>

## VisualShaderNodeFaceForward

**Inherits:** [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class_VisualShaderNodeVectorBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Returns the vector that points in the same direction as a reference vector within the visual shader graph.

### Description

Translates to `faceforward(N, I, Nref)` in the shader language. The function has three vector parameters: `N`, the vector to orient, `I`, the incident vector, and `Nref`, the reference vector. If the dot product of `I` and `Nref` is smaller than zero the return value is `N`. Otherwise, `-N` is returned.
