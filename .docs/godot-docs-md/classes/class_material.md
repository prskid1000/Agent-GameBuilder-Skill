<span id="class_Material"></span>

## Material

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BlitMaterial](class_blitmaterial.md#class_BlitMaterial), [CanvasItemMaterial](class_canvasitemmaterial.md#class_CanvasItemMaterial), [FogMaterial](class_fogmaterial.md#class_FogMaterial), [PanoramaSkyMaterial](class_panoramaskymaterial.md#class_PanoramaSkyMaterial), [ParticleProcessMaterial](class_particleprocessmaterial.md#class_ParticleProcessMaterial), [PhysicalSkyMaterial](class_physicalskymaterial.md#class_PhysicalSkyMaterial), [PlaceholderMaterial](class_placeholdermaterial.md#class_PlaceholderMaterial), [ProceduralSkyMaterial](class_proceduralskymaterial.md#class_ProceduralSkyMaterial), [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial)

Virtual base class for applying visual properties to an object, such as color and roughness.

### Description

**Material** is a base resource used for coloring and shading geometry. All materials inherit from it and almost all [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) derived nodes carry a **Material**. A few flags and parameters are shared between all material types and are configured here.

Importantly, you can inherit from **Material** to create your own custom material type in script or in GDExtension.

### Tutorials

- 3D Material Testers Demo

- Third Person Shooter (TPS) Demo

### Properties


| [Material](class_material.md#class_Material) | [next_pass](class_material.md#class_Material_property_next_pass) |
| --- | --- |
| [int](class_int.md#class_int) | [render_priority](class_material.md#class_Material_property_render_priority) |

### Methods


| [bool](class_bool.md#class_bool) | [_can_do_next_pass](class_material.md#class_Material_private_method__can_do_next_pass) ( ) | virtual | const |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_can_use_render_priority](class_material.md#class_Material_private_method__can_use_render_priority) ( ) | virtual | const |
| [Mode](class_shader.md#enum_Shader_Mode) | [_get_shader_mode](class_material.md#class_Material_private_method__get_shader_mode) ( ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_get_shader_rid](class_material.md#class_Material_private_method__get_shader_rid) ( ) | virtual | required | const |
| [Resource](class_resource.md#class_Resource) | [create_placeholder](class_material.md#class_Material_method_create_placeholder) ( ) const |
| void | [inspect_native_shader_code](class_material.md#class_Material_method_inspect_native_shader_code) ( ) |

---

### Constants

<span id="class_Material_constant_RENDER_PRIORITY_MAX"></span>

**RENDER_PRIORITY_MAX** = `127` [🔗](class_material.md#class_Material_constant_RENDER_PRIORITY_MAX)

Maximum value for the [render_priority](class_material.md#class_Material_property_render_priority) parameter.

<span id="class_Material_constant_RENDER_PRIORITY_MIN"></span>

**RENDER_PRIORITY_MIN** = `-128` [🔗](class_material.md#class_Material_constant_RENDER_PRIORITY_MIN)

Minimum value for the [render_priority](class_material.md#class_Material_property_render_priority) parameter.

---

### Property Descriptions

<span id="class_Material_property_next_pass"></span>

[Material](class_material.md#class_Material) **next_pass** [🔗](class_material.md#class_Material_property_next_pass)

- void **set_next_pass** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_next_pass** ( )

Sets the **Material** to be used for the next pass. This renders the object again using a different material.

 **Note:** [next_pass](class_material.md#class_Material_property_next_pass) materials are not necessarily drawn immediately after the source **Material**. Draw order is determined by material properties, [render_priority](class_material.md#class_Material_property_render_priority), and distance to camera.

 **Note:** This only applies to [StandardMaterial3D](class_standardmaterial3d.md#class_StandardMaterial3D) s and [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) s with type "Spatial".

---

<span id="class_Material_property_render_priority"></span>

[int](class_int.md#class_int) **render_priority** [🔗](class_material.md#class_Material_property_render_priority)

- void **set_render_priority** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_render_priority** ( )

Sets the render priority for objects in 3D scenes. Higher priority objects will be sorted in front of lower priority objects. In other words, all objects with [render_priority](class_material.md#class_Material_property_render_priority) `1` will render on top of all objects with [render_priority](class_material.md#class_Material_property_render_priority) `0`.

 **Note:** This only applies to [StandardMaterial3D](class_standardmaterial3d.md#class_StandardMaterial3D) s and [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) s with type "Spatial".

 **Note:** This will not impact how transparent objects are sorted relative to opaque objects or how dynamic meshes will be sorted relative to other opaque meshes. This is because all transparent objects are drawn after all opaque objects and all dynamic opaque meshes are drawn before other opaque meshes.

---

### Method Descriptions

<span id="class_Material_private_method__can_do_next_pass"></span>

[bool](class_bool.md#class_bool) **_can_do_next_pass** ( ) *virtual* *const* [🔗](class_material.md#class_Material_private_method__can_do_next_pass)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if [next_pass](class_material.md#class_Material_property_next_pass) should be shown in the editor or not.

---

<span id="class_Material_private_method__can_use_render_priority"></span>

[bool](class_bool.md#class_bool) **_can_use_render_priority** ( ) *virtual* *const* [🔗](class_material.md#class_Material_private_method__can_use_render_priority)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if [render_priority](class_material.md#class_Material_property_render_priority) should be shown in the editor or not.

---

<span id="class_Material_private_method__get_shader_mode"></span>

[Mode](class_shader.md#enum_Shader_Mode) **_get_shader_mode** ( ) *virtual* |required| *const* [🔗](class_material.md#class_Material_private_method__get_shader_mode)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools.

---

<span id="class_Material_private_method__get_shader_rid"></span>

[RID](class_rid.md#class_RID) **_get_shader_rid** ( ) *virtual* |required| *const* [🔗](class_material.md#class_Material_private_method__get_shader_rid)

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools. Used to access the RID of the **Material**'s [Shader](class_shader.md#class_Shader).

---

<span id="class_Material_method_create_placeholder"></span>

[Resource](class_resource.md#class_Resource) **create_placeholder** ( ) *const* [🔗](class_material.md#class_Material_method_create_placeholder)

Creates a placeholder version of this resource ([PlaceholderMaterial](class_placeholdermaterial.md#class_PlaceholderMaterial)).

---

<span id="class_Material_method_inspect_native_shader_code"></span>

void **inspect_native_shader_code** ( ) [🔗](class_material.md#class_Material_method_inspect_native_shader_code)

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also [Shader.inspect_native_shader_code()](class_shader.md#class_Shader_method_inspect_native_shader_code).
