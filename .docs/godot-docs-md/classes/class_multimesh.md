.. meta::
	:keywords: batch

<span id="class_MultiMesh"></span>

## MultiMesh

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides high-performance drawing of a mesh multiple times using GPU instancing.

### Description

MultiMesh provides low-level mesh instancing. Drawing thousands of [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) nodes can be slow, since each object is submitted to the GPU then drawn individually.

MultiMesh is much faster as it can draw thousands of instances with a single draw call, resulting in less API overhead.

As a drawback, if the instances are too far away from each other, performance may be reduced as every single instance will always render (they are spatially indexed as one, for the whole object).

Since instances may have any behavior, the AABB used for visibility must be provided by the user.

 **Note:** A MultiMesh is a single object, therefore the same maximum lights per object restriction applies. This means, that once the maximum lights are consumed by one or more instances, the rest of the MultiMesh instances will **not** receive any lighting.

 **Note:** Blend Shapes will be ignored if used in a MultiMesh.

### Tutorials

- [Using MultiMeshInstance](../tutorials/3d/using_multi_mesh_instance.md)

- [Optimization using MultiMeshes](../tutorials/performance/using_multimesh.md)

- [Animating thousands of fish with MultiMeshInstance](../tutorials/performance/vertex_animation/animating_thousands_of_fish.md)

### Properties


| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [buffer](class_multimesh.md#class_MultiMesh_property_buffer) | `PackedFloat32Array()` |
| --- | --- | --- |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [color_array](class_multimesh.md#class_MultiMesh_property_color_array) |
| [AABB](class_aabb.md#class_AABB) | [custom_aabb](class_multimesh.md#class_MultiMesh_property_custom_aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [custom_data_array](class_multimesh.md#class_MultiMesh_property_custom_data_array) |
| [int](class_int.md#class_int) | [instance_count](class_multimesh.md#class_MultiMesh_property_instance_count) | `0` |
| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_multimesh.md#class_MultiMesh_property_mesh) |
| [PhysicsInterpolationQuality](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality) | [physics_interpolation_quality](class_multimesh.md#class_MultiMesh_property_physics_interpolation_quality) | `0` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [transform_2d_array](class_multimesh.md#class_MultiMesh_property_transform_2d_array) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [transform_array](class_multimesh.md#class_MultiMesh_property_transform_array) |
| [TransformFormat](class_multimesh.md#enum_MultiMesh_TransformFormat) | [transform_format](class_multimesh.md#class_MultiMesh_property_transform_format) | `0` |
| [bool](class_bool.md#class_bool) | [use_colors](class_multimesh.md#class_MultiMesh_property_use_colors) | `false` |
| [bool](class_bool.md#class_bool) | [use_custom_data](class_multimesh.md#class_MultiMesh_property_use_custom_data) | `false` |
| [int](class_int.md#class_int) | [visible_instance_count](class_multimesh.md#class_MultiMesh_property_visible_instance_count) | `-1` |

### Methods


| [AABB](class_aabb.md#class_AABB) | [get_aabb](class_multimesh.md#class_MultiMesh_method_get_aabb) ( ) const |
| --- | --- |
| [Color](class_color.md#class_Color) | [get_instance_color](class_multimesh.md#class_MultiMesh_method_get_instance_color) ( instance: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_instance_custom_data](class_multimesh.md#class_MultiMesh_method_get_instance_custom_data) ( instance: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_instance_transform](class_multimesh.md#class_MultiMesh_method_get_instance_transform) ( instance: [int](class_int.md#class_int) ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_instance_transform_2d](class_multimesh.md#class_MultiMesh_method_get_instance_transform_2d) ( instance: [int](class_int.md#class_int) ) const |
| void | [reset_instance_physics_interpolation](class_multimesh.md#class_MultiMesh_method_reset_instance_physics_interpolation) ( instance: [int](class_int.md#class_int) ) |
| void | [reset_instances_physics_interpolation](class_multimesh.md#class_MultiMesh_method_reset_instances_physics_interpolation) ( ) |
| void | [set_buffer_interpolated](class_multimesh.md#class_MultiMesh_method_set_buffer_interpolated) ( buffer_curr: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), buffer_prev: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| void | [set_instance_color](class_multimesh.md#class_MultiMesh_method_set_instance_color) ( instance: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_instance_custom_data](class_multimesh.md#class_MultiMesh_method_set_instance_custom_data) ( instance: [int](class_int.md#class_int), custom_data: [Color](class_color.md#class_Color) ) |
| void | [set_instance_transform](class_multimesh.md#class_MultiMesh_method_set_instance_transform) ( instance: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [set_instance_transform_2d](class_multimesh.md#class_MultiMesh_method_set_instance_transform_2d) ( instance: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |

---

### Enumerations

<span id="enum_MultiMesh_TransformFormat"></span>

enum **TransformFormat**: [🔗](class_multimesh.md#enum_MultiMesh_TransformFormat)

<span id="class_MultiMesh_constant_TRANSFORM_2D"></span>

[TransformFormat](class_multimesh.md#enum_MultiMesh_TransformFormat) **TRANSFORM_2D** = `0`

Use this when using 2D transforms.

<span id="class_MultiMesh_constant_TRANSFORM_3D"></span>

[TransformFormat](class_multimesh.md#enum_MultiMesh_TransformFormat) **TRANSFORM_3D** = `1`

Use this when using 3D transforms.

---

<span id="enum_MultiMesh_PhysicsInterpolationQuality"></span>

enum **PhysicsInterpolationQuality**: [🔗](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality)

<span id="class_MultiMesh_constant_INTERP_QUALITY_FAST"></span>

[PhysicsInterpolationQuality](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality) **INTERP_QUALITY_FAST** = `0`

Always interpolate using Basis lerping, which can produce warping artifacts in some situations.

<span id="class_MultiMesh_constant_INTERP_QUALITY_HIGH"></span>

[PhysicsInterpolationQuality](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality) **INTERP_QUALITY_HIGH** = `1`

Attempt to interpolate using Basis slerping (spherical linear interpolation) where possible, otherwise fall back to lerping.

---

### Property Descriptions

<span id="class_MultiMesh_property_buffer"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **buffer** = `PackedFloat32Array()` [🔗](class_multimesh.md#class_MultiMesh_property_buffer)

- void **set_buffer** ( value: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) )
- [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_buffer** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) for more details.

---

<span id="class_MultiMesh_property_color_array"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **color_array** [🔗](class_multimesh.md#class_MultiMesh_property_color_array)

**Deprecated:** Accessing this property is very slow. Use [set_instance_color()](class_multimesh.md#class_MultiMesh_method_set_instance_color) and [get_instance_color()](class_multimesh.md#class_MultiMesh_method_get_instance_color) instead.

Array containing each [Color](class_color.md#class_Color) used by all instances of this mesh.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.

---

<span id="class_MultiMesh_property_custom_aabb"></span>

[AABB](class_aabb.md#class_AABB) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_multimesh.md#class_MultiMesh_property_custom_aabb)

- void **set_custom_aabb** ( value: [AABB](class_aabb.md#class_AABB) )
- [AABB](class_aabb.md#class_AABB) **get_custom_aabb** ( )

Custom AABB for this MultiMesh resource. Setting this manually prevents costly runtime AABB recalculations.

---

<span id="class_MultiMesh_property_custom_data_array"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **custom_data_array** [🔗](class_multimesh.md#class_MultiMesh_property_custom_data_array)

**Deprecated:** Accessing this property is very slow. Use [set_instance_custom_data()](class_multimesh.md#class_MultiMesh_method_set_instance_custom_data) and [get_instance_custom_data()](class_multimesh.md#class_MultiMesh_method_get_instance_custom_data) instead.

Array containing each custom data value used by all instances of this mesh, as a [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.

---

<span id="class_MultiMesh_property_instance_count"></span>

[int](class_int.md#class_int) **instance_count** = `0` [🔗](class_multimesh.md#class_MultiMesh_property_instance_count)

- void **set_instance_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_instance_count** ( )

Number of instances that will get drawn. This clears and (re)sizes the buffers. Setting data format or flags afterwards will have no effect.

By default, all instances are drawn but you can limit this with [visible_instance_count](class_multimesh.md#class_MultiMesh_property_visible_instance_count).

---

<span id="class_MultiMesh_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_multimesh.md#class_MultiMesh_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

[Mesh](class_mesh.md#class_Mesh) resource to be instanced.

The looks of the individual instances can be modified using [set_instance_color()](class_multimesh.md#class_MultiMesh_method_set_instance_color) and [set_instance_custom_data()](class_multimesh.md#class_MultiMesh_method_set_instance_custom_data).

---

<span id="class_MultiMesh_property_physics_interpolation_quality"></span>

[PhysicsInterpolationQuality](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality) **physics_interpolation_quality** = `0` [🔗](class_multimesh.md#class_MultiMesh_property_physics_interpolation_quality)

- void **set_physics_interpolation_quality** ( value: [PhysicsInterpolationQuality](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality) )
- [PhysicsInterpolationQuality](class_multimesh.md#enum_MultiMesh_PhysicsInterpolationQuality) **get_physics_interpolation_quality** ( )

Choose whether to use an interpolation method that favors speed or quality.

When using low physics tick rates (typically below 20) or high rates of object rotation, you may get better results from the high quality setting.

 **Note:** Fast quality does not equate to low quality. Except in the special cases mentioned above, the quality should be comparable to high quality.

---

<span id="class_MultiMesh_property_transform_2d_array"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **transform_2d_array** [🔗](class_multimesh.md#class_MultiMesh_property_transform_2d_array)

**Deprecated:** Accessing this property is very slow. Use [set_instance_transform_2d()](class_multimesh.md#class_MultiMesh_method_set_instance_transform_2d) and [get_instance_transform_2d()](class_multimesh.md#class_MultiMesh_method_get_instance_transform_2d) instead.

Array containing each [Transform2D](class_transform2d.md#class_Transform2D) value used by all instances of this mesh, as a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array). Each transform is divided into 3 [Vector2](class_vector2.md#class_Vector2) values corresponding to the transforms' `x`, `y`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_MultiMesh_property_transform_array"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **transform_array** [🔗](class_multimesh.md#class_MultiMesh_property_transform_array)

**Deprecated:** Accessing this property is very slow. Use [set_instance_transform()](class_multimesh.md#class_MultiMesh_method_set_instance_transform) and [get_instance_transform()](class_multimesh.md#class_MultiMesh_method_get_instance_transform) instead.

Array containing each [Transform3D](class_transform3d.md#class_Transform3D) value used by all instances of this mesh, as a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array). Each transform is divided into 4 [Vector3](class_vector3.md#class_Vector3) values corresponding to the transforms' `x`, `y`, `z`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) for more details.

---

<span id="class_MultiMesh_property_transform_format"></span>

[TransformFormat](class_multimesh.md#enum_MultiMesh_TransformFormat) **transform_format** = `0` [🔗](class_multimesh.md#class_MultiMesh_property_transform_format)

- void **set_transform_format** ( value: [TransformFormat](class_multimesh.md#enum_MultiMesh_TransformFormat) )
- [TransformFormat](class_multimesh.md#enum_MultiMesh_TransformFormat) **get_transform_format** ( )

Format of transform used to transform mesh, either 2D or 3D.

---

<span id="class_MultiMesh_property_use_colors"></span>

[bool](class_bool.md#class_bool) **use_colors** = `false` [🔗](class_multimesh.md#class_MultiMesh_property_use_colors)

- void **set_use_colors** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_colors** ( )

If `true`, the **MultiMesh** will use color data (see [set_instance_color()](class_multimesh.md#class_MultiMesh_method_set_instance_color)). Can only be set when [instance_count](class_multimesh.md#class_MultiMesh_property_instance_count) is `0` or less. This means that you need to call this method before setting the instance count, or temporarily reset it to `0`.

---

<span id="class_MultiMesh_property_use_custom_data"></span>

[bool](class_bool.md#class_bool) **use_custom_data** = `false` [🔗](class_multimesh.md#class_MultiMesh_property_use_custom_data)

- void **set_use_custom_data** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_custom_data** ( )

If `true`, the **MultiMesh** will use custom data (see [set_instance_custom_data()](class_multimesh.md#class_MultiMesh_method_set_instance_custom_data)). Can only be set when [instance_count](class_multimesh.md#class_MultiMesh_property_instance_count) is `0` or less. This means that you need to call this method before setting the instance count, or temporarily reset it to `0`.

---

<span id="class_MultiMesh_property_visible_instance_count"></span>

[int](class_int.md#class_int) **visible_instance_count** = `-1` [🔗](class_multimesh.md#class_MultiMesh_property_visible_instance_count)

- void **set_visible_instance_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_visible_instance_count** ( )

Limits the number of instances drawn, -1 draws all instances. Changing this does not change the sizes of the buffers.

---

### Method Descriptions

<span id="class_MultiMesh_method_get_aabb"></span>

[AABB](class_aabb.md#class_AABB) **get_aabb** ( ) *const* [🔗](class_multimesh.md#class_MultiMesh_method_get_aabb)

Returns the visibility axis-aligned bounding box in local space.

---

<span id="class_MultiMesh_method_get_instance_color"></span>

[Color](class_color.md#class_Color) **get_instance_color** ( instance: [int](class_int.md#class_int) ) *const* [🔗](class_multimesh.md#class_MultiMesh_method_get_instance_color)

Gets a specific instance's color multiplier.

---

<span id="class_MultiMesh_method_get_instance_custom_data"></span>

[Color](class_color.md#class_Color) **get_instance_custom_data** ( instance: [int](class_int.md#class_int) ) *const* [🔗](class_multimesh.md#class_MultiMesh_method_get_instance_custom_data)

Returns the custom data that has been set for a specific instance.

---

<span id="class_MultiMesh_method_get_instance_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_instance_transform** ( instance: [int](class_int.md#class_int) ) *const* [🔗](class_multimesh.md#class_MultiMesh_method_get_instance_transform)

Returns the [Transform3D](class_transform3d.md#class_Transform3D) of a specific instance.

---

<span id="class_MultiMesh_method_get_instance_transform_2d"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_instance_transform_2d** ( instance: [int](class_int.md#class_int) ) *const* [🔗](class_multimesh.md#class_MultiMesh_method_get_instance_transform_2d)

Returns the [Transform2D](class_transform2d.md#class_Transform2D) of a specific instance.

---

<span id="class_MultiMesh_method_reset_instance_physics_interpolation"></span>

void **reset_instance_physics_interpolation** ( instance: [int](class_int.md#class_int) ) [🔗](class_multimesh.md#class_MultiMesh_method_reset_instance_physics_interpolation)

When using *physics interpolation*, this function allows you to prevent interpolation on an instance in the current physics tick.

This allows you to move instances instantaneously, and should usually be used when initially placing an instance such as a bullet to prevent graphical glitches.

---

<span id="class_MultiMesh_method_reset_instances_physics_interpolation"></span>

void **reset_instances_physics_interpolation** ( ) [🔗](class_multimesh.md#class_MultiMesh_method_reset_instances_physics_interpolation)

When using *physics interpolation*, this function allows you to prevent interpolation for all instances in the current physics tick.

This allows you to move all instances instantaneously, and should usually be used when initially placing instances to prevent graphical glitches.

---

<span id="class_MultiMesh_method_set_buffer_interpolated"></span>

void **set_buffer_interpolated** ( buffer_curr: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), buffer_prev: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_multimesh.md#class_MultiMesh_method_set_buffer_interpolated)

An alternative to setting the [buffer](class_multimesh.md#class_MultiMesh_property_buffer) property, which can be used with *physics interpolation*. This method takes two arrays, and can set the data for the current and previous tick in one go. The renderer will automatically interpolate the data at each frame.

This is useful for situations where the order of instances may change from physics tick to tick, such as particle systems.

When the order of instances is coherent, the simpler alternative of setting [buffer](class_multimesh.md#class_MultiMesh_property_buffer) can still be used with interpolation.

---

<span id="class_MultiMesh_method_set_instance_color"></span>

void **set_instance_color** ( instance: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_multimesh.md#class_MultiMesh_method_set_instance_color)

Sets the color of a specific instance by *multiplying* the mesh's existing vertex colors. This allows for different color tinting per instance.

 **Note:** Each component is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.

For the color to take effect, ensure that [use_colors](class_multimesh.md#class_MultiMesh_property_use_colors) is `true` on the **MultiMesh** and [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) is `true` on the material. If you intend to set an absolute color instead of tinting, make sure the material's albedo color is set to pure white (`Color(1, 1, 1)`).

---

<span id="class_MultiMesh_method_set_instance_custom_data"></span>

void **set_instance_custom_data** ( instance: [int](class_int.md#class_int), custom_data: [Color](class_color.md#class_Color) ) [🔗](class_multimesh.md#class_MultiMesh_method_set_instance_custom_data)

Sets custom data for a specific instance. `custom_data` is a [Color](class_color.md#class_Color) type only to contain 4 floating-point numbers.

 **Note:** Each number is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.

For the custom data to be used, ensure that [use_custom_data](class_multimesh.md#class_MultiMesh_property_use_custom_data) is `true`.

This custom instance data has to be manually accessed in your custom shader using `INSTANCE_CUSTOM`.

---

<span id="class_MultiMesh_method_set_instance_transform"></span>

void **set_instance_transform** ( instance: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_multimesh.md#class_MultiMesh_method_set_instance_transform)

Sets the [Transform3D](class_transform3d.md#class_Transform3D) for a specific instance.

---

<span id="class_MultiMesh_method_set_instance_transform_2d"></span>

void **set_instance_transform_2d** ( instance: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_multimesh.md#class_MultiMesh_method_set_instance_transform_2d)

Sets the [Transform2D](class_transform2d.md#class_Transform2D) for a specific instance.
