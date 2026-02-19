<span id="class_RenderData"></span>

## RenderData

**Inherits:** [Object](class_object.md#class_Object)

**Inherited By:** [RenderDataExtension](class_renderdataextension.md#class_RenderDataExtension), [RenderDataRD](class_renderdatard.md#class_RenderDataRD)

Abstract render data object, holds frame data related to rendering a single frame of a viewport.

### Description

Abstract render data object, exists for the duration of rendering a single viewport. See also [RenderDataRD](class_renderdatard.md#class_RenderDataRD), [RenderSceneData](class_renderscenedata.md#class_RenderSceneData), and [RenderSceneDataRD](class_renderscenedatard.md#class_RenderSceneDataRD).

 **Note:** This is an internal rendering server object. Do not instantiate this class from a script.

### Methods


| [RID](class_rid.md#class_RID) | [get_camera_attributes](class_renderdata.md#class_RenderData_method_get_camera_attributes) ( ) const |
| --- | --- |
| [RID](class_rid.md#class_RID) | [get_environment](class_renderdata.md#class_RenderData_method_get_environment) ( ) const |
| [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) | [get_render_scene_buffers](class_renderdata.md#class_RenderData_method_get_render_scene_buffers) ( ) const |
| [RenderSceneData](class_renderscenedata.md#class_RenderSceneData) | [get_render_scene_data](class_renderdata.md#class_RenderData_method_get_render_scene_data) ( ) const |

---

### Method Descriptions

<span id="class_RenderData_method_get_camera_attributes"></span>

[RID](class_rid.md#class_RID) **get_camera_attributes** ( ) *const* [🔗](class_renderdata.md#class_RenderData_method_get_camera_attributes)

Returns the [RID](class_rid.md#class_RID) of the camera attributes object in the [RenderingServer](class_renderingserver.md#class_RenderingServer) being used to render this viewport.

---

<span id="class_RenderData_method_get_environment"></span>

[RID](class_rid.md#class_RID) **get_environment** ( ) *const* [🔗](class_renderdata.md#class_RenderData_method_get_environment)

Returns the [RID](class_rid.md#class_RID) of the environment object in the [RenderingServer](class_renderingserver.md#class_RenderingServer) being used to render this viewport.

---

<span id="class_RenderData_method_get_render_scene_buffers"></span>

[RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) **get_render_scene_buffers** ( ) *const* [🔗](class_renderdata.md#class_RenderData_method_get_render_scene_buffers)

Returns the [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) object managing the scene buffers for rendering this viewport.

---

<span id="class_RenderData_method_get_render_scene_data"></span>

[RenderSceneData](class_renderscenedata.md#class_RenderSceneData) **get_render_scene_data** ( ) *const* [🔗](class_renderdata.md#class_RenderData_method_get_render_scene_data)

Returns the [RenderSceneData](class_renderscenedata.md#class_RenderSceneData) object managing this frames scene data.
