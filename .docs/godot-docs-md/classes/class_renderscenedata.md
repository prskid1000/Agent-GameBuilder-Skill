<span id="class_RenderSceneData"></span>

## RenderSceneData

**Inherits:** [Object](class_object.md#class_Object)

**Inherited By:** [RenderSceneDataExtension](class_renderscenedataextension.md#class_RenderSceneDataExtension), [RenderSceneDataRD](class_renderscenedatard.md#class_RenderSceneDataRD)

Abstract render data object, holds scene data related to rendering a single frame of a viewport.

### Description

Abstract scene data object, exists for the duration of rendering a single viewport. See also [RenderSceneDataRD](class_renderscenedatard.md#class_RenderSceneDataRD), [RenderData](class_renderdata.md#class_RenderData), and [RenderDataRD](class_renderdatard.md#class_RenderDataRD).

 **Note:** This is an internal rendering server object. Do not instantiate this class from a script.

### Methods


| [Projection](class_projection.md#class_Projection) | [get_cam_projection](class_renderscenedata.md#class_RenderSceneData_method_get_cam_projection) ( ) const |
| --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_cam_transform](class_renderscenedata.md#class_RenderSceneData_method_get_cam_transform) ( ) const |
| [RID](class_rid.md#class_RID) | [get_uniform_buffer](class_renderscenedata.md#class_RenderSceneData_method_get_uniform_buffer) ( ) const |
| [int](class_int.md#class_int) | [get_view_count](class_renderscenedata.md#class_RenderSceneData_method_get_view_count) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_view_eye_offset](class_renderscenedata.md#class_RenderSceneData_method_get_view_eye_offset) ( view: [int](class_int.md#class_int) ) const |
| [Projection](class_projection.md#class_Projection) | [get_view_projection](class_renderscenedata.md#class_RenderSceneData_method_get_view_projection) ( view: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_RenderSceneData_method_get_cam_projection"></span>

[Projection](class_projection.md#class_Projection) **get_cam_projection** ( ) *const* [🔗](class_renderscenedata.md#class_RenderSceneData_method_get_cam_projection)

Returns the camera projection used to render this frame.

 **Note:** If more than one view is rendered, this will return a combined projection.

---

<span id="class_RenderSceneData_method_get_cam_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_cam_transform** ( ) *const* [🔗](class_renderscenedata.md#class_RenderSceneData_method_get_cam_transform)

Returns the camera transform used to render this frame.

 **Note:** If more than one view is rendered, this will return a centered transform.

---

<span id="class_RenderSceneData_method_get_uniform_buffer"></span>

[RID](class_rid.md#class_RID) **get_uniform_buffer** ( ) *const* [🔗](class_renderscenedata.md#class_RenderSceneData_method_get_uniform_buffer)

Return the [RID](class_rid.md#class_RID) of the uniform buffer containing the scene data as a UBO.

---

<span id="class_RenderSceneData_method_get_view_count"></span>

[int](class_int.md#class_int) **get_view_count** ( ) *const* [🔗](class_renderscenedata.md#class_RenderSceneData_method_get_view_count)

Returns the number of views being rendered.

---

<span id="class_RenderSceneData_method_get_view_eye_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **get_view_eye_offset** ( view: [int](class_int.md#class_int) ) *const* [🔗](class_renderscenedata.md#class_RenderSceneData_method_get_view_eye_offset)

Returns the eye offset per view used to render this frame. This is the offset between our camera transform and the eye transform.

---

<span id="class_RenderSceneData_method_get_view_projection"></span>

[Projection](class_projection.md#class_Projection) **get_view_projection** ( view: [int](class_int.md#class_int) ) *const* [🔗](class_renderscenedata.md#class_RenderSceneData_method_get_view_projection)

Returns the view projection per view used to render this frame.

 **Note:** If a single view is rendered, this returns the camera projection. If more than one view is rendered, this will return a projection for the given view including the eye offset.
