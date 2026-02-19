<span id="class_VisualShaderNodeTransformCompose"></span>

## VisualShaderNodeTransformCompose

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Composes a [Transform3D](class_transform3d.md#class_Transform3D) from four [Vector3](class_vector3.md#class_Vector3) s within the visual shader graph.

### Description

Creates a 4×4 transform matrix using four vectors of type `vec3`. Each vector is one row in the matrix and the last column is a `vec4(0, 0, 0, 1)`.
