<span id="class_VisualShaderNodeVaryingGetter"></span>

## VisualShaderNodeVaryingGetter

**Inherits:** [VisualShaderNodeVarying](class_visualshadernodevarying.md#class_VisualShaderNodeVarying) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node that gets a value of a varying.

### Description

Outputs a value of a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying getter in Fragment shader requires a varying with mode set to [VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT](class_visualshader.md#class_VisualShader_constant_VARYING_MODE_VERTEX_TO_FRAG_LIGHT).
