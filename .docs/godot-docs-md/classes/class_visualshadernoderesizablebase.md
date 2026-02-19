<span id="class_VisualShaderNodeResizableBase"></span>

## VisualShaderNodeResizableBase

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeCurveTexture](class_visualshadernodecurvetexture.md#class_VisualShaderNodeCurveTexture), [VisualShaderNodeCurveXYZTexture](class_visualshadernodecurvexyztexture.md#class_VisualShaderNodeCurveXYZTexture), [VisualShaderNodeFrame](class_visualshadernodeframe.md#class_VisualShaderNodeFrame), [VisualShaderNodeGroupBase](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase)

Base class for resizable nodes in a visual shader graph.

### Description

Resizable nodes have a handle that allows the user to adjust their size as needed.

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [size](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase_property_size) | `Vector2(0, 0)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeResizableBase_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(0, 0)` [🔗](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase_property_size)

- void **set_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

The size of the node in the visual shader graph.
