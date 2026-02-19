<span id="class_VisualShaderNodeScreenUVToSDF"></span>

## VisualShaderNodeScreenUVToSDF

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A function to convert screen UV to an SDF (signed-distance field), to be used within the visual shader graph.

### Description

Translates to `screen_uv_to_sdf(uv)` in the shader language. If the UV port isn't connected, `SCREEN_UV` is used instead.
