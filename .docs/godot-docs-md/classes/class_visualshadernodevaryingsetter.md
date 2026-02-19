<span id="class_VisualShaderNodeVaryingSetter"></span>

## VisualShaderNodeVaryingSetter

**Inherits:** [VisualShaderNodeVarying](class_visualshadernodevarying.md#class_VisualShaderNodeVarying) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node that sets a value of a varying.

### Description

Inputs a value to a varying defined in the shader. You need to first create a varying that can be used in the given function, e.g. varying setter in Fragment shader requires a varying with mode set to [VisualShader.VARYING_MODE_FRAG_TO_LIGHT](class_visualshader.md#class_VisualShader_constant_VARYING_MODE_FRAG_TO_LIGHT).
