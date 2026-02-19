<span id="class_VisualInstance3D"></span>

## VisualInstance3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [Decal](class_decal.md#class_Decal), [FogVolume](class_fogvolume.md#class_FogVolume), [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D), [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D), [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D), [Light3D](class_light3d.md#class_Light3D), [LightmapGI](class_lightmapgi.md#class_LightmapGI), [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D), [OpenXRVisibilityMask](class_openxrvisibilitymask.md#class_OpenXRVisibilityMask), [ReflectionProbe](class_reflectionprobe.md#class_ReflectionProbe), [RootMotionView](class_rootmotionview.md#class_RootMotionView), [VisibleOnScreenNotifier3D](class_visibleonscreennotifier3d.md#class_VisibleOnScreenNotifier3D), [VoxelGI](class_voxelgi.md#class_VoxelGI)

Parent of all visual 3D nodes.

### Description

The **VisualInstance3D** is used to connect a resource to a visual representation. All visual 3D nodes inherit from the **VisualInstance3D**. In general, you should not access the **VisualInstance3D** properties directly as they are accessed and managed by the nodes that inherit from **VisualInstance3D**. **VisualInstance3D** is the node representation of the [RenderingServer](class_renderingserver.md#class_RenderingServer) instance.

### Properties


| [int](class_int.md#class_int) | [layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers) | `1` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [sorting_offset](class_visualinstance3d.md#class_VisualInstance3D_property_sorting_offset) | `0.0` |
| [bool](class_bool.md#class_bool) | [sorting_use_aabb_center](class_visualinstance3d.md#class_VisualInstance3D_property_sorting_use_aabb_center) |

### Methods


| [AABB](class_aabb.md#class_AABB) | [_get_aabb](class_visualinstance3d.md#class_VisualInstance3D_private_method__get_aabb) ( ) | virtual | const |
| --- | --- | --- | --- |
| [AABB](class_aabb.md#class_AABB) | [get_aabb](class_visualinstance3d.md#class_VisualInstance3D_method_get_aabb) ( ) const |
| [RID](class_rid.md#class_RID) | [get_base](class_visualinstance3d.md#class_VisualInstance3D_method_get_base) ( ) const |
| [RID](class_rid.md#class_RID) | [get_instance](class_visualinstance3d.md#class_VisualInstance3D_method_get_instance) ( ) const |
| [bool](class_bool.md#class_bool) | [get_layer_mask_value](class_visualinstance3d.md#class_VisualInstance3D_method_get_layer_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| void | [set_base](class_visualinstance3d.md#class_VisualInstance3D_method_set_base) ( base: [RID](class_rid.md#class_RID) ) |
| void | [set_layer_mask_value](class_visualinstance3d.md#class_VisualInstance3D_method_set_layer_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_VisualInstance3D_property_layers"></span>

[int](class_int.md#class_int) **layers** = `1` [🔗](class_visualinstance3d.md#class_VisualInstance3D_property_layers)

- void **set_layer_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_layer_mask** ( )

The render layer(s) this **VisualInstance3D** is drawn on.

This object will only be visible for [Camera3D](class_camera3d.md#class_Camera3D) s whose cull mask includes any of the render layers this **VisualInstance3D** is set to.

For [Light3D](class_light3d.md#class_Light3D) s, this can be used to control which **VisualInstance3D** s are affected by a specific light. For [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), this can be used to control which particles are effected by a specific attractor. For [Decal](class_decal.md#class_Decal) s, this can be used to control which **VisualInstance3D** s are affected by a specific decal.

To adjust [layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers) more easily using a script, use [get_layer_mask_value()](class_visualinstance3d.md#class_VisualInstance3D_method_get_layer_mask_value) and [set_layer_mask_value()](class_visualinstance3d.md#class_VisualInstance3D_method_set_layer_mask_value).

 **Note:** [VoxelGI](class_voxelgi.md#class_VoxelGI), SDFGI and [LightmapGI](class_lightmapgi.md#class_LightmapGI) will always take all layers into account to determine what contributes to global illumination. If this is an issue, set [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_mode) to [GeometryInstance3D.GI_MODE_DISABLED](class_geometryinstance3d.md#class_GeometryInstance3D_constant_GI_MODE_DISABLED) for meshes and [Light3D.light_bake_mode](class_light3d.md#class_Light3D_property_light_bake_mode) to [Light3D.BAKE_DISABLED](class_light3d.md#class_Light3D_constant_BAKE_DISABLED) for lights to exclude them from global illumination.

---

<span id="class_VisualInstance3D_property_sorting_offset"></span>

[float](class_float.md#class_float) **sorting_offset** = `0.0` [🔗](class_visualinstance3d.md#class_VisualInstance3D_property_sorting_offset)

- void **set_sorting_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_sorting_offset** ( )

The amount by which the depth of this **VisualInstance3D** will be adjusted when sorting by depth. Uses the same units as the engine (which are typically meters). Adjusting it to a higher value will make the **VisualInstance3D** reliably draw on top of other **VisualInstance3D** s that are otherwise positioned at the same spot. To ensure it always draws on top of other objects around it (not positioned at the same spot), set the value to be greater than the distance between this **VisualInstance3D** and the other nearby **VisualInstance3D** s.

---

<span id="class_VisualInstance3D_property_sorting_use_aabb_center"></span>

[bool](class_bool.md#class_bool) **sorting_use_aabb_center** [🔗](class_visualinstance3d.md#class_VisualInstance3D_property_sorting_use_aabb_center)

- void **set_sorting_use_aabb_center** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_sorting_use_aabb_center** ( )

If `true`, the object is sorted based on the [AABB](class_aabb.md#class_AABB) center. The object will be sorted based on the global position otherwise.

The [AABB](class_aabb.md#class_AABB) center based sorting is generally more accurate for 3D models. The position based sorting instead allows to better control the drawing order when working with [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) and [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D).

---

### Method Descriptions

<span id="class_VisualInstance3D_private_method__get_aabb"></span>

[AABB](class_aabb.md#class_AABB) **_get_aabb** ( ) *virtual* *const* [🔗](class_visualinstance3d.md#class_VisualInstance3D_private_method__get_aabb)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_VisualInstance3D_method_get_aabb"></span>

[AABB](class_aabb.md#class_AABB) **get_aabb** ( ) *const* [🔗](class_visualinstance3d.md#class_VisualInstance3D_method_get_aabb)

Returns the [AABB](class_aabb.md#class_AABB) (also known as the bounding box) for this **VisualInstance3D**.

---

<span id="class_VisualInstance3D_method_get_base"></span>

[RID](class_rid.md#class_RID) **get_base** ( ) *const* [🔗](class_visualinstance3d.md#class_VisualInstance3D_method_get_base)

Returns the RID of the resource associated with this **VisualInstance3D**. For example, if the Node is a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D), this will return the RID of the associated [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_VisualInstance3D_method_get_instance"></span>

[RID](class_rid.md#class_RID) **get_instance** ( ) *const* [🔗](class_visualinstance3d.md#class_VisualInstance3D_method_get_instance)

Returns the RID of this instance. This RID is the same as the RID returned by [RenderingServer.instance_create()](class_renderingserver.md#class_RenderingServer_method_instance_create). This RID is needed if you want to call [RenderingServer](class_renderingserver.md#class_RenderingServer) functions directly on this **VisualInstance3D**.

---

<span id="class_VisualInstance3D_method_get_layer_mask_value"></span>

[bool](class_bool.md#class_bool) **get_layer_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_visualinstance3d.md#class_VisualInstance3D_method_get_layer_mask_value)

Returns whether or not the specified layer of the [layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers) is enabled, given a `layer_number` between 1 and 20.

---

<span id="class_VisualInstance3D_method_set_base"></span>

void **set_base** ( base: [RID](class_rid.md#class_RID) ) [🔗](class_visualinstance3d.md#class_VisualInstance3D_method_set_base)

Sets the resource that is instantiated by this **VisualInstance3D**, which changes how the engine handles the **VisualInstance3D** under the hood. Equivalent to [RenderingServer.instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base).

---

<span id="class_VisualInstance3D_method_set_layer_mask_value"></span>

void **set_layer_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_visualinstance3d.md#class_VisualInstance3D_method_set_layer_mask_value)

Based on `value`, enables or disables the specified layer in the [layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers), given a `layer_number` between 1 and 20.
