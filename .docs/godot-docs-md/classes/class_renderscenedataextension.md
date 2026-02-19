<span id="class_RenderSceneDataExtension"></span>

## RenderSceneDataExtension

**Inherits:** [RenderSceneData](class_renderscenedata.md#class_RenderSceneData) **<** [Object](class_object.md#class_Object)

This class allows for a RenderSceneData implementation to be made in GDExtension.

### Description

This class allows for a RenderSceneData implementation to be made in GDExtension.

### Methods


| [Projection](class_projection.md#class_Projection) | [_get_cam_projection](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_cam_projection) ( ) | virtual | const |
| --- | --- | --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_get_cam_transform](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_cam_transform) ( ) | virtual | const |
| [RID](class_rid.md#class_RID) | [_get_uniform_buffer](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_uniform_buffer) ( ) | virtual | const |
| [int](class_int.md#class_int) | [_get_view_count](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_view_count) ( ) | virtual | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_view_eye_offset](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_view_eye_offset) ( view: [int](class_int.md#class_int) ) | virtual | const |
| [Projection](class_projection.md#class_Projection) | [_get_view_projection](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_view_projection) ( view: [int](class_int.md#class_int) ) | virtual | const |

---

### Method Descriptions

<span id="class_RenderSceneDataExtension_private_method__get_cam_projection"></span>

[Projection](class_projection.md#class_Projection) **_get_cam_projection** ( ) *virtual* *const* [🔗](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_cam_projection)

Implement this in GDExtension to return the camera [Projection](class_projection.md#class_Projection).

---

<span id="class_RenderSceneDataExtension_private_method__get_cam_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_get_cam_transform** ( ) *virtual* *const* [🔗](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_cam_transform)

Implement this in GDExtension to return the camera [Transform3D](class_transform3d.md#class_Transform3D).

---

<span id="class_RenderSceneDataExtension_private_method__get_uniform_buffer"></span>

[RID](class_rid.md#class_RID) **_get_uniform_buffer** ( ) *virtual* *const* [🔗](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_uniform_buffer)

Implement this in GDExtension to return the [RID](class_rid.md#class_RID) of the uniform buffer containing the scene data as a UBO.

---

<span id="class_RenderSceneDataExtension_private_method__get_view_count"></span>

[int](class_int.md#class_int) **_get_view_count** ( ) *virtual* *const* [🔗](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_view_count)

Implement this in GDExtension to return the view count.

---

<span id="class_RenderSceneDataExtension_private_method__get_view_eye_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_view_eye_offset** ( view: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_view_eye_offset)

Implement this in GDExtension to return the eye offset for the given `view`.

---

<span id="class_RenderSceneDataExtension_private_method__get_view_projection"></span>

[Projection](class_projection.md#class_Projection) **_get_view_projection** ( view: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_renderscenedataextension.md#class_RenderSceneDataExtension_private_method__get_view_projection)

Implement this in GDExtension to return the view [Projection](class_projection.md#class_Projection) for the given `view`.
