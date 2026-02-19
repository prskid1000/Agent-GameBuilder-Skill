<span id="class_VisualShaderNodeIf"></span>

## VisualShaderNodeIf

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Outputs a 3D vector based on the result of a floating-point comparison within the visual shader graph.

### Description

This visual shader node has six input ports:

- Port **1** and **2** provide the two floating-point numbers `a` and `b` that will be compared.

- Port **3** is the tolerance, which allows similar floating-point numbers to be considered equal.

- Ports **4**, **5**, and **6** are the possible outputs, returned if `a == b`, `a > b`, or `a < b` respectively.
