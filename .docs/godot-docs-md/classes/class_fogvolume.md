<span id="class_FogVolume"></span>

## FogVolume

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A region that contributes to the default volumetric fog from the world environment.

### Description

**FogVolume** s are used to add localized fog into the global volumetric fog effect. **FogVolume** s can also remove volumetric fog from specific areas if using a [FogMaterial](class_fogmaterial.md#class_FogMaterial) with a negative [FogMaterial.density](class_fogmaterial.md#class_FogMaterial_property_density).

Performance of **FogVolume** s is directly related to their relative size on the screen and the complexity of their attached [FogMaterial](class_fogmaterial.md#class_FogMaterial). It is best to keep **FogVolume** s relatively small and simple where possible.

 **Note:** **FogVolume** s only have a visible effect if [Environment.volumetric_fog_enabled](class_environment.md#class_Environment_property_volumetric_fog_enabled) is `true`. If you don't want fog to be globally visible (but only within **FogVolume** nodes), set [Environment.volumetric_fog_density](class_environment.md#class_Environment_property_volumetric_fog_density) to `0.0`.

### Tutorials

- [Volumetric fog and fog volumes](../tutorials/3d/volumetric_fog.md)

### Properties


| [Material](class_material.md#class_Material) | [material](class_fogvolume.md#class_FogVolume_property_material) |
| --- | --- |
| [FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) | [shape](class_fogvolume.md#class_FogVolume_property_shape) | `3` |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_fogvolume.md#class_FogVolume_property_size) | `Vector3(2, 2, 2)` |

---

### Property Descriptions

<span id="class_FogVolume_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_fogvolume.md#class_FogVolume_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The [Material](class_material.md#class_Material) used by the **FogVolume**. Can be either a built-in [FogMaterial](class_fogmaterial.md#class_FogMaterial) or a custom [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial).

---

<span id="class_FogVolume_property_shape"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **shape** = `3` [🔗](class_fogvolume.md#class_FogVolume_property_shape)

- void **set_shape** ( value: [FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) )
- [FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **get_shape** ( )

The shape of the **FogVolume**. This can be set to either [RenderingServer.FOG_VOLUME_SHAPE_ELLIPSOID](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID), [RenderingServer.FOG_VOLUME_SHAPE_CONE](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE), [RenderingServer.FOG_VOLUME_SHAPE_CYLINDER](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER), [RenderingServer.FOG_VOLUME_SHAPE_BOX](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX) or [RenderingServer.FOG_VOLUME_SHAPE_WORLD](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_WORLD).

---

<span id="class_FogVolume_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_fogvolume.md#class_FogVolume_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The size of the **FogVolume** when [shape](class_fogvolume.md#class_FogVolume_property_shape) is [RenderingServer.FOG_VOLUME_SHAPE_ELLIPSOID](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID), [RenderingServer.FOG_VOLUME_SHAPE_CONE](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE), [RenderingServer.FOG_VOLUME_SHAPE_CYLINDER](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER) or [RenderingServer.FOG_VOLUME_SHAPE_BOX](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX).

 **Note:** Thin fog volumes may appear to flicker when the camera moves or rotates. This can be alleviated by increasing ProjectSettings.rendering/environment/volumetric_fog/volume_depth (at a performance cost) or by decreasing [Environment.volumetric_fog_length](class_environment.md#class_Environment_property_volumetric_fog_length) (at no performance cost, but at the cost of lower fog range). Alternatively, the **FogVolume** can be made thicker and use a lower density in the [material](class_fogvolume.md#class_FogVolume_property_material).

 **Note:** If [shape](class_fogvolume.md#class_FogVolume_property_shape) is [RenderingServer.FOG_VOLUME_SHAPE_CONE](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE) or [RenderingServer.FOG_VOLUME_SHAPE_CYLINDER](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER), the cone/cylinder will be adjusted to fit within the size. Non-uniform scaling of cone/cylinder shapes via the [size](class_fogvolume.md#class_FogVolume_property_size) property is not supported, but you can scale the **FogVolume** node instead.
