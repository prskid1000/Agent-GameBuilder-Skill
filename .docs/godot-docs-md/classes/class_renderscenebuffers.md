<span id="class_RenderSceneBuffers"></span>

## RenderSceneBuffers

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [RenderSceneBuffersExtension](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension), [RenderSceneBuffersRD](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD)

Abstract scene buffers object, created for each viewport for which 3D rendering is done.

### Description

Abstract scene buffers object, created for each viewport for which 3D rendering is done. It manages any additional buffers used during rendering and will discard buffers when the viewport is resized. See also [RenderSceneBuffersRD](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD).

 **Note:** This is an internal rendering server object. Do not instantiate this class from a script.

### Methods


| void | [configure](class_renderscenebuffers.md#class_RenderSceneBuffers_method_configure) ( config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration) ) |
| --- | --- |

---

### Method Descriptions

<span id="class_RenderSceneBuffers_method_configure"></span>

void **configure** ( config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration) ) [🔗](class_renderscenebuffers.md#class_RenderSceneBuffers_method_configure)

This method is called by the rendering server when the associated viewport's configuration is changed. It will discard the old buffers and recreate the internal buffers used.
