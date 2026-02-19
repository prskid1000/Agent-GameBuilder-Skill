<span id="class_VisualShaderNodeTransformDecompose"></span>

## VisualShaderNodeTransformDecompose

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Decomposes a [Transform3D](class_transform3d.md#class_Transform3D) into four [Vector3](class_vector3.md#class_Vector3) s within the visual shader graph.

### Description

Takes a 4×4 transform matrix and decomposes it into four `vec3` values, one from each row of the matrix.
