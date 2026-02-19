.. meta::
	:keywords: stain

<span id="class_Decal"></span>

## Decal

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node that projects a texture onto a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D).

### Description

**Decal** s are used to project a texture onto a [Mesh](class_mesh.md#class_Mesh) in the scene. Use Decals to add detail to a scene without affecting the underlying [Mesh](class_mesh.md#class_Mesh). They are often used to add weathering to building, add dirt or mud to the ground, or add variety to props. Decals can be moved at any time, making them suitable for things like blob shadows or laser sight dots.

They are made of an [AABB](class_aabb.md#class_AABB) and a group of [Texture2D](class_texture2d.md#class_Texture2D) s specifying [Color](class_color.md#class_Color), normal, ORM (ambient occlusion, roughness, metallic), and emission. Decals are projected within their [AABB](class_aabb.md#class_AABB) so altering the orientation of the Decal affects the direction in which they are projected. By default, Decals are projected down (i.e. from positive Y to negative Y).

The [Texture2D](class_texture2d.md#class_Texture2D) s associated with the Decal are automatically stored in a texture atlas which is used for drawing the decals so all decals can be drawn at once. Godot uses clustered decals, meaning they are stored in cluster data and drawn when the mesh is drawn, they are not drawn as a post-processing effect after.

 **Note:** Decals cannot affect an underlying material's transparency, regardless of its transparency mode (alpha blend, alpha scissor, alpha hash, opaque pre-pass). This means translucent or transparent areas of a material will remain translucent or transparent even if an opaque decal is applied on them.

 **Note:** Decals are only supported in the Forward+ and Mobile rendering methods, not Compatibility. When using the Mobile rendering method, only 8 decals can be displayed on each mesh resource. Attempting to display more than 8 decals on a single mesh resource will result in decals flickering in and out as the camera moves.

 **Note:** When using the Mobile rendering method, decals will only correctly affect meshes whose visibility AABB intersects with the decal's AABB. If using a shader to deform the mesh in a way that makes it go outside its AABB, [GeometryInstance3D.extra_cull_margin](class_geometryinstance3d.md#class_GeometryInstance3D_property_extra_cull_margin) must be increased on the mesh. Otherwise, the decal may not be visible on the mesh.

### Properties


| [float](class_float.md#class_float) | [albedo_mix](class_decal.md#class_Decal_property_albedo_mix) | `1.0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [cull_mask](class_decal.md#class_Decal_property_cull_mask) | `1048575` |
| [float](class_float.md#class_float) | [distance_fade_begin](class_decal.md#class_Decal_property_distance_fade_begin) | `40.0` |
| [bool](class_bool.md#class_bool) | [distance_fade_enabled](class_decal.md#class_Decal_property_distance_fade_enabled) | `false` |
| [float](class_float.md#class_float) | [distance_fade_length](class_decal.md#class_Decal_property_distance_fade_length) | `10.0` |
| [float](class_float.md#class_float) | [emission_energy](class_decal.md#class_Decal_property_emission_energy) | `1.0` |
| [float](class_float.md#class_float) | [lower_fade](class_decal.md#class_Decal_property_lower_fade) | `0.3` |
| [Color](class_color.md#class_Color) | [modulate](class_decal.md#class_Decal_property_modulate) | `Color(1, 1, 1, 1)` |
| [float](class_float.md#class_float) | [normal_fade](class_decal.md#class_Decal_property_normal_fade) | `0.0` |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_decal.md#class_Decal_property_size) | `Vector3(2, 2, 2)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_albedo](class_decal.md#class_Decal_property_texture_albedo) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_emission](class_decal.md#class_Decal_property_texture_emission) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_normal](class_decal.md#class_Decal_property_texture_normal) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_orm](class_decal.md#class_Decal_property_texture_orm) |
| [float](class_float.md#class_float) | [upper_fade](class_decal.md#class_Decal_property_upper_fade) | `0.3` |

### Methods


| [Texture2D](class_texture2d.md#class_Texture2D) | [get_texture](class_decal.md#class_Decal_method_get_texture) ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture) ) const |
| --- | --- |
| void | [set_texture](class_decal.md#class_Decal_method_set_texture) ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |

---

### Enumerations

<span id="enum_Decal_DecalTexture"></span>

enum **DecalTexture**: [🔗](class_decal.md#enum_Decal_DecalTexture)

<span id="class_Decal_constant_TEXTURE_ALBEDO"></span>

[DecalTexture](class_decal.md#enum_Decal_DecalTexture) **TEXTURE_ALBEDO** = `0`

[Texture2D](class_texture2d.md#class_Texture2D) corresponding to [texture_albedo](class_decal.md#class_Decal_property_texture_albedo).

<span id="class_Decal_constant_TEXTURE_NORMAL"></span>

[DecalTexture](class_decal.md#enum_Decal_DecalTexture) **TEXTURE_NORMAL** = `1`

[Texture2D](class_texture2d.md#class_Texture2D) corresponding to [texture_normal](class_decal.md#class_Decal_property_texture_normal).

<span id="class_Decal_constant_TEXTURE_ORM"></span>

[DecalTexture](class_decal.md#enum_Decal_DecalTexture) **TEXTURE_ORM** = `2`

[Texture2D](class_texture2d.md#class_Texture2D) corresponding to [texture_orm](class_decal.md#class_Decal_property_texture_orm).

<span id="class_Decal_constant_TEXTURE_EMISSION"></span>

[DecalTexture](class_decal.md#enum_Decal_DecalTexture) **TEXTURE_EMISSION** = `3`

[Texture2D](class_texture2d.md#class_Texture2D) corresponding to [texture_emission](class_decal.md#class_Decal_property_texture_emission).

<span id="class_Decal_constant_TEXTURE_MAX"></span>

[DecalTexture](class_decal.md#enum_Decal_DecalTexture) **TEXTURE_MAX** = `4`

Max size of [DecalTexture](class_decal.md#enum_Decal_DecalTexture) enum.

---

### Property Descriptions

<span id="class_Decal_property_albedo_mix"></span>

[float](class_float.md#class_float) **albedo_mix** = `1.0` [🔗](class_decal.md#class_Decal_property_albedo_mix)

- void **set_albedo_mix** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_albedo_mix** ( )

Blends the albedo [Color](class_color.md#class_Color) of the decal with albedo [Color](class_color.md#class_Color) of the underlying mesh. This can be set to `0.0` to create a decal that only affects normal or ORM. In this case, an albedo texture is still required as its alpha channel will determine where the normal and ORM will be overridden. See also [modulate](class_decal.md#class_Decal_property_modulate).

---

<span id="class_Decal_property_cull_mask"></span>

[int](class_int.md#class_int) **cull_mask** = `1048575` [🔗](class_decal.md#class_Decal_property_cull_mask)

- void **set_cull_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_cull_mask** ( )

Specifies which [VisualInstance3D.layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers) this decal will project on. By default, Decals affect all layers. This is used so you can specify which types of objects receive the Decal and which do not. This is especially useful so you can ensure that dynamic objects don't accidentally receive a Decal intended for the terrain under them.

---

<span id="class_Decal_property_distance_fade_begin"></span>

[float](class_float.md#class_float) **distance_fade_begin** = `40.0` [🔗](class_decal.md#class_Decal_property_distance_fade_begin)

- void **set_distance_fade_begin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_begin** ( )

The distance from the camera at which the Decal begins to fade away (in 3D units).

---

<span id="class_Decal_property_distance_fade_enabled"></span>

[bool](class_bool.md#class_bool) **distance_fade_enabled** = `false` [🔗](class_decal.md#class_Decal_property_distance_fade_enabled)

- void **set_enable_distance_fade** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_distance_fade_enabled** ( )

If `true`, decals will smoothly fade away when far from the active [Camera3D](class_camera3d.md#class_Camera3D) starting at [distance_fade_begin](class_decal.md#class_Decal_property_distance_fade_begin). The Decal will fade out over [distance_fade_begin](class_decal.md#class_Decal_property_distance_fade_begin) + [distance_fade_length](class_decal.md#class_Decal_property_distance_fade_length), after which it will be culled and not sent to the shader at all. Use this to reduce the number of active Decals in a scene and thus improve performance.

---

<span id="class_Decal_property_distance_fade_length"></span>

[float](class_float.md#class_float) **distance_fade_length** = `10.0` [🔗](class_decal.md#class_Decal_property_distance_fade_length)

- void **set_distance_fade_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_length** ( )

The distance over which the Decal fades (in 3D units). The Decal becomes slowly more transparent over this distance and is completely invisible at the end. Higher values result in a smoother fade-out transition, which is more suited when the camera moves fast.

---

<span id="class_Decal_property_emission_energy"></span>

[float](class_float.md#class_float) **emission_energy** = `1.0` [🔗](class_decal.md#class_Decal_property_emission_energy)

- void **set_emission_energy** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_energy** ( )

Energy multiplier for the emission texture. This will make the decal emit light at a higher or lower intensity, independently of the albedo color. See also [modulate](class_decal.md#class_Decal_property_modulate).

---

<span id="class_Decal_property_lower_fade"></span>

[float](class_float.md#class_float) **lower_fade** = `0.3` [🔗](class_decal.md#class_Decal_property_lower_fade)

- void **set_lower_fade** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lower_fade** ( )

Sets the curve over which the decal will fade as the surface gets further from the center of the [AABB](class_aabb.md#class_AABB). Only positive values are valid (negative values will be clamped to `0.0`). See also [upper_fade](class_decal.md#class_Decal_property_upper_fade).

---

<span id="class_Decal_property_modulate"></span>

[Color](class_color.md#class_Color) **modulate** = `Color(1, 1, 1, 1)` [🔗](class_decal.md#class_Decal_property_modulate)

- void **set_modulate** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_modulate** ( )

Changes the [Color](class_color.md#class_Color) of the Decal by multiplying the albedo and emission colors with this value. The alpha component is only taken into account when multiplying the albedo color, not the emission color. See also [emission_energy](class_decal.md#class_Decal_property_emission_energy) and [albedo_mix](class_decal.md#class_Decal_property_albedo_mix) to change the emission and albedo intensity independently of each other.

---

<span id="class_Decal_property_normal_fade"></span>

[float](class_float.md#class_float) **normal_fade** = `0.0` [🔗](class_decal.md#class_Decal_property_normal_fade)

- void **set_normal_fade** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_normal_fade** ( )

Fades the Decal if the angle between the Decal's [AABB](class_aabb.md#class_AABB) and the target surface becomes too large. A value of `0` projects the Decal regardless of angle, a value of `1` limits the Decal to surfaces that are nearly perpendicular.

 **Note:** Setting [normal_fade](class_decal.md#class_Decal_property_normal_fade) to a value greater than `0.0` has a small performance cost due to the added normal angle computations.

---

<span id="class_Decal_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_decal.md#class_Decal_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

Sets the size of the [AABB](class_aabb.md#class_AABB) used by the decal. All dimensions must be set to a value greater than zero (they will be clamped to `0.001` if this is not the case). The AABB goes from `-size/2` to `size/2`.

 **Note:** To improve culling efficiency of "hard surface" decals, set their [upper_fade](class_decal.md#class_Decal_property_upper_fade) and [lower_fade](class_decal.md#class_Decal_property_lower_fade) to `0.0` and set the Y component of the [size](class_decal.md#class_Decal_property_size) as low as possible. This will reduce the decals' AABB size without affecting their appearance.

---

<span id="class_Decal_property_texture_albedo"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_albedo** [🔗](class_decal.md#class_Decal_property_texture_albedo)

- void **set_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture) ) *const*

[Texture2D](class_texture2d.md#class_Texture2D) with the base [Color](class_color.md#class_Color) of the Decal. Either this or the [texture_emission](class_decal.md#class_Decal_property_texture_emission) must be set for the Decal to be visible. Use the alpha channel like a mask to smoothly blend the edges of the decal with the underlying object.

 **Note:** Unlike [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) whose filter mode can be adjusted on a per-material basis, the filter mode for **Decal** textures is set globally with ProjectSettings.rendering/textures/decals/filter.

---

<span id="class_Decal_property_texture_emission"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_emission** [🔗](class_decal.md#class_Decal_property_texture_emission)

- void **set_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture) ) *const*

[Texture2D](class_texture2d.md#class_Texture2D) with the emission [Color](class_color.md#class_Color) of the Decal. Either this or the [texture_albedo](class_decal.md#class_Decal_property_texture_albedo) must be set for the Decal to be visible. Use the alpha channel like a mask to smoothly blend the edges of the decal with the underlying object.

 **Note:** Unlike [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) whose filter mode can be adjusted on a per-material basis, the filter mode for **Decal** textures is set globally with ProjectSettings.rendering/textures/decals/filter.

---

<span id="class_Decal_property_texture_normal"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_normal** [🔗](class_decal.md#class_Decal_property_texture_normal)

- void **set_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture) ) *const*

[Texture2D](class_texture2d.md#class_Texture2D) with the per-pixel normal map for the decal. Use this to add extra detail to decals.

 **Note:** Unlike [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) whose filter mode can be adjusted on a per-material basis, the filter mode for **Decal** textures is set globally with ProjectSettings.rendering/textures/decals/filter.

 **Note:** Setting this texture alone will not result in a visible decal, as [texture_albedo](class_decal.md#class_Decal_property_texture_albedo) must also be set. To create a normal-only decal, load an albedo texture into [texture_albedo](class_decal.md#class_Decal_property_texture_albedo) and set [albedo_mix](class_decal.md#class_Decal_property_albedo_mix) to `0.0`. The albedo texture's alpha channel will be used to determine where the underlying surface's normal map should be overridden (and its intensity).

---

<span id="class_Decal_property_texture_orm"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_orm** [🔗](class_decal.md#class_Decal_property_texture_orm)

- void **set_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture) ) *const*

[Texture2D](class_texture2d.md#class_Texture2D) storing ambient occlusion, roughness, and metallic for the decal. Use this to add extra detail to decals.

 **Note:** Unlike [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) whose filter mode can be adjusted on a per-material basis, the filter mode for **Decal** textures is set globally with ProjectSettings.rendering/textures/decals/filter.

 **Note:** Setting this texture alone will not result in a visible decal, as [texture_albedo](class_decal.md#class_Decal_property_texture_albedo) must also be set. To create an ORM-only decal, load an albedo texture into [texture_albedo](class_decal.md#class_Decal_property_texture_albedo) and set [albedo_mix](class_decal.md#class_Decal_property_albedo_mix) to `0.0`. The albedo texture's alpha channel will be used to determine where the underlying surface's ORM map should be overridden (and its intensity).

---

<span id="class_Decal_property_upper_fade"></span>

[float](class_float.md#class_float) **upper_fade** = `0.3` [🔗](class_decal.md#class_Decal_property_upper_fade)

- void **set_upper_fade** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_upper_fade** ( )

Sets the curve over which the decal will fade as the surface gets further from the center of the [AABB](class_aabb.md#class_AABB). Only positive values are valid (negative values will be clamped to `0.0`). See also [lower_fade](class_decal.md#class_Decal_property_lower_fade).

---

### Method Descriptions

<span id="class_Decal_method_get_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture) ) *const* [🔗](class_decal.md#class_Decal_method_get_texture)

Returns the [Texture2D](class_texture2d.md#class_Texture2D) associated with the specified [DecalTexture](class_decal.md#enum_Decal_DecalTexture). This is a convenience method, in most cases you should access the texture directly.

For example, instead of `albedo_tex = $Decal.get_texture(Decal.TEXTURE_ALBEDO)`, use `albedo_tex = $Decal.texture_albedo`.

One case where this is better than accessing the texture directly is when you want to copy one Decal's textures to another. For example:

.. tabs::

```
```

    for i in Decal.TEXTURE_MAX:
        $NewDecal.set_texture(i, $OldDecal.get_texture(i))

```
```

    for (int i = 0; i < (int)Decal.DecalTexture.Max; i++)
    {
        GetNode<Decal>("NewDecal").SetTexture(i, GetNode<Decal>("OldDecal").GetTexture(i));
    }

---

<span id="class_Decal_method_set_texture"></span>

void **set_texture** ( type: [DecalTexture](class_decal.md#enum_Decal_DecalTexture), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_decal.md#class_Decal_method_set_texture)

Sets the [Texture2D](class_texture2d.md#class_Texture2D) associated with the specified [DecalTexture](class_decal.md#enum_Decal_DecalTexture). This is a convenience method, in most cases you should access the texture directly.

For example, instead of `$Decal.set_texture(Decal.TEXTURE_ALBEDO, albedo_tex)`, use `$Decal.texture_albedo = albedo_tex`.

One case where this is better than accessing the texture directly is when you want to copy one Decal's textures to another. For example:

.. tabs::

```
```

    for i in Decal.TEXTURE_MAX:
        $NewDecal.set_texture(i, $OldDecal.get_texture(i))

```
```

    for (int i = 0; i < (int)Decal.DecalTexture.Max; i++)
    {
        GetNode<Decal>("NewDecal").SetTexture(i, GetNode<Decal>("OldDecal").GetTexture(i));
    }
