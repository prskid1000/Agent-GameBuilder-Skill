<span id="class_RenderDataExtension"></span>

## RenderDataExtension

**Inherits:** [RenderData](class_renderdata.md#class_RenderData) **<** [Object](class_object.md#class_Object)

This class allows for a RenderData implementation to be made in GDExtension.

### Description

This class allows for a RenderData implementation to be made in GDExtension.

### Methods


| [RID](class_rid.md#class_RID) | [_get_camera_attributes](class_renderdataextension.md#class_RenderDataExtension_private_method__get_camera_attributes) ( ) | virtual | const |
| --- | --- | --- | --- |
| [RID](class_rid.md#class_RID) | [_get_environment](class_renderdataextension.md#class_RenderDataExtension_private_method__get_environment) ( ) | virtual | const |
| [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) | [_get_render_scene_buffers](class_renderdataextension.md#class_RenderDataExtension_private_method__get_render_scene_buffers) ( ) | virtual | const |
| [RenderSceneData](class_renderscenedata.md#class_RenderSceneData) | [_get_render_scene_data](class_renderdataextension.md#class_RenderDataExtension_private_method__get_render_scene_data) ( ) | virtual | const |

---

### Method Descriptions

<span id="class_RenderDataExtension_private_method__get_camera_attributes"></span>

[RID](class_rid.md#class_RID) **_get_camera_attributes** ( ) *virtual* *const* [🔗](class_renderdataextension.md#class_RenderDataExtension_private_method__get_camera_attributes)

Implement this in GDExtension to return the [RID](class_rid.md#class_RID) for the implementation's camera attributes object.

---

<span id="class_RenderDataExtension_private_method__get_environment"></span>

[RID](class_rid.md#class_RID) **_get_environment** ( ) *virtual* *const* [🔗](class_renderdataextension.md#class_RenderDataExtension_private_method__get_environment)

Implement this in GDExtension to return the [RID](class_rid.md#class_RID) of the implementation's environment object.

---

<span id="class_RenderDataExtension_private_method__get_render_scene_buffers"></span>

[RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) **_get_render_scene_buffers** ( ) *virtual* *const* [🔗](class_renderdataextension.md#class_RenderDataExtension_private_method__get_render_scene_buffers)

Implement this in GDExtension to return the implementation's [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) object.

---

<span id="class_RenderDataExtension_private_method__get_render_scene_data"></span>

[RenderSceneData](class_renderscenedata.md#class_RenderSceneData) **_get_render_scene_data** ( ) *virtual* *const* [🔗](class_renderdataextension.md#class_RenderDataExtension_private_method__get_render_scene_data)

Implement this in GDExtension to return the implementation's [RenderSceneDataExtension](class_renderscenedataextension.md#class_RenderSceneDataExtension) object.
