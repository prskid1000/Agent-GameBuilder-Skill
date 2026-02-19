<span id="class_VisualShaderNodeGlobalExpression"></span>

## VisualShaderNodeGlobalExpression

**Inherits:** [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class_VisualShaderNodeExpression) **<** [VisualShaderNodeGroupBase](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase) **<** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A custom global visual shader graph expression written in Godot Shading Language.

### Description

Custom Godot Shader Language expression, which is placed on top of the generated shader. You can place various function definitions inside to call later in [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class_VisualShaderNodeExpression) s (which are injected in the main shader functions). You can also declare varyings, uniforms and global constants.
